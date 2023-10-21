# 介绍
目前只有 领取巡光之礼 自动刷毁灭花萼 冰遗器的功能

！！！先将安装教程和使用教程全部看一遍再决定要不要安装 因为安装过程极为繁琐！！！

！！！可能出现各种意想不到的bug！！！

# 安装教程
0.5.关闭任何杀毒软件，否则python安装可能会出问题。

0.75.前往https://digi.bib.uni-mannheim.de/tesseract/下载32/64位的任意版本setup.exe，安装，将安装完的tesseract文件夹名字改成Tesseract
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

3.代码117行上下有一句if n_time <= '2023-10-10':  代码189行上下有一句elif n_time > '2023-10-10':		这两句意思是：如果时间在2023-10-10前(包括这一天) 刷毁灭花萼 如果时间在2023-10-10后 刷冰遗器 根据自己的需要改引号内的数值

4.yc.txt文件中的数值是每次执行的延迟 每次执行的下一次都会比这一次晚一段时间 这是为了重复在每天同一时间运行的情况下体力能回复满 每个循环周期结束后（比如每个周末）最好把yc改成0

5.！！建议搭配上windows定时开机和定时任务使用 并且保证程序第一次运行的时候体力是满的 不然实在想不到能用这个干什么！！

QQ:898777578
