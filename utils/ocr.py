import base64
import json
from urllib import parse

import pickledb
import requests


class BaiduOCR(object):
    def __init__(self, api_key, secret_key, ocr_taoken_db_path='ocr_token.db'):
        self.api_key = api_key
        self.secret_key = secret_key
        self.ocr_taoken_db_path = ocr_taoken_db_path

    def get_token(self, ):
        """
        文档:
            https://ai.baidu.com/docs#/Auth/top
        """
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
            self.api_key, self.secret_key)
        response = requests.get(host)
        if response:
            rj = response.json()
            print(json.dumps(rj))
            db = pickledb.load(self.ocr_taoken_db_path, False)
            db.set('token', json.dumps(rj))
            db.dump()

    def read_token(self):
        db = pickledb.load(self.ocr_taoken_db_path, False)
        token = json.loads(db.get('token'))
        # print(token)
        return token['access_token']

    def get_info(self, img_path=''):
        """
        文档：
            https://ai.baidu.com/docs#/OCR-API-GeneralBasic/3d4cee4a
        """
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
        header = {
            "Content-Type": "application/x-www-form-urlencoded  "
        }
        data = {
            "access_token": self.read_token(),
        }

        with open(img_path, "rb") as f:
            # b64encode是编码，b64decode是解码
            base64_data = base64.b64encode(f.read())
            # base64.b64decode(base64data)
            # print(base64_data)
            data['image'] = base64_data

        data = parse.urlencode(data)

        r = requests.post(url, headers=header, data=data)
        rj = r.json()
        print(json.dumps(rj))
        msg = ''
        for s in rj['words_result']:
            msg += s['words']
        print('msg: ' + msg)
        return rj, msg
