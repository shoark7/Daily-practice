# 본 함수는 숫자를 입력 받고 그 개수만큼 소수를 만들어 출력하는 기능입니다.
# 제너레이터를 실험해볼 계획이고, 동시에 is_prime 헬퍼 함수를 만들어 사용해보겠습니다.
# 시작 날짜는 16년 9월 1일이고 당일 날 완성했습니다.

def prime_maker(number):
    """주어진 개수만큼 소수를 만들겠습니다."""
    if number < 1 or not isinstance(number, int) :
        raise ValueError('Input number must be type integer and greater than 1')

    def is_prime(n):
        prime = True
        if not isinstance(n, int) or n < 2:
            raise ValueError("It can't be prime number. Try once.")
        if n == 2 or n == 3:
            return prime
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                prime = False
                break
        return prime

    count = 0
    now_number = 2
    while True:
        if is_prime(now_number):
            yield now_number
            count += 1

        now_number += 1
        if count == number:
            break


k = prime_maker(500)
try:
    while True:
        print(next(k))
except:
    pass


