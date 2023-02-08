print("원하는 리스트 인덱스 입력받기 with. 예외처리")


def value_err_func():
    try:
        index_input = int(input("인덱스를 입력하세요: "))
    except ValueError as exception:
        raise exception
    else:
        return index_input


def index_err_func(l, i):
    try:
        result = l[i]
    except IndexError as ie:
        i = len(l)-1
        result = l[i]
        return i, result
    else:
        return result
    finally:
        print("list[{0}]: {1}".format(i, result))


L = list(range(0, 11))
try:
    index = value_err_func()
    index_err_func(L, index)
except ValueError as ve:
    print("입력 값은 반드시 숫자를 사용해야 합니다.")
    print("{0}: {1}".format(type(ve), ve))
except IndexError as ve:
    print("사용 가능한 index 범위는 0 ~ {1} 입니다.".format(index_err_func[0]))
except Exception as ex:
    print("예상치 못한 예외가 발생했습니다.")
    print("{0}: {1}".format(type(ex), ex))
