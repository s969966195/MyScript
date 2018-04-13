# coding=utf-8
import requests
from lxml import etree
import sys


def produceText(title, text):
    with open('./'+u'2007政府工作报告', 'w') as f:
        for ti in title:
            f.write(ti.xpath('string(.)').encode('utf-8') + '\n')
        for te in text:
            f.write(te.xpath('string(.)').encode('utf-8') + '\n')


def getText(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    title = html.xpath('//div[@align="center"]//font[@size="4"]')
    text = html.xpath('//div[@align="left"]//font[@size="3"]')
    produceText(title, text)


if __name__ == '__main__':
    url = sys.argv[1]
    getText(url)
