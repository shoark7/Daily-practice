"""
Long time no see. :) It's been about 2 weeks from the last post.
My post today is BeautifulSoup. It's a famous html, xml parser in python.
I've read 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/' twice, yesterday and today,
and I'll do simple html parsing today.

Target site is 'NAVER'(http://www.naver.com/), the most, most famous search engine in Korea.
I'll do simple examples today.

Start date = 2016/11/03
End date = 2016/11/03
"""

from pprint import pprint
import string
import re
import requests
from bs4 import BeautifulSoup


##########################################################################################
#### Example 1. Find all tags used in 'NAVER' alphabetically and save them in a dict. ####
##########################################################################################


def find_all_tags(url, duplicate=False):
    """
    Find all tags used in site of given url and return a dict of tags alphabetically.
    :param url: target site url to look for tags
    :param duplicate: Whether or not that duplicate tags are included in dict.
    :return: A dict of tags. Keys are alphabets and values are list of tags.
    """
    while True:
        try:
            html_text = requests.get(url).text
        except:
            raise TypeError("URL's not a right type.")
        else:
            break


    _soup = BeautifulSoup(html_text, 'html.parser')
    _result_dict = {}
    for c in string.ascii_uppercase:
        tag_list = [tag.name for tag in _soup.find_all() if tag.name.startswith(c.lower())]
        # All html tags are lowercases, so we should use str.lower method.

        if not duplicate:
            tag_list = list(set(tag_list))
            _result_dict[c] = tag_list
        # If duplication of tags in results are not allowed, make them unique.
    return _result_dict

# pprint(find_all_tags('http://www.naver.com'))
"""results are
{'A': ['area', 'address', 'a'],
 'B': ['button', 'body', 'br'],
 'C': [],
 'D': ['dl', 'dt', 'dd', 'div'],
 'E': ['em'],
 'F': ['fieldset', 'form'],
 'G': [],
 'H': ['h1', 'h4', 'h3', 'hr', 'html', 'head', 'h2'],
 'I': ['i', 'input', 'img', 'iframe'],
 'J': [],
 'K': [],
 'L': ['link', 'legend', 'li', 'label'],
 'M': ['map', 'meta'],
 'N': ['noscript'],
 'O': ['ol', 'option', 'optgroup'],
 'P': ['p'],
 'Q': [],
 'R': [],
 'S': ['span', 'select', 'script', 'strong'],
 'T': ['title'],
 'U': ['ul'],
 'V': [],
 'W': [],
 'X': [],
 'Y': [],
 'Z': []}
"""


##############################################################
#### Example 2. Extract realtime search ranking in NAVER. ####
##############################################################

def find_search_rank_list():
    """
    This function is NAVER dedicated. NAVER shows realtime search ranking
    and we'll extract it by BS4.
    I can't show you now, but you should check source inspector to find html tree of NAVER.
    If you're interested, contact me and I will kindly tell you everything.
    :return: A list of realtime search rank from 1st to 10th.
    """
    html_text = requests.get('http://www.naver.com').text
    naver_soup = BeautifulSoup(html_text, 'html.parser')
    rank_list = naver_soup.select_one('#realrank')
    # '#' is a symbol of ID in html. A html page has only one id,
    # so we can use select_one, not 'select'. The return value is a tag, not 'list'.

    # In rank_list, it has 'li's so we iterate over them and extract keyword from them.
    return [li.a.get('title') for li in rank_list('li')][:-1]

    """
    1. rank_list('li') equals to rank_list.find_all('li). It extracts all 'li's in rank_list
    2. In each li, we go deep into a and get 'title' attribute value.
    3. I don't know why but length of final results is 11, not 10. We exclude last element.
    """

print(find_search_rank_list())
"""results
['월드시리즈', '채프먼', '한광옥', '시카고컵스', '장시호', '질투의 화신', '회오리축구단', '100마일', '채동욱', '장희진']
It varies depending on time, because it is "realtime" search.
"""



##################################################################################
#### Example 3. Extract blog post titles with given name and limits in NAVER. ####
##################################################################################

def get_blog_title(keyword, limit=20):
    """
    Naver offers blog platform for users. When we search something in NAVER,
    it shows many blog posts which contain contents about keyword. We will extract
    blog post titles.
    :param keyword: Search keyword you type in.
    :param limit: How number of titles you want.
    :return: A list of blog titles containing contents about the keyword.
    """

    # Naver uses pagination for blog posts and each page has 10 titles.
    # If we want 45 titles, we should iterate over 4 * 10 plus 5 titles.
    # url 'https://search.naver.com/search.naver?where=post&sm=tab_pge&
    # query=keyword&st=sim&date_option=0&date_from=&date_to=&dup_remove=1&post_blogurl=&post_blogurl_without=&srchby=all&nso=&ie=utf8
    # &start=11'
    url_front = 'https://search.naver.com/search.naver?where=post&sm=tab_pge&query='
    url_back = '&st=sim&date_option=0&date_from=&date_to=&dup_remove=1&post_blogurl=&post_blogurl_without=&srchby=all&nso=&ie=utf8&start='
    # url_full = url_front + keyword + url_back + limit

    result_list = []
    limit_over_10 = limit // 10
    limit_under_10 = limit % 10

    # Start coding!
    for i in range(limit_over_10 + (1 if limit_under_10 else 0)):
        start = str(i) + '1'
        url_full = url_front + keyword + url_back + start
        response = requests.get(url_full).text
        soup_naver = BeautifulSoup(response, 'html.parser')

        page_container = soup_naver.find('ul', id='elThumbnailResultArea')
        if page_container == None:
            print(keyword+'에 대한 결과가 없습니다.')
            return None
        # page_container is a 'ul'
        # post id = sp_blog1, sp_blog2, sp_blog3, ...

        for j in range(1, (10 if i != limit_over_10 else limit_under_10)+1):
            post_id = 'sp_blog_' + str(j)
            try:
                result_list.append(page_container.find('li', id=post_id).dt.a.get('title'))
            except:
                pass


    return result_list

pprint(get_blog_title('로스트 인 더스트', 100))