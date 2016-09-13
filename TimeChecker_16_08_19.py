import datetime
import time
import sys
# 이 프로그램은 1/100분 단위로 시간이 재져서 화면에 출력하게 하는 기능을 포함하고 있습니다.
# 8월 19일 날 제작을 시작하여 당일 완성하였습니다.

class Timer:

	def __init__(self):
		self._hour = 0
		self._minute = 0
		self._second = 0
		self._hundi_second = 0


	def run(self):
		while self._hour < 3:
			the_time = "{:02d}:{:02d}:{:02d}.{:02d}".format(self._hour, self._minute, self._second, self._hundi_second)
			print(the_time+'\r', end="", flush=True)

			self._hundi_second += 1

			if self._hundi_second == 100:
				self._second += 1
				self._hundi_second ^= self._hundi_second
			if self._second == 60:
				self._minute += 1
				self._second ^= self._second
			if self._minute == 60:
				self._hour += 1
				self._minute ^= self._minute
			
			time.sleep(0.01)

		print("3시간이 되어 프로그램을 종료합니다. 감사합니다.")

if __name__ == "__main__":
	new = Timer()
	new.run()
