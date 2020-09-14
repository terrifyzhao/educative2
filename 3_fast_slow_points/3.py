def find_happy_number(num):
    a = operate(num)
    b = operate(operate(num))
    while 1:
        a = operate(a)
        b = operate(operate(b))
        if a == 1:
            return True
        elif a == b:
            return False


def operate(num):
    res = 0
    while num:
        a = num % 10
        res += a * a
        num = int(num / 10)
    return res


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
