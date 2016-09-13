import string
import random
# 여러 실험에서 쓰일 랜덤 문자열 생성함수를 만듭니다.
# 문자열은 최소 2글자, 최대 10글자 사이까지 만들어질 수 있고, 영어, 숫자로만 구성되어집니다.
# 당일 날 완성했습니다.

def random_string_maker():
    english_and_numbers = string.ascii_letters + string.digits
    string_length = random.randint(2,10)
    result = ""

    for i in range(string_length):
        result += random.choice(english_and_numbers)
        if i == string_length - 1 and result.isnumeric():
            random_string_maker()

    return result

# test
# if __name__ == '__main__':
#     for i in range(10):
#         print('{0:02d} '.format(i+1) + '/ 10, '+random_string_maker())


# 다음은 실험을 위해 1부터 10까지의 정수를 키로 하고, 랜덤문자열을 밸류로 하는 사전을 만든다
int_string_dict= {}
for i in range(1,11):
    int_string_dict[i] = random_string_maker()

# int_string_dict는 문자열을 밸류로 받고 있습니다.
# 그것을 뒤틀어서 밸류를 그 밸류의 길이로 바꾸겠습니다.
# dict comprehension을 통해서 말입니다.

int_length_dict = {}
int_length_dict = {int:len(string) for int, string in int_string_dict.items()}

# 완성되었습니다. 결과를 확인해보겠습니다.
for key, value in int_length_dict.items():
    print('key : {0:2d}, length of original value : {1}'.format(key, value))
