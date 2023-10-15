import os
import pyautogui
from PIL import Image
import pytesseract
from time import sleep
import time
import pydirectinput
import win32gui



#!!!!!!!!!!!!!!!!!!!!!!!!!!请输入你的屏幕分辨率(默认1920*1080)!!!!!!!!!!!!!!!!!!!!!!!!!!#
screensizex=1920;screensizey=1080
def scx(sizex):   #sizeclickx
    af_sizex=int(sizex*screensizex/1920)
    return(af_sizex)
def scy(sizey):   #sizeclicky
    af_sizey=int(sizey*screensizey/1080)
    return(af_sizey)

#!!!!!!!!!!!!!!!!!!!!!!!!!!windows每次自动执行任务后延迟2.5分钟，保证体力完全回复至240!!!!!!!!!!!!!!!!!!!!!!!!!!#
f=open('yc.txt', encoding='utf-8')
yc_list=[]
for line in f:
    yc_list.append(int(line.strip()))
yc_num=yc_list[0]
sleep(yc_num)
yc_num=yc_num+150
with open('yc.txt', 'w') as yc:
    yc.write(str(yc_num))
print(yc_num)


#自动战斗(仅支持毁灭拟态花萼及冰遗器)
def fight():
    g=0
    while g==0:
        sleep(0.5)
        g = pyautogui.locateOnScreen('sixth1.png')
        if g==None:
            g=0
        if g!=0:
            center = pyautogui.center(g)
            sleep(0.5)
            pyautogui.click(scx(1760), scy(42))
os.popen('Game\StarRail.exe')
a=0
print(1)
sleep(10)
try:
    hwnd = win32gui.FindWindow('Star Rail', 'Star Rail')
    # 置顶窗口
    win32gui.SetForegroundWindow(hwnd)
except:
    pass
while a==0:
    # 获取屏幕分辨率
    screenWidth, screenHeight = pyautogui.size()
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()
    # 将截图保存为临时文件
    screenshot.save('screenshot.png')
    # 使用 pytesseract 识别文字
    text = pytesseract.image_to_string(Image.open('screenshot.png'), lang='chi_sim', config='--psm 6')
    print(text)
    #进入游戏
    if '点击进' in text:
        print('1145141919810')
        sleep(1)
        pydirectinput.click()
        sleep(0.1)
        pydirectinput.click()
        a=1
    else:
        sleep(1)
#f1
b=0
while b==0:
    sleep(0.5)
    b = pyautogui.locateOnScreen('first.png')
    if b == None:
        b=0
    print(b)
    if b!=0:
        sleep(2)
        pydirectinput.press('f1')
        print('111111')


hdlj_x=scx(187)
hdlj_y=scy(139)
pyautogui.moveTo(hdlj_x, hdlj_y)
for i in range(13):
    pyautogui.moveTo(hdlj_x, hdlj_y)
    pyautogui.click()
    hdlj_y = hdlj_y+scy(60)
    for i in range(5):
        sleep(0.1)
        c = pyautogui.locateOnScreen('xgzl_beiyong.png')
        if c==None:
            c=0
        if c!=0:
            center = pyautogui.center(c)
            pyautogui.click(center)



n_time = time.strftime('%Y-%m-%d', time.localtime())
if n_time <= '2023-10-10':
    print('huae')
    #退出f1界面
    pyautogui.press('esc')
    sleep(1)
    #进入f4界面
    pyautogui.press('f4')
    sleep(1)
    #毁灭拟态花萼传送
    nt = 0
    while nt == 0:
        sleep(0.5)
        nt = pyautogui.locateOnScreen('second.png')
        if nt == None:
            nt = 0
        if nt != 0:
            center = pyautogui.center(nt)  # 寻找图片的中心
            pyautogui.click(center)
    d=0
    while d==0:
        sleep(0.5)
        d = pyautogui.locateOnScreen('third.png')
        if d==None:
            d=0
        if d!=0:
            center = pyautogui.center(d)  # 寻找图片的中心
            pyautogui.click(center)
    e=0
    while e==0:
        sleep(0.5)
        e = pyautogui.locateOnScreen('forth.png')
        if e==None:
            e=0
        if e!=0:
            center = pyautogui.center(e)  # 寻找图片的中心
            pyautogui.click(center)
    #设置挑战次数并挑战
    f=0
    while f==0:
        sleep(0.5)
        f = pyautogui.locateOnScreen('fifth.png')
        if f==None:
            f=0
        if f!=0:
            center = pyautogui.center(f)
            sleep(0.5)
            pyautogui.click(scx(1745), scy(900))
            sleep(0.5)
            pyautogui.click(center)
            sleep(1.5)
            pyautogui.click(center)

    fight()
    #重复战斗 消耗剩余体力
    h=0
    tili=240
    while h==0 and tili>0:
        sleep(0.5)
        h = pyautogui.locateOnScreen('seventh.png')
        if h==None:
            h=0
        if h!=0:
            center = pyautogui.center(h)
            sleep(0.5)
            pyautogui.click(center)
            tili=tili-60
            fight()
    sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('f4')
    pyautogui.keyUp('f4')
    pyautogui.keyUp('alt')
elif n_time > '2023-10-10':
    print('yiqi')
    # 退出f1界面
    pyautogui.press('esc')
    sleep(1)
    # 进入f4界面
    pyautogui.press('f4')
    sleep(1)
    # 冰系遗器传送
    nt = 0
    while nt == 0:
        sleep(0.5)
        nt = pyautogui.locateOnScreen('second.png')
        if nt == None:
            nt = 0
        if nt != 0:
            center = pyautogui.center(nt)  # 寻找图片的中心
            pyautogui.click(center)
    print('qinshisuidong')
    d = 0
    while d==0:
        sleep(0.5)
        d = pyautogui.locateOnScreen('yiqi1.png')
        if d==None:
            d=0
        if d!=0:
            center = pyautogui.center(d)  # 寻找图片的中心
            pyautogui.click(center)
    e = 0
    while e == 0:
        sleep(0.5)
        e = pyautogui.locateOnScreen('yiqi2.png')
        if e == None:
            e = 0
        if e != 0:
            center = pyautogui.center(e)  # 寻找图片的中心
            pyautogui.click(center)
    # 挑战
    f = 0
    while f == 0:
        sleep(0.5)
        f = pyautogui.locateOnScreen('fifth.png')
        if f == None:
            f = 0
        if f != 0:
            center = pyautogui.center(f)
            sleep(0.5)
            pyautogui.click(center)
            sleep(1.5)
            pyautogui.click(center)

    fight()
    # 重复战斗 消耗剩余体力
    h = 0
    tili = 240
    while h == 0 and tili > 0:
        sleep(0.5)
        h = pyautogui.locateOnScreen('yiqi3.png')
        if h == None:
            h = 0
        if h != 0:
            pyautogui.click(1204, 947)
            h = 0
            tili=tili-40
    print('zl')
    sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('f4')
    pyautogui.keyUp('f4')
    pyautogui.keyUp('alt')
