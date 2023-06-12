import googletrans          # google翻译


# 翻译核心程序
def translate_text(text, target_language):
    try:
        translator = googletrans.Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception:
        print("error translate")
        return "error has ranslate"


# 翻译(报错重新执行，最多重复3次翻译)
def translate_google(text, target_language):
    try_num = 1
    recivetest = translate_text(text, target_language)
    while recivetest == "error has ranslate":
        print("try again")
        recivetest = translate_text(text, target_language)
        try_num = try_num+1
        if try_num >= 3:
            if target_language == "JA":     # 保险起见这里不做二次翻译怕影响后续语音功能
                recivetest = "申し訳ありませんが、はっきりと聞いていませんでした"
            else:
                recivetest = translate_text("对不起没有听清楚", target_language)
            break
    return recivetest
