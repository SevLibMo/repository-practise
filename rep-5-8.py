lvl = int(input("Ваш уровень: "))
hp = int(input("Ваше здоровье: "))
if lvl < 5 and lvl >= 1:
    print("Ваш уровень слишком низкий для выполнения миссии.")
elif lvl >= 5 and hp >=50  and hp <= 100:
    print("Вы готовы к миссии!")
elif lvl >= 5 and hp >= 20 and hp < 50:
    print("Ваше здоровье низкое, будьте осторожны.")
elif lvl >=5 and hp < 20 and hp >= 1:
    print("Ваше здоровье слишком низкое для выполнения миссии.")
else:
    print("Некорректные данные.")