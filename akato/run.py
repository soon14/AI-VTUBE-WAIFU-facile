import time                     # 时间
import wave
import pyaudio
import keyboard
import openai
import json
import sys
import multiprocessing
from vtube import vtube_worker
from config import api_key
from utils.translate import translate_google
from utils.TTS import voicevox_tts
from utils.promptMaker import getPrompt
from utils.subtitle import generate_subtitle

# to help the CLI write unicode characters to the terminal
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

openai.api_key = api_key

conversation = []
# Create a dictionary to hold the message data
history = {"history": conversation}
total_characters = 0
chat_now = ""
owner_name = "sugar"


# 读出翻译结果(此处只针对voicevox生成的语音，"test.wav"是文件路径，要改改这个)
def read_wav():
    chunk = 1024

    try:
        with wave.open("test.wav", 'rb')as wav_file:
            audio = pyaudio.PyAudio()

            stream = audio.open(format=audio.get_format_from_width(wav_file.getsampwidth()),
                                channels=wav_file.getnchannels(),
                                rate=wav_file.getframerate(),
                                output=True)
            data = wav_file.readframes(chunk)
            while data:
                stream.write(data)
                data = wav_file.readframes(chunk)
            stream.stop_stream()
            stream.close()
            audio.terminate()
    except Exception:
        print("error wav")


# 录音功能(录音时间过短进入openai的语音转文字会报错，请一定注意)
def record_audio():
    pressdown_num = 0
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "input.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    print("Recording...")
    while keyboard.is_pressed('RIGHT_SHIFT'):
        data = stream.read(CHUNK)
        frames.append(data)
        pressdown_num = pressdown_num + 1
    print("Stopped recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    if pressdown_num >= 5:         # 粗糙的处理手段
        return 1
    else:
        print("杂鱼杂鱼，好短好短(录音时间过短,按右shift重新录制)")
        return 0


# 使用openai进行文字提取(记得去填你的api)
def transcribe_audio(file):
    global chat_now
    audio_file = open(file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    chat_now = transcript.text
    return chat_now


# function to get an answer from OpenAI
def openai_answer():
    global total_characters, conversation

    total_characters = sum(len(d['content']) for d in conversation)

    while total_characters > 4000:
        try:
            # print(total_characters)
            # print(len(conversation))
            conversation.pop(2)
            total_characters = sum(len(d['content']) for d in conversation)
        except Exception as e:
            print("Error removing old messages: {0}".format(e))

    with open("conversation.json", "w", encoding="utf-8") as f:
        # Write the message data to the file in JSON format
        json.dump(history, f, indent=4)

    prompt = getPrompt()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        max_tokens=128,
        temperature=1,
        top_p=0.9
    )
    message = response['choices'][0]['message']['content']
    conversation.append({'role': 'assistant', 'content': message})

    # translate_text(message)
    return message


if __name__ == '__main__':
    # 共享内存数据
    shared_data = multiprocessing.Value('i', 0)

    process = multiprocessing.Process(target=vtube_worker, args=(shared_data,))
    process.start()

    while 1:
        # 输入要翻译的文本和目标语言代码
        # text = input("请输入要翻译的文本：")
        print("请按住右shift录制问题")
        while 1:
            if keyboard.is_pressed('RIGHT_SHIFT'):
                if record_audio():
                    break
        text = transcribe_audio("input.wav")
        print(owner_name + ":" + text)

        # 将问题发送给openai(这段copy的出了问题请自行解决)
        result = "sugar" + " said " + text
        conversation.append({'role': 'user', 'content': result})
        message = openai_answer()
        print("Akato:", message)
        print("Akato:", message[0:4])

        # 调用翻译函数进行翻译并打印,不知道代码翻下"googletrans代码.txt"
        # translated_text = translate_google(message, "zh-cn")
        # print("中文翻译结果：", translated_text)
        tts = translate_google(message[5:], "JA")
        print("日语翻译结果：", tts)

        generate_subtitle(text, message[5:])

        # 生成语音文件+读出语音文件(改语音可以看"speaker.json"及"voicevox")
        voicevox_tts(tts, 46)

        if message[0:4] == "看右下方":
            shared_data.value = 1
            print("动作1")
        elif message[0:4] == "看左下方":
            shared_data.value = 2
            print("动作2")
        elif message[0:4] == "看右上方":
            shared_data.value = 3
            print("动作3")
        elif message[0:4] == "看左上方":
            shared_data.value = 4
            print("动作4")
        elif message[0:4] == "看向下方":
            shared_data.value = 5
            print("动作5")
        elif message[0:4] == "看向上方":
            shared_data.value = 6
            print("动作6")
        elif message[0:4] == "看向右侧":
            shared_data.value = 7
            print("动作7")
        elif message[0:4] == "看向左侧":
            shared_data.value = 8
            print("动作8")
        elif message[0:4] == "皱起眉头":
            shared_data.value = 9
            print("动作9")
        elif message[0:4] == "向左歪头":
            shared_data.value = 10
            print("动作10")
        elif message[0:4] == "向右歪头":
            shared_data.value = 11
            print("动作11")
        elif message[0:4] == "左右摇头":
            shared_data.value = 12
            print("动作12")

        read_wav()
        shared_data.value = 99
        time.sleep(0.5)     # 无特殊意义的延时,如果出问题就加回来
        with open("output.txt", "w") as f:
            f.truncate(0)
        with open("chat.txt", "w") as f:
            f.truncate(0)

    process.join()
