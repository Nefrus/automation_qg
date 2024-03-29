"""
红米note7,全面屏，关闭全面屏手势
"""
import sys

sys.path.append("..")

import uiautomator2 as u2

from handler.QG import watch_video_news, watch_article, share_winxin
from utils.utils import local_sleep


def main():
    d = u2.connect()  # 这里是adb devices得到的
    d.app_start("cn.xuexi.android")  # 启动
    local_sleep(15, '等待启动完成')  # 等待启动完成
    share_winxin(d)  # 分享操作
    watch_article(d)  # 读文章的时候顺便收藏
    watch_video_news(d)
    print("已完成，请检查积分")


if __name__ == "__main__":
    main()
