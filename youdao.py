# -*- coding: UTF-8 -*-
import hashlib
import random
import requests
import time


s = requests.Session()
m = hashlib.md5()

class Dict:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding' : 'gzip, deflate',
            'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control' : 'no-cache',
            'Connection' : 'keep-alive',
            # 'Content-Length': 200
            'Host' : 'fanyi.youdao.com',
            'Origin' : 'http://fanyi.youdao.com',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Referer': 'http://fanyi.youdao.com/',
            'contentType': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie' : '_ntes_nnid=dc654481a4df5ed84af7f876f3401711,1494387288102; OUTFOX_SEARCH_USER_ID_NCOO=1428372036.53805; OUTFOX_SEARCH_USER_ID=-1251891461@10.168.11.18; fanyi-ad-id=40789; fanyi-ad-closed=1; UM_distinctid=1616e46ce5482-046bed22cf122-4323461-1fa400-1616e46ce554bf; SESSION_FROM_COOKIE=www.google.com; JSESSIONID=aaapsnHiaecJd9C6iCahw; ___rl__test__cookies=1519353828292'
        }
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.google.com/'
        

    def base_config(self):
        """
        设置基本的参数，cookie
        """
        s.get('http://fanyi.youdao.com/')

    def translate(self,translate_text):
        s = requests.Session()
        m = hashlib.md5()
        self.base_config()
        i = translate_text
        salf = str(int(time.time() * 1000) + random.randint(0, 9))
        n = 'fanyideskweb' + i + salf + "rY0D^0'nM0}g5Mm1z%1G4"
        m.update(n.encode('utf-8'))
        sign = m.hexdigest()
        data = {
            'i': i,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salf,
            'sign': sign,
            'doctype': 'json',
            'version': "2.1",
            'keyfrom': "fanyi.web",
            'action': "FY_BY_DEFAULT",
            'typoResult': 'false'
        }
        
        resp = s.post(self.url, headers=self.headers, data=data)
        array_trans = []
        result_trans = ''
        try:
            array_trans = resp.json()['translateResult']
            for outer_trans in array_trans:
                for ele_trans in outer_trans:
                    result_trans += ele_trans['tgt']
                result_trans += ' \n '
        except Exception as e:
            print('Error:', e)
        finally:
            print('error in translate...')
        return result_trans

# dic = Dict()
# resp = dic.translate('thinking in java')
# print(resp)