import urllib.request
import re
from bs4 import BeautifulSoup
import pymysql.cursors
import datetime
import youdao
import time
import yaml

class Paragraph:
    def __init__(self, wanqu_url):
            try:
                f = open('translate.yml', 'r')
                self.trans_conf = yaml.load(f)
                proxies = {
                    'https': 'https://127.0.0.1:1080',
                    'http': 'http://127.0.0.1:1080'
                }
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                }
                print(wanqu_url)
                self.wanqu_url = wanqu_url
                opener = urllib.request.build_opener(
                    urllib.request.ProxyHandler(proxies))
                urllib.request.install_opener(opener)
                req = urllib.request.Request(wanqu_url, headers=headers)
                response = urllib.request.urlopen(req)

                html = response.read()
                data = html.decode('utf-8', errors='ignore')
                soup = BeautifulSoup(data, "lxml")
                self.get_paragraph(soup)

            except Exception as e:
                print('Error:', e)
            finally:
                print('finally...')

    def get_paragraph(self, soup):
        wanqu_text = ''
        translate_text = ''
        
        
        paragraph_list = soup.findAll('p')
        print(len(paragraph_list))
        for parag in paragraph_list:
            pp = parag.text
            wanqu_text = wanqu_text + '  ' + pp + '  \n  '
        
        # ss = self.translate_slice(wanqu_text)
        
        # for sstext in ss:
        #     time.sleep(5)
        #     dic = youdao.Dict()
        #     translate_text = translate_text + dic.translate(sstext)
        wanqu_text = wanqu_text + '  \n  ' + 'URL : ' + self.wanqu_url
        translate_text = translate_text + '  \n  ' + 'URL : ' + self.wanqu_url
        self.persistence(wanqu_text,translate_text)


    def persistence(self, w_text,translate_text):
        # Connect to the database
        connection = pymysql.connect(host=self.trans_conf['mysql']['server'],
                                    user=self.trans_conf['mysql']['user'],
                                    password=self.trans_conf['mysql']['password'],
                                    db=self.trans_conf['mysql']['database'],
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `article` (`Content`, `Collecttime`,`Contributor`,`TranslateContent`,`ArticleURL`) VALUES (%s, %s,%s,%s,%s)"
                cursor.execute(sql, (w_text, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'machine',translate_text,self.wanqu_url))

            connection.commit()

        finally:
            connection.close()
    def translate_slice(self,translate_text):
        return [translate_text[start:start+4000] for start in range(0, len(translate_text), 4000)]
