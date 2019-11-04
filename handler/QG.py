import uiautomator2 as u2

from utils.database import db
from utils.utils import local_sleep, get_screenshot
from utils import ocr, utils


def login(d, username, passwd):
    d.app_start("cn.xuexi.android")  # 启动
    local_sleep(10, "启动app")
    if d(resourceId="cn.xuexi.android:id/fl_login_mode").exists:
        d(resourceId="cn.xuexi.android:id/et_phone_input").set_text(username)
        d(resourceId="cn.xuexi.android:id/et_pwd_login").set_text(passwd)
        d.press("back")
        d(resourceId="cn.xuexi.android:id/btn_next").click()
        local_sleep(3)
        d.click(0.9, 0.9)
    local_sleep(5, "进入主页面")
    print("已登录")


def get_count(d):
    """
    获取 阅读文章和视听学习 还需几次
    """
    d(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
    local_sleep(2, '显示积分页面')
    d.drag(0.5, 0.5, 0.2, 0.2)

    img_name = "screen.png"
    get_screenshot(img_name)
    crop_img = utils.img_crop(img_name, 0, 350, 1080, 2100)
    rj, _ = ocr.get_info(crop_img)

    data = {
        'article': 0,
        'video': 0
    }
    num = rj['words_result_num']
    words = rj['words_result']
    for i in range(num):
        if words[i]['words'] == '阅读文章':
            data['article'] = 6 - int(words[i + 3]['words'][2:3])
            # print(6 - int(words[i + 3]['words'][2:3]))

        if words[i]['words'] == '视听学习':
            data['video'] = 6 - int(words[i + 3]['words'][2:3])
            # print(6 - int(words[i + 3]['words'][2:3]))

    print(data)
    # 返回
    d.press("back")

    return data


def watch_video_news(d, count=6):
    """
    看新闻联播
    """
    d(resourceId="cn.xuexi.android:id/home_bottom_tab_button_contact").click()
    d(text="联播频道").click()
    local_sleep(3, '等待新闻联播页面渲染完成')

    current_count = db.query_video_today_number()
    print("今日已看 %d 次新闻联播" % current_count)
    while current_count < count:
        obj_list = d(resourceId="cn.xuexi.android:id/general_card_title_id")
        for obj in obj_list:
            title = obj.get_text()
            if not db.query_video_by_title(title):
                obj.click()
                local_sleep(2, '第 %d 次播放新闻联播' % (current_count + 1), d)
                db.insert_video(title)
                current_count += 1
                print('第 %s 次播放新闻联播完成' % current_count)
                d.press("back")
                # 新闻联播每天更新，全部都是昨天的，所以只要有记录就是看过
                if current_count < count:
                    break
            print(title)

        d.drag(0.5, 0.8, 0.5, 0.1)

    print("今日观看新闻联播已完成")


def click_collection(d):
    # 存在视频情况，遇到就pass掉
    try:
        w, h = d.window_size()
        if h > 1920:
            d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[2]').click()
        else:
            d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[2]').click()

        d.xpath('//android.widget.GridView/android.widget.RelativeLayout[3]').click()
    except:
        pass


def watch_article(d, count=6):
    """
    看推荐文章
    """
    d(resourceId="cn.xuexi.android:id/home_bottom_tab_button_work").click()
    d(text="推荐").click()
    local_sleep(3, '等待推荐页面渲染完成')

    current_count = db.query_article_today_number()
    print("今日已看 %d 次推荐文章" % current_count)
    while current_count < count:
        obj_list = d(resourceId="cn.xuexi.android:id/general_card_title_id")
        for obj in obj_list:
            title = obj.get_text()
            if not db.query_article_by_title(title):
                obj.click()
                click_collection(d)
                local_sleep(2, '第 %d 次看新闻' % (current_count + 1), d)
                db.insert_article(title)
                current_count += 1
                print('第 %s 次看新闻完成' % current_count)
                d.press("back")
                if current_count < count:
                    break
            print(title)

        d.drag(0.5, 0.8, 0.5, 0.1)

    print("今日看推荐文章已完成")


def share_winxin(d):
    w, h = d.window_size()

    d(resourceId="cn.xuexi.android:id/home_bottom_tab_button_work").click()
    d(text="推荐").click()
    d.xpath('//android.widget.ListView/android.widget.FrameLayout[2]').click()
    local_sleep(3, '等待推荐页面渲染完成')

    if h > 1920:
        d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[2]').click()
    else:
        d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[2]').click()
    # d.xpath('//android.widget.GridView/android.widget.RelativeLayout[4]').click()
    d(resourceId="cn.xuexi.android:id/txt_gv_item", text="分享给微信\n好友").click()
    local_sleep(2, '等待微信界面渲染完成')
    d.press("back")
    if h > 1920:
        d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[2]').click()
    else:
        d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[2]').click()
    # d.xpath('//android.widget.GridView/android.widget.RelativeLayout[4]').click()
    d(resourceId="cn.xuexi.android:id/txt_gv_item", text="分享给微信\n好友").click()
    local_sleep(2, '等待微信界面渲染完成')
    d.press("back")

    # 返回主页面
    d.press("back")


if __name__ == "__main__":
    d = u2.connect()  # 这里是adb devices得到的
    w, h = d.window_size()
    print(w, h)
    # login(d)
    # get_count(d)
