'''
1. 定位到2022必看热片
2. 从2022必看片中提取到子页面的链接地址
3. 请求子页面的链接地址。拿到我们想要的下载地址...
'''

import requests
import re

domain = 'https://www.dytt89.com/'
resp = requests.get(domain, verify=False)       # verify = False 去掉安全验证
resp.encoding = 'gb2312'        # 指定编码方式
# print(resp.text)

# 拿到ul里面的li
obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td '
                  r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')
    # print(ul)

    # 提取子页面链接：
    result2 = obj2.finditer(ul)
    for i in result2:
        href = i.group('href')
        # 拼接子页面的url地址： 域名+子页面地址
        child_href = domain + href.strip("/")
        child_href_list.append(child_href)      # 保存子页面链接

for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    print(f"{result3.group('movie')}:{result3.group('download')}")
    break       # 测试用
