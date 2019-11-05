"""
努比亚z7max
"""
import subprocess
from time import sleep

import uiautomator2 as u2

from handler.QG import watch_video_news, watch_article, share_winxin
from handler.phone import unlock_phone
from utils.utils import local_sleep


def login(d, username, passwd):
    d.app_start("cn.xuexi.android")  # 启动
    local_sleep(20, "启动app")
    if d(resourceId="cn.xuexi.android:id/fl_login_mode").exists:
        d.click(0.877, 0.4)  # 清除原有号码
        d(resourceId="cn.xuexi.android:id/et_phone_input").set_text(username)
        d(resourceId="cn.xuexi.android:id/et_pwd_login").set_text(passwd)
        d.press("back")
        d(resourceId="cn.xuexi.android:id/btn_next").click()
        local_sleep(3)
        d.click(0.9, 0.96)
    local_sleep(5, "进入主页面")
    print("已登录")


def main():
    d = u2.connect()  # 这里是adb devices得到的
    d.app_stop("cn.xuexi.android")  # 启动
    print(d.info)
    print(d.window_size())

    unlock_phone(d)
    login(d, "", "")
    d.app_start("cn.xuexi.android")  # 启动
    local_sleep(15, '等待启动完成')  # 等待启动完成
    # 以下操作，只要回到app主界面就可以单独使用，也可自己改代码控制
    # share_winxin(d)  # 分享操作 1分
    watch_article(d)  # 读文章的时候顺便收藏
    watch_video_news(d)
    print("已完成，请检查积分")
    subprocess.call("adb shell input keyevent 26", shell=True)  # 唤醒关闭屏幕


if __name__ == "__main__":
    main()
