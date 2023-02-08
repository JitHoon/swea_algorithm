class Student:
    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    # 대부분의 객체를 출력할 때 많이 사용하는 함수 (객체의 표현을 지원)
    def __repr__(self):
        return "{0}(name: {1}, gender: {2}, height: {3})"\
            .format(self.__class__.__name__, self.name, self.gender, self.height)


s1 = Student("홍길동", "남", 155.5)

# __repr__() 을 통해 객체 출력
# __str__() 과 결과값 동일
print(s1)

students = [
    Student("최영인", "남", 170.5),
    Student("김용남", "여", 160.5),
    Student("최지선", "여", 160.5),
    Student("최지훈", "남", 174.5)
]

for student in students:
    print(student)

print("name 기준으로 오름차순 정렬")
for student in sorted(students, key=lambda x: x.name, reverse=False):
    print(student)


print("name 기준으로 내림차순 정렬")
for student in sorted(students, key=lambda x: x.name, reverse=True):
    print(student)

print("height 기준으로 오름차순 정렬")
for student in sorted(students, key=lambda x: x.height, reverse=False):
    print(student)

print("name 기준으로 내림차순 정렬")
for student in sorted(students, key=lambda x: x.height, reverse=True):
    print(student)
