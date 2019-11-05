"""
挑战题

需要百度ocr识别，密钥用自己的
url: https://ai.baidu.com/
"""
import sys

sys.path.append("..")

from run import config

from utils.ocr import BaiduOCR
from utils import utils


def main():
    ocr = BaiduOCR(config.baidu_ocr_api_key, config.baidu_ocr_secret_key, config.ocr_token_db_path)
    # ocr.get_token()  # 执行一次会在本地保存
    utils.get_screenshot('cache/screen.png')
    dst_name = utils.img_crop('cache/screen.png', 0, 500, 1080, 1200)
    _, msg = ocr.get_info(dst_name)
    utils.search_info(msg)


if __name__ == "__main__":
    main()
