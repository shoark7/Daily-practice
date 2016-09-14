import datetime
import time

# 연도와 월을 입력 받으면 그 달의 달력을 간단하게 출력하는 프로그램입니다.
# 16년 9월 12일에 시작해 당일 날 완성했습니다.

def weekday_finder(weekday):
    return ['월','화','수','목','금','토','일'][weekday]



class Calendar(object):
    """초기화시 연도와 월을 입력 받는다. 그 달의 달력을 출력한다.
        단 커맨드 창에서 일|월|화|수|목|금|토 와 같은 형식이 되도록 한다."""

    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.day_of_month = [31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    def show_graph(self):

        print('   월   화   수   목   금   토   일')
        for d in range(1, self.day_of_month[self.month - 1]+1):
            day_of_month = datetime.date(self.year, self.month, d).weekday()
            weekday = weekday_finder(day_of_month)
            if d == 1:
                print('    ' * (day_of_month+1)+'{:2d}'.format(d), end='')
            else:
                print(' '*3 + '{:2d}'.format(d), end="")

            if day_of_month == 6:
                print()




cal = Calendar(2016,9)
cal.show_graph()
