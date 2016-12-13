import re
import requests

__author__ = 'hzwer'

home = 'http://hzwer.com/'
LINE_NUM = 0
PAGE_NUM = 0


def GetPage(url):
    global LINE_NUM, PAGE_NUM
    r = requests.get(url)
    content = r.text
    pattern = re.compile('line-height: 16px !important;">\n(.*?)</text', re.S)
    code = re.findall(pattern, content)
    if(code):
        sum = 0
        for j in code:
            sum = sum + len(j.splitlines())
        LINE_NUM = LINE_NUM + sum
        PAGE_NUM = LINE_NUM + 1
        print('url: {} {}行代码，合计{}行代码'.format(url, sum, LINE_NUM))


if __name__ == '__main__':
    for i in range(1, 10000):
        url = home + str(i) + '.html'
        GetPage(url)
    print('共{}个页面，{}行代码'.format(PAGE_NUM, LINE_NUM))
