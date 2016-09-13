"""
	json.load()의 성능을 시험해보도록 한다.
"""
import json
import datetime

data = []
i = 1

with open('daily_money_expenditure.txt', 'r', encoding='utf-8') as output:
	for line in output:
		data.append(json.loads(line))
		print("%d번째 성공입니다." % i)
		i += 1
print(data)


k = input("어떡할까요??")


