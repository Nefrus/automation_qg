import subprocess
from time import sleep


def unlock_phone(d):
    print(d.info)
    print(d.window_size())
    res = subprocess.check_output("adb shell dumpsys window policy | grep mShow", shell=True).decode('utf-8')
    if 'mShowingLockscreen=false' in res or 'mDreamingLockscreen=false' in res:
        subprocess.call("adb shell input keyevent 26", shell=True)  # 唤醒关闭屏幕

    subprocess.call("adb shell input keyevent 26", shell=True)  # 唤醒关闭屏幕
    # subprocess.call("adb shell input keyevent 26", shell=True)  # 唤醒关闭屏幕
    d.double_click(0.5, 0.5)
    d.drag(0.5, 0.8, 0.5, 0.1)
    sleep(2)
    d(text="1").click()
    d(text="2").click()
    d(text="3").click()
    d(text="4").click()
    sleep(3)
    d.click(0.01, 0.01)
