# simple_calculator.py
import time
import sys
import datetime

"""
	매우 간단한 계산기를 만든다.
"""
sum_method = [lambda arg: sum(arg), # 덧셈 기능. 0 번째.
    lambda arg: sum( [ n ** 2 for n in arg]), # 제곱 덧셈 1번째 
    lambda arg: sum( [abs(n) for n in arg])] # 절대값 곱셈 2번째

print("현재 시각", datetime.datetime.now(),"반갑습니다.")
print("""간단한 계산기입니다. 여러 가지의 덧셈기능을 제공합니다.
	무엇을 원하시나요?
	  1. 단순 합
	  2. 제곱의 합
	  3. 절대값의 값
	  4. 종료.
	""")

while True:
	desired_menu = 0
	method = 0
	result = 0
	


# 여기서는 3가지의 함수를 지원하며 사용자가 원하는 기능을 사용할 수 있다.
# 사용자가 원하는 기능을 받는다.

	while desired_menu not in ["1","2","3","4"]:
		desired_menu = input("원하시는 메뉴를 선택하세요 : ")

		if(desired_menu == "1"):
			method = sum_method[0]
		elif(desired_menu == "2"):
			method = sum_method[1]
		elif(desired_menu == "3"):
			method = sum_method[2]
		elif(desired_menu == "4"):
			print("시스템을 종료합니다.")
			time.sleep(2)
			sys.exit()
		else:
			print("없는 기능입니다. 다시 입력하셔야 돼요.")


#원하는 기능을 받았다면 이번에는 배열값을 받는다. ',' 로 구분하게 하여 각 단위가 모두 숫자인지 판별한다.

	while True:
		numbers = input("원하시는 숫자들을 입력하세요. 숫자는 ','를 기준으로 입력해주시면 됩니다. ")
		numbers = numbers.split(',')
		if not any(map(str.isnumeric, numbers)):
			print("숫자만 입력하셔야 합니다. 다시 입력하세요.")
		else:
			numbers = [float(n) for n in numbers]
			break

	result = method(numbers)
	print("원하시는 결과는 {0}입니다.".format(result))
	print("=" * 40)
	print()


















