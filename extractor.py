# coding:utf-8

import re
import json
import random
import requests
from urllib import unquote_plus
from urlparse import urljoin

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
    """
    秒拍
    :param url:
    :return:
    """
    code = miaopai_code_re.findall(url)
    if code is None:
        return None
    result = miaopai_template.format(code[0])
    return result


def bilibili(url):
    """
    bilibili （有时能用，有时不能用）
    :param url:
    :return:
    """

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
    """
    小咖秀
    :param url:
    :return:
    """
    code = xiaokaxiu_code_re.findall(url)
    if code == []:
        return None
    result = xiaokaxiu_template.format(code[0])
    return result


def weibo(url):
    """
    微博视频 weibo
    :param url:
    :return:
    """

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
    if not content: return None
    video_urls = weibo_url_re.findall(content)
    if not video_urls: return None
    video_url = unquote_plus(video_urls[0])
    return video_url


def kankannews(url):
    """
    看看新闻 kankannews.com
    :param url:
    :return:
    """
    kankannews_re = re.compile(r'mp4 : \"(.*?)\"')
    content = requests.get(url).content
    result = kankannews_re.findall(content)
    return result[0]


def aipai(url):
    """
    爱拍游戏 aipai.com  http://www.aipai.com/c1/PTk4NiAhbiFoLSc.html
    """
    aipai_url_re = re.compile(r'\"info=(.*?)&amp;avatarName')
    content = requests.get(url).content
    text = aipai_url_re.findall(content)[0]
    text = unquote_plus(text)
    print text
    json_data = json.loads(text)
    print json_data
    print json_data
    video_info = json_data["work"]
    videos = []
    try:
        videos.append(urljoin(video_info["baseURL"], video_info["flvFileName"]))
        videos.append(urljoin(video_info["baseURL"], video_info["flvFileName480"]))
        videos.append(urljoin(video_info["baseURL"], video_info["flvFileName1080"]))
    except:
        pass
    return list(set(videos))


if __name__ == "__main__":
    print aipai("http://www.aipai.com/c1/PTk4NiAhbiFoLSc.html")
