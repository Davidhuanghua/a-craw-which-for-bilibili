import re
from prettytable import PrettyTable
import importlib, sys
import requests
from bs4 import BeautifulSoup
importlib.reload(sys)

url = 'https://www.bilibili.com/video/BV1fx411F75x?from=search&seid=5432403958009611009'
resp = requests.get(url)
match_rule = r'cid=(.*?)&aid'
oid = re.search(match_rule, resp.text).group().replace('cid=', '').replace('&aid', '')

xml_url = 'https://api.bilibili.com/x/v1/dm/list.so?oid='+oid
html = requests.get('https://api.bilibili.com/x/v1/dm/list.so?oid='+oid)
resp2 = BeautifulSoup(html.text, 'lxml')


# 视频信息
def start_craw(url='http://api.bilibili.com/archive_stat/stat?aid={}&type=jsonp'):
    print('开始爬取……')
    headers = {}
    x = PrettyTable(['视频编号', '播放量', '弹幕', '回复', '收藏', '硬币', '分享'])
    t = 0
    i = 434946

    while (t < 100):
        r = requests.get(url.format(i), headers=headers)
        if r.status_code == 200:
            try:
                # 数据清洗
                j = r.json()['data']
                favorite = j['favorite']
                danmaku = j['danmaku']
                coin = j['coin']
                view = j['view']
                share = j['share']
                reply = j['reply']
                favorite = str(favorite)
                danmaku = str(danmaku)
                coin = str(coin)
                view = str(view)
                share = str(share)
                reply = str(reply)
                av_num = "av" + str(i)
                x.add_row([av_num, view, danmaku, reply, favorite, coin, share])
            except Exception as e:
                pass
        else:
            break
        i = i + 1
        t = t + 1
    with open('video信息.txt', 'a')as f:
        f.write(str(x))
    print('爬取完成')

start_craw()

# 弹幕
resp2 = resp2.encode("raw_unicode_escape").decode()
result = re.findall("\">(.*?)</d>", resp2)

mylog = open('danmu.txt', mode='a', encoding='utf-8')
for i in result:
    print(i, file=mylog)
mylog.close()
print('弹幕内容已分行保存在danmu.txt文件中')
