p = int(input("Сумма покупки:"))
if p < 1000:
    print("Скидка не предоставляется")
if p >= 1000 and p < 5000:
    print("Скидка 5%")
if p >= 5000:
    print("Скидка 10%")