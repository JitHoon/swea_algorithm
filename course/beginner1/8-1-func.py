def outer_func():
    id = 0

    def inner_func():
        nonlocal id
        id += 1
        return id

    return inner_func


result = outer_func()

print("{0}".format(result))  # 출력값 없음

print("{0}".format(result()))  # 1
print("{0}".format(result()))  # 2
print("{0}".format(result()))  # 3

print(dir())
