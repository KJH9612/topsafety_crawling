from bs4 import BeautifulSoup
import requests
import re
import math

def getItems(url, headers, html_dom, pattern):
    #상품 정보
    lists = []

    # 메인페이지 접속
    req = requests.get(url, headers=headers)
    parser = BeautifulSoup(req.text, "html.parser")

    # 상품 페이지 정규식으로 추출
    product_number = int(re.findall(pattern, str(parser.select_one(html_dom)))[0])
    total_page = math.ceil(product_number / 16)

    for page in range(0, total_page):
        cur_page_info = requests.get(url+'?page='+str(page+1), headers=headers)
        cur_page_parser = BeautifulSoup(cur_page_info.text, "html.parser")
        # print(cur_page_parser)
        before_items = cur_page_parser.select('div.xans-product-listnormal>ul>li>div.box>a')

        # print(before_items)

        #print()
        lists += re.findall('anchorBoxName_[0-9]+', str(before_items))

    # print()

    return re.findall('[0-9]+', str(lists))
    # 페이지 아이템 추출
    #tmp = parser.select(html_DOM)