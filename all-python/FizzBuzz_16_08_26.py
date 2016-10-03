# 유명한 FizzBuzz 문제를 풀어봅니다.
# 16년 8월 26일 날 시작했고 당일 날 완성했습니다.

# 1부터 100까지 시행함.
# for i in range(1,101):
#     if __name__ == '__main__':
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)


# 어느 고수의 코딩..
for i in range(1,101): print([i,'Fizz','Buzz','FizzBuzz'][(i% 3 == 0) + 2 * (i % 5 == 0)])
