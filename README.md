# ai-waifu
这是一个利用人工智能创造的虚拟vtb的项目，力求一个能够更加流畅交流的ai

## 使用说明：  
  将你的openai api存放于config.py文件中  
  安装所有需要的库，requiremen文件内还有缺失，需要自己安装一部分  
  运行程序前提前打开 voicevox（下载完后运行run.exe即可）  
  运行程序前提前打开 vtube studio（不用的话把协程启动注释了就行）  

在中国境内运行的实例，https://www.bilibili.com/video/BV1xu411Y7re

## 本项目目前使用的工具有：  
  1、voicevox    https://voicevox.hiroshiba.jp/  
  2、google翻译  python自带的库呐  
  3、openai gpt3 这个不用多说了吧，去创建自己的api吧  https://platform.openai.com/account/api-keys


## 目前的项目只拥有一个雏形，只实现了以下功能：  
  1、利用openai进行文字转语音  
  2、向gpt3进行提问并获取回答  
  3、通过google翻译将回答转换成日文  
  4、使用voicevox将日文转化为语音输出  
  5、制作简易动作模板，通过自制vts插件输入  
看着还挺简单对吧，但是由于中国的网络环境这些动作实现还是有3-5秒的延迟，有点悲哀
以及使用gpt聊天容易出现问题，性格单一死板


# 已有版本
## A1.0	简易的，瑕疵的【这只是一个开端，初版中的初版吧】  √
	1-1、基本框架雏形（语音识别，聊天功能，话语功能）  
	1-2、简易VTS插件（简易动作功能）  
