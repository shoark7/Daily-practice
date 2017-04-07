"""
Today is upgrade version of bs4.
Now our target is 'http://www.daum.net'.
Daum is the second largest search engine after NAVER.
Naver is unrivaled, Daum actually one fifth of Naver's power, I think.

Daum has also movie section. Once we get the movie id,
we look for netizen's id's, comments, their personal scores and put them into lists.

Start date = 2016/11/05
End date = 2016/11/05
"""

from pprint import pprint
from bs4 import BeautifulSoup
import requests
from io import BytesIO
import re


def doctor_strange_daum_movie_netizen(pages=10):
    """
    we will find for doctor strange. Cause I like it.
    :param pages: how many data we want. Each page has 10 parts.
    :return: list of lists(id, comment, score)
    """

    query_front = 'http://movie.daum.net/moviedb/grade?movieId=88187&type=netizen&page='
    result_list = []

    for i in range(1, pages + 1):
        url_full = query_front + str(i)
        response_text = requests.get(url_full).text
        soup = BeautifulSoup(response_text, 'html.parser')

        roots = soup.find('div', class_='main_detail').find('ul', class_='list_netizen').find_all('div', class_='review_info')
        for root in roots:
            netizen = root.em.string
            score = root.find('em', class_='emph_grade').string
            comment = root.find('p', class_='desc_review').text.strip()
            result_list.append([str(netizen), int(score), str(comment)])

    pprint(result_list)

    return result_list

# strange = doctor_strange_daum_movie_netizen(pages=20)
# score_average = sum(list[1] for list in strange) / len(strange)
# print(score_average)

"""
This function needs emprovements. Actually, the nice version would be
including movie name as input and make results.
But I don't know why but daum changes movie names into id so I couldn't make query
for the results. SO the result is only for Doctor Strange. I will find another way.. Sorry.
"""