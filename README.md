# ai-waifu
这是一个利用人工智能创造的虚拟老婆的项目，相信已经有很多人实现了与其对话，那如果能给她赋予肉体呢？

使用说明：  
  将你的openai api存放于config.py文件中  
  安装所有需要的库，requiremen文件内还有缺失，需要自己安装一部分  
  运行程序前提前打开 voicevox（下载完后运行run.exe即可）  
  运行程序前提前打开 vtube studio（不用的话把协程启动注释了就行）  

在中国境内运行的实例，https://www.bilibili.com/video/BV1xu411Y7re

本项目目前使用的工具有：  
  1、voicevox    https://voicevox.hiroshiba.jp/  
  2、google翻译  python自带的库呐  
  3、openai gpt3 这个不用多说了吧，去创建自己的api吧  


目前的项目只拥有一个雏形，只实现了以下功能：  
  1、利用openai进行文字转语音  
  2、向gpt3进行提问并获取回答  
  3、通过google翻译将回答转换成日文  
  4、使用voicevox将日文转化为语音输出  
  5、制作简易动作模板，通过自制vts插件输入  
看着还挺简单对吧，但是由于中国的网络环境这些动作实现还是有3-5秒的延迟，有点无法容忍


基于已实现的功能我称之为V1.0版本，未来目标：  
A1.0	简易的，瑕疵的【这只是一个开端，初版中的初版吧】  
√	1-1、基本框架雏形（语音识别，聊天功能，话语功能）  
√	1-2、简易VTS插件（简易动作功能）  
A2.0	可以投入使用的级别，比较完善的[【A2.0版本可以认为是我最期待的初版】  
	2-1、新的语言模型（负责新的大脑部分）  
	2-2、翻译模块本地化（优化响应速度）  
	2-3、动态语音输入（需要针对中文进行优化，优化响应速度）  
	2-4、语音分段输出（若语音生成时间过长会浪费大量响应时间）  
	2-5、更流畅的随机动作  
A3.0	从这个版本开始做开创性内容【开发时会具有不可预测的困难】  
	3-1、第二个语言模型（负责第二人格，没有人交流是孤单的）
	3-2、真实的脸部动作（希望可以通过ai进行辅助生成）  
	3-3、声音识别（类似于小爱同学和Siri ？）  
A3.1	走一步算一步级别【异常困难级别】  
	3-4、模拟情感（这个暂时没有头绪）  
	3-5、基于情感更换话语功能（也没有头绪）  
	3-6、模拟肢体动作（寄希望于ai了）  
	3-7、初步接入vrchat（实现A3.0的最终夙愿，升级维度）  
A4.0	先别写了，你写的完吗你  
	4-1、目标捕捉，障碍识别，&*%*&^%*&*&@$#@#&#^&)@(&%!#^$%^(!#&)$  
A5.0	你疯了，怎么还有  
	5-1、面向现实，真是疯狂的目标  
