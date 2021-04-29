import getCateName
import getURLItems
import re
import time
import math

url = 'http://topsafety.co.kr'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

MainCate = getCateName.getCategory(url, header, 'li.xans-record- > a', '([0-9]+\/")', 3)

# 카테고리 정규식
specialRE = '[/]+'
# 카테고리 개수 카운트
cnt = 0
#총 상품 {상품카테고리 : [상품코드], .....}
lists = dict()

# 카테고리 정보 수집
for cateName, info in MainCate.items():
    main_cate_no, link = info.values()

    SubCate = getCateName.getCategory(url+link, header, 'ul.menuCategory > li.xans-product-displaycategory > a', '([0-9]+\/")', 3)
    for subName, cate_link_info in SubCate.items():
        sub_cate_no, sub_cate_link = cate_link_info.values()

        RESubName = re.findall(".* ", str(subName))[0]
        RESubName = RESubName.strip()

        # print(a, '/'.join(re.split(specialRE, cateName)).replace('ㆍ', ' '),
        # cate_link_info['cate_no'], '/'.join(re.split(specialRE, RESubName)), sep="\t\t")

        lists[main_cate_no+sub_cate_no] = getURLItems.getItems(url+sub_cate_link, header, 'p.prdCount>strong', '[0-9]+')
        # print(getData.strip())
print(lists)
# print(cnt)
# print(MainCate)
