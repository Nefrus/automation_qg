import os
import subprocess
import time
import webbrowser
from urllib import parse

from PIL import Image


def local_sleep(t, s='', d=None):
    tmp = t
    while tmp:
        time.sleep(1)
        if d:
            d.click(0.01, 0.5)  # 长时间不操作可能断开连接
        tmp -= 1
        print("\r%s需等待 %s 秒，还需 %s 秒" % (s, str(t), str(tmp)), end='')
    print()


def get_screenshot(name='screen.png'):
    dirname = os.path.dirname(name)
    if dirname and not os.path.exists(dirname):
        os.mkdir(dirname)
    sc = "adb shell mkdir -p /sdcard/" + dirname
    subprocess.call(sc, shell=True)
    sc = "adb shell rm -rf /sdcard/" + name
    subprocess.call(sc, shell=True)
    sc = "adb shell screencap -p /sdcard/" + name
    subprocess.call(sc, shell=True)
    sc = "adb pull /sdcard/" + name + " " + name
    subprocess.call(sc, shell=True)
    sc = "adb shell rm -rf /sdcard/" + name
    subprocess.call(sc, shell=True)


def img_crop(img_url, x1, y1, x2, y2):
    im = Image.open(img_url)
    name, suffix = img_url.split('.')
    dst_name = name + '2.jpg'
    # im.crop((x1, y1, x2, y2)).save(dst_name)
    im.crop((x1, y1, x2, y2)).convert('RGB').save(dst_name)
    return dst_name


def search_info(msg):
    head = '学习强国 3G免费网 '
    msg = head + msg
    print('search msg: ' + msg)

    msg = parse.urlencode({"wd": msg[:100]})
    url = "https://www.baidu.com/s?" + msg + "&rsv_spt=1&rsv_iqid=0xd95b90fe00008a9c&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&inputT=65675&rsv_sug4=65675"
    # url = "https://www.google.com/search?safe=strict&source=hp&ei=mPm4XdH3I5GkmAWC_7aYCQ&q=%E6%B5%8B%E8%AF%95&oq=%E6%B5%8B%E8%AF%95&gs_l=psy-ab.3..0l10.1589.2299..2608...0.0..0.160.924.0j7......0....1..gws-wiz.....0.oFpRYeAacOw&ved=0ahUKEwjRo6L0-8LlAhUREqYKHYK_DZMQ4dUDCAY&uact=5"
    webbrowser.open(url, new=0, autoraise=True)
