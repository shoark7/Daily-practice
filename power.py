import sys
import warnings
# print(sys.argv[0])


# class Calendar:
#    def __init__(self, year, month):
#        self.year=year;
#        self.month=month;
#        self.days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
#
#    def calcDay(self):
#        day=(self.year-1)*365;
#        lunarCnt=0;
#        days=self.days;
#        sumMonth=0;
#
#        for i in range(1, self.year):
#            res=self.lunar(i);
#            if res == True:
#                lunarCnt+=1;
#            else:
#                pass;
#        day=day+lunarCnt;
#
#        yearChk=self.lunar(self.year);
#
#        if yearChk is True:
#            days[1]=29;
#        else:
#            pass;
#
#        for i in range(1, self.month+1):
#            sumMonth+=days[i];
#
#        print(day+sumMonth);
#
#    def calcWeek(self):
#        pass;
#
#    def lunar(self, month):
#        res=True;
#        if (month%4==0) and (month%100!=0) or (month%400==0):
#            res=True;
#        else:
#            res=False;
#
#        return res;
#
#
# K = Calendar(2016, 12)
# K.calcDay()
