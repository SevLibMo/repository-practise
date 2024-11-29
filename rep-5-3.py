print("Введите два числа:")
a = int(input("a = "))
b = int(input("b = "))
print("Выберите операцию(+, -, *, /)")
o = str(input())
if o == "+":
    print(a+b)
elif o == "-":
    print(a-b)
elif o == "*":
    print(a*b)
elif o == "/":
    print(a/b)
else:
    print("Неверная операция")

