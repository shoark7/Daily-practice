import system
""" sorted와 list.sort()의 key를 연습하기 위해 만들었습니다. """
""" 16년 8월 30일 날 시작해서 당일 완성했습니다. """



def sort_key(values, group):
    def helper(x):
        if x in group:
            return False
        return True
    # values.sort(key=helper)
    sorted(values, key=helper)


numbers = [8,5,1,2,6,2,4,8,9]
group= {6,8,9}

sort_key(numbers, group)
print(numbers)
# print(sorted(numbers, key=lambda x: x >= 6, reverse = True))
