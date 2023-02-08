# map(), filter(), eval()
l = list(range(1, 11))
oper = input("원하는 연산식을 입력하세요: ")
con = input("원하는 조건식을 입력하세요: ")

map_result = list(map(lambda x: eval(oper), l))

filter_result = list(filter(lambda x: eval(con), map_result))

print(filter_result)  # [6, 9, 12, 15]

# eval
a = "2*3"
b = "'hello, python!'.upper()"

print(eval(a))
print(eval(b))
