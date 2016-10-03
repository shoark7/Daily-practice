
# 이 파일은 입력 받은 두 수가 서로소(coprime)인지 검증합니다.
# 16년 8월 26일 날 시작하여 당일 날 완성했습니다.

"""
1. 두 수를 입력 받는다.
2. 입력 받은 수를 검증받는다.
    2.1 받은 값이 2개뿐인지 검증한다.
    2.2 받은 값이 모두 정수인지 검증한다.
3. 검증 후 값을 반환한다.
    3.1 서로소면 True
    3.2 아니면 False
"""

from random import randint
def is_coprime(*two_value):

    if len(two_value ) != 2 or any(map(lambda x: x != int(x), two_value )):
        print("No correct input. Bye")
        return False
    else:
        first_value = two_value[0]
        second_value = two_value[1]

        for i in range(2, min(two_value) + 1):    while True:
        a, b = randint(2, 10), randint(2,10) # 두 개의 랜덤 정수 각각 할당
        if a == b: continue
        break

            if first_value % i == 0 and second_value % i == 0:
                return False

        return True



# 올바른 값을 출력하는지 10번 정도 검증

for i in range(10):

    if is_coprime(a,b):
        print('{:4d}, {:4d} are coprime'.format(a,b))
    else:
        print('{:4d}, {:4d} are not'.format(a,b))

