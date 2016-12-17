import re
import requests
import threading
import multiprocessing

__author__ = 'hzwer'

home = 'http://hzwer.com/'
LINE_NUM = 0
PAGE_NUM = 0

lock = threading.Lock()


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
        if(lock.acquire()):
            LINE_NUM = LINE_NUM + sum
            PAGE_NUM = PAGE_NUM + 1
            print('url: {} {}行代码，合计{}行代码'.format(url, sum, LINE_NUM))
            lock.release()


record = []
if __name__ == '__main__':
    pool = multiprocessing.Pool(8)
    for i in range(1, 100):
        url = home + str(i) + '.html'
        process = pool.apply_async(GetPage(url))
    pool.close()
    pool.join()

    print('共{}个页面，{}行代码'.format(PAGE_NUM, LINE_NUM))
