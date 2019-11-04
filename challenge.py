"""
挑战题

需要百度ocr识别，密钥用自己的
url: https://ai.baidu.com/
"""
from utils import ocr, utils


def main():
    # ocr.get_token()  # 执行一次会在本地保存
    utils.get_screenshot('cache/screen.png')
    dst_name = utils.img_crop('cache/screen.png', 0, 500, 1080, 1200)
    _, msg = ocr.get_info(dst_name)
    utils.search_info(msg)


if __name__ == "__main__":
    main()
