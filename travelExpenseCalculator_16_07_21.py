# 2016년 7월 9일 ~ 8월 12일까지의 인도여행에서 영감을 받았습니다.
# 여행시 밥값, 숙소값 등을 공평하게 n분의 1하기 위해 이 프로그램을 만들었습니다.
# 시작한 날짜는 16년 7월 21일입니다.
# 그리고 완성한 날짜는 16년 8월 11일입니다.

import datetime as dt
import string
import re
today = dt.datetime.today()

print(" 즐거운 여행되고 계신지요? 여행 비용 계산기 기능입니다.")
print(" 날짜 및 시간 {}년 {}월 {}일 {}시 {}분입니다."\
	.format(today.year, today.month, today.day, today.hour, today.minute))


""" Step 1. 사람 수 입력 단계 """
permitToNext = False
while permitToNext == False:
	try:
		people = re.split('\t| ',input(' 비용을 계산할 사람들의 이름을 공백을 기준으로 적어주세요 : '))
	except SyntaxError:
		while type(people) != type([]):
			people = re.split('\t| ',input('공백을 기준으로 정확히 적어주세요... : '))
			continue
	
	if len(people) <= 1:
		print("최소 두 명 이상 있어야 가능합니다. 다시 입력해주세요...\n")
		continue
		

	print("\n계산에 참여하는 분은 \n", )
	for i, p in enumerate(people):
		if i != len(people) - 1:
			print('\t'+str(i+1)+'.', p, end=', ')
		else:
			print('\t'+str(i+1)+'.', p,' 총 {}분입니다. 맞습니까?\n'.format(len(people)))

	ok = input("맞으면 y, 틀리면 n을 입력하세요 : ")
	while ok not in 'YynNㅇ':
		ok = input("정확히 입력해주세요 : ")
	
	if ok.upper() == 'Y' or ok == 'ㅇ':
		print("감사합니다. 한 분씩 내역과 비용을 입력하겠습니다.\n")
		permitToNext = True
	else:
		print("그렇다면 다시 입력하겠습니다.\n")


""" Step 2. 각자의 사용금액 입력 단계 """
# 택시 비용, 밥값 등 모두를 위해 사용한 금액을 입력하는 단계.
# 사용 내역은 Usage, 금액은 expense라고 정의합니다.
print("내역과 비용을 차례로 계속 입력하시면 됩니다. \n\
'끝'이라고 입력하시거나 비용을 아무것도 입력 안 하시면 자동으로 입력이 끝납니다.\n")
# eachUsageExpense = [{}] * len(people)
eachUsageExpense = []
for i in range(len(people)):
	eachUsageExpense.append({})

for i, person in enumerate(people): # 한 사람당 입력을 위해 for문을 돌린다.
	print('{}{}의 입력을 받겠습니다. 내역와 비용을 TAB으로 구분해서 적어주세요.\n\
기억이 안 나시면 비용만 적으셔도 됩니다. 비용은 숫자만 받습니다.\n'.format('먼저 ' if i == 0 else '', person))
	
	usage = 0
	tmp = '123'
	
	while True:
		
		tmp = input('  내역 & 금액 >>>> ')
		if len(tmp.split('\t')) == 1 and tmp.isnumeric():
			
			expense = int(tmp)
			eachUsageExpense[i][usage] = int(expense)
			usage += 1
			
		elif len(tmp.split('\t')) == 2 and tmp.split('\t')[1].isnumeric():
			usage = tmp.split('\t')[0]
			expense = int(tmp.split('\t')[1])
			eachUsageExpense[i][usage] = expense

		elif tmp == '' or tmp == '끝':
			print('{}의 입력이 끝났습니다.'.format(person))
			print('-' * 60)
			break
		else:
			print("정확한 형식을 지켜서 입력해주세요.")
			continue

		
print(eachUsageExpense)

""" Step 3. 화면 출력 및 합계 계산 단계 """

# 화면에 결과를 모두 출력하고 싶었지만... 지금 당장은 계산만 하겠습니다.

# print('ㅡ'* round(34 / 3) * len(eachUsageExpense))
# print('|', end="")
# for person in people:
# 	print('{:20s}|'.format(person), end="")
# print()
# print('ㅡ'* round(34 / 3) * len(eachUsageExpense))

# maxLength = 0
# for value in eachUsageExpense:
# 	maxLength = max(maxLength, len(value))


# for i in range(maxLength):
# 	print('|', end="")
# 	for record in eachUsageExpense:
# 		keySet = list(record.keys())
# 		try:
# 			print('{:10}{:10}|'.format(keySet[i] if len(keySet[i]) <=5 else keySet[i][:5] + '...',\
# 			record[keySet[i]]), end="")
# 		except IndexError:
# 			print('{:10}{:10}|'.format('',''), end="")
# 	print()
# print('ㅡ'* round(40 / 3) * len(eachUsageExpense))

eachUsageSum = []
howMany = len(people)
maxLength = max(map(len, people))

for i, person in enumerate(people):
	eachUsageSum.append(sum(eachUsageExpense[i].values()))
	print('{:5}의 총 사용금액은 {}원입니다.'.format(person, eachUsageSum[i]))





