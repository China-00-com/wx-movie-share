# coding:utf-8

import re
import json
import random
import requests
from urllib import unquote_plus
try:
    import cPickle as pickle
except:
    import pickle as pickle


UA_PC = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
UA_MOB = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"

miaopai_code_re = re.compile(r"http://www.miaopai.com/show/(.*?)__\.htm")
miaopai_template = "http://gslb.miaopai.com/stream/{}__.mp4"

bilibili_code_re = re.compile(r"http://www.bilibili.com(.*?)video/av(\d+)\.html")
bilibili_api = "http://api.bilibili.com/playurl?aid={}&page=1&platform=html5&quality=1&vtype=mp4&type=jsonp"

xiaokaxiu_code_re = re.compile(r"http://v.xiaokaxiu.com/v/(.*?)__\.html")
xiaokaxiu_template = miaopai_template

weibo_url_re = re.compile(r'video_src=(.*?)&playerType')


def miaopai(url):
    code = miaopai_code_re.findall(url)
    if code is None:
        return None
    result = miaopai_template.format(code[0])
    return result


def bilibili(url):

    headers = {"user-agent": UA_PC}
    cookies = requests.get(url, headers=headers).cookies
    code = bilibili_code_re.findall(url)
    print code
    if code == []:
        return None
    url = bilibili_api.format(code[0][1])
    print url
    content = requests.get(url, headers=headers, cookies=cookies).content[1:-2]
    print content
    if content[0] != "{": return None
    json_data = json.loads(content)
    urls = json_data.get("durl")
    if urls is None: return None
    return urls["0"]["url"]


def xiaokaxiu(url):
    code = xiaokaxiu_code_re.findall(url)
    if code ==[]:
        return None
    result = xiaokaxiu_template.format(code[0])
    return result


def weibo(url):
    pkls = [
        "41488bd76ac6ca8c58602e7680a9da52.pkl",
        "b74fb2a9635aba6490153a4f99d3bf9d.pkl"
    ]

    pkl_name = random.choice(pkls)
    pkl_file = file(pkl_name, 'rb')
    user = pickle.load(pkl_file)
    pkl_file.close()
    session = user["session"]
    headers = user["headers"]
    content = session.get(url).content
    if not content:return None
    video_urls = weibo_url_re.findall(content)
    if not video_urls:return None
    video_url = unquote_plus(video_urls[0])
    return video_url




if __name__ == "__main__":
    print weibo("http://weibo.com/tv/v/Eg0cFd6Ia")