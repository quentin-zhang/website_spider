import paragraph
import yaml
f = open('translate.yml', 'r')
trans_conf = yaml.load(f)
w_url = trans_conf['translate']['single']
para = paragraph.Paragraph(w_url)