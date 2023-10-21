# 免责声明
本软件是一个外部工具旨在自动化崩坏星轨的游戏玩法。它被设计成仅通过现有用户界面与游戏交互,并遵守相关法律法规。该软件包旨在提供简化和用户通过功能与游戏交互,并且它不打算以任何方式破坏游戏平衡或提供任何不公平的优势。该软件包不会以任何方式修改任何游戏文件或游戏代码。

This software is open source, free of charge and for learning and exchange purposes only. The developer team has the final right to interpret this project. All problems arising from the use of this software are not related to this project and the developer team. If you encounter a merchant using this software to practice on your behalf and charging for it, it may be the cost of equipment and time, etc. The problems and consequences arising from this software have nothing to do with it.

本软件开源、免费，仅供学习交流使用。开发者团队拥有本项目的最终解释权。使用本软件产生的所有问题与本项目与开发者团队无关。若您遇到商家使用本软件进行代练并收费，可能是设备与时间等费用，产生的问题及后果与本软件无关。

请注意，根据MiHoYo的 [崩坏:星穹铁道的公平游戏宣言]([https://hsr.hoyoverse.com/en-us/news/111244](https://sr.mihoyo.com/news/111246?nav=news&type=notice)):

    "严禁使用外挂、加速器、脚本或其他破坏游戏公平性的第三方工具。"
    "一经发现，米哈游（下亦称“我们”）将视违规严重程度及违规次数，采取扣除违规收益、冻结游戏账号、永久封禁游戏账号等措施。"


# 介绍
目前只有 领取巡光之礼 自动刷毁灭花萼 冰遗器的功能

！！！先将安装教程和使用教程全部看一遍再决定要不要安装 因为安装过程极为繁琐！！！

！！！可能出现各种意想不到的bug！！！

# 安装教程
0.5.关闭任何杀毒软件，否则python安装可能会出问题。

0.75.前往https://digi.bib.uni-mannheim.de/tesseract/ 下载32/64位的任意版本setup.exe，安装，将安装完的tesseract文件夹名字改成Tesseract
     并下载tessdata_fast/中所有文件，放到Tesseract/tessdata文件夹里

1.前往python官网python.org现在python3.11.x版本的python，安装时勾选带"PATH"的选项

2.将所有文件放入星穹铁道文件夹Star Rail内

3.按win+i，输入环境变量，依次点击编辑系统环境变量，环境变量，双击下方系统变量中的Path，将Tesseract路径下的tessdata文件夹的路径复制，点击环境变量中的新建，将路径粘贴进去，确定，点击新建（w），变量名为TESSDATA_PREFIX，变量值为上面tessdata文件夹的路径，确定，确定

4.按win+r，输入cmd，回车，依次输入
	pip install pyautogui
	pip install pytesseract
	pip install pydirectinput
	pip install win32gui    若输入这一行时报错，在cmd里输入pip install pywin32,打开C:\Users\‘这里输入你电脑的用户名’\AppData\Local\Programs\Python\Python311\Lib\site-packages\pywin32_system32，按上面的方法打开path环境变量，将这个地址新建并复制进去，再次输入pip install win32gui
 
5.右键main.py文件，打开属性，点击兼容性，勾选以管理员身份运行

6.先别启动，看看使用教程

# 使用教程
1.右键用idel打开main.py文件

2.若设置中分辨率不是1920*1080，改成1920*1080，若仍卡住不动则将画质设为高，仍卡住不动则大概率需要将所有.png自己截图替换一遍
  调不了1920*1080的，将main文件中的分辨率数值改成游戏中的分辨率，并将所有.png自己截图替换一遍

3.代码117行上下有一句if n_time <= '2023-10-10':  代码189行上下有一句elif n_time > '2023-10-10':		这两句意思是：如果时间在2023-10-10前(包括这一天) 刷花萼 如果时间在2023-10-10后 刷遗器 根据自己的需要改引号内的数值

4.yc.txt文件中的数值是每次执行的延迟 每次执行的下一次都会比这一次晚一段时间 这是为了重复在每天同一时间运行的情况下体力能回复满 每个循环周期结束后（比如每个周末）最好把yc改成0

5.！！建议搭配上windows定时开机和定时任务使用 并且保证程序第一次运行的时候体力是满的 不然实在想不到能用这个干什么！！

6.将游戏内沿用自动战斗设置打开

7.要刷遗器和花萼，修改fort.pngh或yiqi2.png

QQ:898777578
