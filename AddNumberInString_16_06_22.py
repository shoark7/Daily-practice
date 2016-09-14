import re
import string

""" 분석   """

# 이 프로그램은 예를 들어 'aqkgiqos'라는 문장이 있을 때 각 글자 사이에
# 그들의 유니코드 차이를 삽입하는 프로그램입니다. 왜 하는지는 모르겠는데
# 이런 문제를 어디서 봤습니다. 영어만 입력받고, 소대문자 모두 입력 가능합니다.
# 프로그램 제작 날짜는 6월 22일이고 완성 날짜는 """ """ 입니다.

""" 설계 """
"""
1. 문장을 입력 받는다. 소대문자 모두 가능하다.
 - 소대문자 모두 가능
 - 모든 공백제거(whitespace)

2. 문장의 모든 글자가 영어인지 검사한다.
    if : 다음 단계
    else : 다시
3. 그 차이 숫자의 절대값을 변수에 담아둔다.
4. 최종 정답을 담아둘 빈 문자열을 만들고 글자와 숫자를 하나씩 집어넣는다. yeah!

"""

# define a function which can trim the sentence
def sentence_trim(sentence):
    sentence = sentence.strip()
    sentence = sentence.replace(' ', '')
    return sentence



def add_number_into_string():
    ############
    ##### 1. Get an input sentence from the user.
    ############
    original_sentence = input("Give me any English sentence : ")
    refined_sentence = sentence_trim(original_sentence)


    ############
    ###### 2. Check if refined_sentence contains any none alphabetic words
    ############

        ### any, map, function is as same as in R.
    while any(map(lambda x: x.lower() not in string.ascii_lowercase, refined_sentence)):
        original_sentence = input("We don't accept any kind of special characters and numbers. Again : ")
        refined_sentence = sentence_trim(original_sentence)


    ############
    ###### 3. Make a list containing the absolute gap between two characters
    ############
    gap_list = []
    for i in range(len(refined_sentence) - 1):
        gap_list.append(
                    abs(
                        ord(refined_sentence[i]) - ord(refined_sentence[i+1])))

        #! ord function calculates a character's unicode in decimal points




    ############
    ##### 4. Make an empty string and append one of each lists' string turn by turn to it.
    ############

    result = ''

    for i,c in enumerate(refined_sentence):
        # if it's not the last element of the sentence
        if i != len(refined_sentence) - 1:
            result += c
            result += str(gap_list[i])
        else:
            result += c
    return result

print(add_number_into_string())
