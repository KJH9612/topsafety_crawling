from bs4 import BeautifulSoup
from urllib import parse
import requests
import re


def getCategory(url, headers, html_dom, pattern, pad=0):
    # url Settings
    # url = 'http://topsafety.co.kr'
    # Header Settings
    # headers = {'User-Agent':'Mozilla/5.0'}
    """
    :rtype: object
    :param url: https://url.com
    :param headers:
    :param html_dom:
    :param pattern:
    :param pad:
    :return: dictionary {CateName:[number, url] ...}
    """

    result = dict()

    # 메인페이지 접속
    req = requests.get(url, headers=headers)
    parser = BeautifulSoup(req.text, "html.parser")

    # 카테고리 부분 추출
    # tmp = parser.select('li.xans-record- > a')
    tmp = parser.select(html_dom)

    # 1차 카테고리 정규식 패턴 추출
    # main_cate_num_pattern = '([0-9]+\/")'
    main_cate_num_result = re.findall('\d+', str(re.findall(pattern, str(tmp))))

    for idx, i in enumerate(main_cate_num_result):
        i = str(i).zfill(pad)
        result[tmp[idx].get_text()] = {'cate_no': i, 'link': tmp[idx]['href']}

    return result


'''
print(getCategory('http://topsafety.co.kr',
                  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'},
                   '([0-9]+\/")', 3))'''