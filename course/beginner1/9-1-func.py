# globals(), locals()
class MyClass:
    pass


def test_fn(param):
    def inner_fn():
        pass
    val1 = 5
    val2 = 8
    for item in locals().items():
        print("{0} : {1}".format(item[0], item[1]))


value1 = 10
value1 = 20
obj1 = MyClass()

print("globals()")
for item in dict(globals()).items():
    print("{0}, {1}".format(item[0], item[1]))

print("locals()")
test_fn(10)
