import urllib.request
import re
import paragraph
import yaml
from bs4 import BeautifulSoup
class WanquTranslate:
    def __init__(self,wanqu_url):
        self.request_url = wanqu_url
    def execute(self):
        response = urllib.request.urlopen(self.request_url)
        html = response.read()
        data = html.decode('utf-8')
        soup = BeautifulSoup(data,"lxml")
        link_list = soup.findAll('a', attrs={'href': re.compile("^(http://.*)(utm_source=wanqu.co.*)$|^(https://.*)(utm_source=wanqu.co.*)$")})
        for link in link_list:
            w_url = link.get('href')
            paragraph.Paragraph(w_url)
if __name__=='__main__':
    f = open('translate.yml', 'r')
    trans_conf = yaml.load(f)
    t = WanquTranslate(trans_conf['translate']['stags'])
    # t = WanquTranslate('https://wanqu.co/issues/1238/')
    t.execute()
