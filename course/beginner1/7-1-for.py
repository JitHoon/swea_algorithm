dogs = {1: '골든리트리버', 2: '진돗개', 3: '보더콜리'}

# 사전 객체 사용 -> 항목의 키 정보 1, 2, 3이 차례로 대입
for key in dogs:
    print("{0}: {1}".format(key, dogs[key]))

# <class ‘dict_items’> 객체 객체 사용
for key, value in dogs.items():
    print("{0}: {1}".format(key, value))

# range(10, -1, -2)
print(range(10, -1, -2))

# 문자열 객체 사용
str = "최지훈"

for c in str:
    print("{0}".format(c))

# 리스트 객체 사용
scores = [100, 95, 88, 98]
total = 0

for score in scores:
    total += score

print("총점: {0}".format(total))

# 이중 for문, 구구단 for문
dan = range(2, 10)
num = range(1, 10)

for i in dan:
    for j in num:
        print("{0} * {1} = {2}".format(i, j, i*j))
    print()

# 구구단 while
i = int(input("단을 입력하세요:"))
j = 1

while j < 10:
    print("{0} * {1} = {2}".format(i, j, i*j))
    j += 1

# 총점 while문 with list
scores = [100, 95, 88, 98]
i = 0
score = 0

while i < len(scores):
    score += scores[i]
    i += 1
print("총점: %d" % score)

# for 문 + continue, break
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for n in numlist:
    if n % 3 == 0:
        continue
    total += n

print("for문 정답: {0}".format(total))

# while 문 + continue, break
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

i = 0

while i < 10:
    if numlist[i] % 3 == 0:
        i += 1
        continue
    total += numlist[i]
    i += 1

print("while문 정답: {0}".format(total))

# 별 트리 실습 1
for i in range(1, 7):
    print("{0}".format("*"*i))

# 별 트리 실습 2
star = "*"

for i in range(1, 7):
    print("{0:^11}".format(star))
    star += "**"
