class Person:
    def __init__(self):
        print('Person__init__')
        self.hello = '안녕하세요'

class Student(Person):
    def __init__(self):
        print('Student__init__')
        super().__init__()            # super()로 기반 클래스의 __init__메서드 호출
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)
