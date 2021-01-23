import requests, time, re, csv
from bs4 import BeautifulSoup
import codecs
import re

with open(r'./小说.csv', 'ab+')as fp:
    fp.write(codecs.BOM_UTF8)
f = open(r'./小说.csv', 'a+', newline='', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(('名称', '作者', '评分', '人数', '简介'))
r'./小说.csv'
urls = ['https://book.douban.com/tag/小说?start={}&type=T/'.format(str(i)) for i in range(0, 41, 20)]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
for url in urls:
    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    infos = soup.select(".subject-item")

    for it in infos:
        name = it.h2.a['title']

        author = it.select_one(".pub").text.strip()

        score = it.select_one('.rating_nums').text

        num1 = it.select_one('.pl').text.strip()
        num2 = re.findall("\d+", num1)[0]

        content = it.p.text
        writer.writerow((name, author, score, num2, content))
        time.sleep(1)
f.close()