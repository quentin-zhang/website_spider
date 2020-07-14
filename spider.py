import urllib.request
import urllib.parse
import hashlib
import time
import random
import json

m = hashlib.md5()
class YouDaoCollect:
    def __init__(self):
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        data = self.form_data()
        req = urllib.request.Request(url, data)
        req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
        response = urllib.request.urlopen(url, data)
        html = response.read().decode('utf-8')
        print(111)
        print(html)
        print(222)
    def form_data(self):
        i = 'thinking in java'
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
        data = urllib.parse.urlencode(data).encode('utf-8')
        return data
yd = YouDaoCollect()
# target = json.loads(html)
# print(target['translateResult'][0][0]['tgt'])