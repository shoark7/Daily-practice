class man(object):
    def __init__(self, sex='m', age='Unknown'):
        self.sex = sex
        self.age = age

    def __str__(self):
        return '인간은 인간입니다. 인간의 존엄성에 도전하다니... 훗... 결계인가?'


k = man(sex='m', age=24)
print(k)


