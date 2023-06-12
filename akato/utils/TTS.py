import requests
import urllib.parse


# (改语音可以看"speaker.json"及"voicevox")
def voicevox_tts(tts, voice):
    voicevox_url = 'http://localhost:50021'
    params_encoded = urllib.parse.urlencode({'text': tts, 'speaker': voice})
    request = requests.post(f'{voicevox_url}/audio_query?{params_encoded}')
    params_encoded = urllib.parse.urlencode({'speaker': voice, 'enable_interrogative_upspeak': True})
    request = requests.post(f'{voicevox_url}/synthesis?{params_encoded}', json=request.json())

    with open("test.wav", "wb") as outfile:
        outfile.write(request.content)
