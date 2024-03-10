def f(n):
    try:
        100 / int(n)
        int(n)
    except ValueError:
        print("Неверный ввод")
    except ArithmeticError:
        print("Ошибка ввода числа")
    else:
        print("=",100/int(n))

n=input("100 : ")
f(n)