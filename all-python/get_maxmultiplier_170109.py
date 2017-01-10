"""
It's from 'http://euler.synap.co.kr/prob_detail.php?id=8'

From an 1000-digit number,
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 =
5832.

we get the largest product in five adjacent digits.

I used two ways.
    1. class way
    2. funciton way

What would be better? Check and see.

Start date : 2016/01/09
End date: 2016/01/10

"""


TEST_SET = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace('\n', '')

from functools import reduce


##### 1. First way #####

class myqueue:
    def __init__(self, init_value):
        self.init_value = init_value
        self.the_list = []

    def pop_and_push(self, value):
        self.the_list.pop(0)
        self.the_list.append(value)

    def get_multiplier(self):
        return reduce(lambda x, y: int(x) * int(y), self.the_list)

    def get_max_multiplier(self, length=5):
        loop_range = len(self.init_value)

        for i in range(length):
            self.the_list.append(int(self.init_value[i]))

        start = length
        max_result = self.get_multiplier()

        while start < loop_range:
            self.pop_and_push(self.init_value[start])
            if self.get_multiplier() > max_result:
                max_result = self.get_multiplier()
            start += 1

        return max_result


####### 2. second way #########
def get_max_multiplier(wanted, length=5):
    max_value = 0

    for i in range(len(wanted) - length + 1):
        current_string = wanted[i:i+length]
        current_multi = int(reduce(lambda x, y: str(int(x) * int(y)), current_string))
        
        if current_multi > max_value:
            max_value = current_multi
    return max_value

print(get_max_multiplier(TEST_SET))

"""
Second is much better and concise.
In first way, I used 'class' mechanism but it's not that readable and efficient.
Now I found my way.
"""
