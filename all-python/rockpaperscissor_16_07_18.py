""" 가위 바위보 프로그램입니다. 컴퓨터와 대결을 시작합니다. 3연승시 성공입니다."""
""" 16년 7월 18일날 제작을 시작했습니다. """
""" 그리고 동일 완성했습니다. """
import random
import time

print("알파고와 가위바위보를 대결합니다. 3연승시 성공입니다!\n")

winStreak = 0
combination = ["가위", '바위','보']
times = 1 # 몇 번만에 이겼는지 승리 후에 알려줌. 친구와 경쟁할 수 있음.

while winStreak != 3:
	computerChoice = random.choice(combination)
	userChoice = input("가위, 바위, 보 중에 하나를 정확히 입력해주세요 : ")
	while userChoice not in combination:
		userChoice = input("  정확히 입력해주세요. 사람 맞죠? : ")

		# 비겼다면? 다시 입력받음. 승패에 영향을 안 끼침
	while userChoice == computerChoice:
		userChoice = ""
		computerChoice = random.choice(combination)
		userChoice = input("비겼습니다. 다시 입력해주세요 : ")
		while userChoice not in combination:
			userChoice = input("  정확히 입력해주세요. 이러기에요? : ")

		# 사람이 이겼을 시.
	if (userChoice == "가위" and computerChoice == '보') or \
	(userChoice == '바위' and computerChoice == '가위') or \
	(userChoice == '보' and computerChoice == '바위'):
		winStreak += 1
		print("인간 {0}, 알파고 {1}. 인간 {2}\n".format(userChoice, computerChoice, "승리" if winStreak == 1 else str(winStreak)+"연승"))
		
		# 컴퓨터 승리시
	else:
		print("인간 {0}, 알파고 {1}. 컴퓨터 승리\n".format(userChoice, computerChoice))
		times += 1
		winStreak = 0

# 3연승으로 빠져 나옴.
# for i in range(1,11):
# 	print('*' * i * 2)
# 	time.sleep(0.3)
for c in "경축! 인간이 알파고를 박살내고 승리하였습니다.\n 기계 따위는 인간의 상대가 되지 않습니다.\n 총 {}번만의 시도로 성공했습니다.".format(times):
	print(c, end="")
	time.sleep(0.1)
# print()
# for i in range(1,11):
# 	print('*' * (11 - i) * 2)
# 	time.sleep(0.3)


		





