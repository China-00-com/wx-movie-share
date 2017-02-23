# coding:utf-8

import re
import json
import requests

UA_PC = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
UA_MOB = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"

miaopai_code_re = re.compile(r"http://www.miaopai.com/show/(.*?)__\.htm")
miaopai_template = "http://gslb.miaopai.com/stream/{}__.mp4"

bilibili_code_re = re.compile(r"http://www.bilibili.com(.*?)video/av(\d+)\.html")
bilibili_api = "http://api.bilibili.com/playurl?aid={}&page=1&platform=html5&quality=1&vtype=mp4&type=jsonp"

xiaokaxiu_code_re = re.compile(r"http://v.xiaokaxiu.com/v/(.*?)__\.html")
xiaokaxiu_template = miaopai_template

weiboi_url_re = re.compile(r"video_src=(.*?)&")


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
    cookies = requests.get("http://www.weibo.com").cookies
    content = requests.get(url,headers={"User-Agent":UA_PC},cookies=cookies).content
    print content
    result = weiboi_url_re.findall(content)
    return result


if __name__ == "__main__":
    print weibo("http://weibo.com/tv/v/Eg0cFd6Ia")