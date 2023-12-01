def plus(a, b):
    return a + b
def minus(a, b):
        return a - b
def multiply(a, b):
        return a * b
def divid(a, b):
    if b==0:
        print("На 0 делить нельзя!")
    else:
        return a / b
print("Выберите функцию:")
print("1.Сложение")
print("2.Вычитание")
print("3.Умножение")
print("4.Деление")
a = input("Напишите номер выбранной функции (1/2/3/4):")
b = int(input("Введите число: "))
c = int(input("Введите число: "))
if a == '1':
    print(b, "+", c, "=", plus(b, c))
elif a == '2':
    print(b, "-", c, "=", minus(b, c))
elif a == '3':
    print(b, "*", c, "=", multiply(b, c))
elif a == '4':
    print(b, "/", c, "=", divid(b, c))
else:
    print("Ошибка! Попробйте ещё раз.")