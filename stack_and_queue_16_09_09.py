import datetime
import random

# 파이썬으로 간단히 나만의 스택과 큐를 구현해보도록 합니다.
# 오늘 날짜는 16년 9월 9일이며 당일 날 완성했습니다.


"""
1. Stack - 10개 까지만 받아들이고 그 이후에는 자료를 추가로 받지 않습니다.
pop, push 기능을 구현합니다.
정수만 받을 수 있습니다.
"""


#######################################
##########  1. stack 구현
#######################################


class myStack:

    @classmethod
    def sum(cls, a, b):
        return cls.rko

    def __init__(self):
        self.a = 3
        self.__stack = []
        self.__point_now = len(self.__stack)

    def push(self, number):
        if len(self.__stack) > 10:
            print("자료가 10개 꽉 찼습니다. 더 이상 들어가지 않습니다.")
            return
        elif not isinstance(number, int):
            print("정수만 받을 수 있습니다. 종료합니다.")
            return
        else:
            self.__stack.append(number)
            self.__point_now += 1

    def pop(self):
        if self.__point_now <= 0:
            return
        else:
            value = self.__stack[-1]
            del(self.__stack[-1])
            self.__point_now -= 1
            return value

    def __str__(self):
        return str(self.__stack)

#
# stack = myStack()
# # stack.b

# stack.push(3)
# print(stack.b)
# print(stack.c)
# for i in range(10):
#     stack.push(random.randint(1,10))
# #
# # for i in range(1,20):
# #     stack.pop()
#
#
# print(stack)



#######################################
##########  2. queue 구현
#######################################

class myQueue:
    def __init__(self):
        self.__queue = []
        self.__len = 0

    def put(self, number):
        if self.__len >= 10:
            print("10개 이상 출력할 수 없습니다.")
            return
        elif not isinstance(number, int):
            print("정수만 입력할 수 있습니다.")
        else:
            self.__queue.append(number)
            self.__len += 1

    def get(self):
        if self.__len <= 0:
            return
        else:
            value = self.__queue[0]
            self.__len -= 1
            del(self.__queue[0])
            return value

queue = myQueue()

for i in range(11):
    queue.put(random.randint(1,10))
for i in range(10):
    print(queue.get())
