"""
红米note7,全面屏，关闭全面屏手势
"""
from time import sleep

import uiautomator2 as u2

from handler.QG import watch_video_news, watch_article, share_winxin


def main():
    d = u2.connect()  # 这里是adb devices得到的
    d.app_start("cn.xuexi.android")  # 启动
    sleep(10)  # 等待启动完成
    # 以下操作，只要回到app主界面就可以单独使用，也可自己改代码控制
    share_winxin(d)  # 分享操作 1分
    watch_article(d)  # 读文章的时候顺便收藏
    watch_video_news(d)
    print("已完成，请检查积分")


if __name__ == "__main__":
    main()
