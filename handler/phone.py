import subprocess
from time import sleep


def unlock_phone(d):
    sleep(10)
    subprocess.call("adb shell input keyevent 26", shell=True)  # 唤醒关闭屏幕
    d.double_click(0.5, 0.5)
    d.drag(0.5, 0.8, 0.5, 0.1)
    d(text="1").click()
    d(text="2").click()
    d(text="3").click()
    d(text="4").click()
    sleep(3)
    d.click(0.5, 0.5)
