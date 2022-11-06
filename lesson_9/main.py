# import random as r
# import time as t
# print("го в русскую рулетку")
# game="y"
# t.sleep(0.5)
# print("*заряжаем револьвер*")
# t.sleep(2.5)
# print("*раскручиваем барабан*")
# t.sleep(1.5)
# print(3)
# t.sleep(1)
# print(2)
# t.sleep(1)
# print(1)
# t.sleep(1)
# print("*выстрел*")
# slots=[1, 2, 3, 4, 5, 6]
# patron=r.choice(slots)
# our=r.choice(slots)
# if patron==our:
#     game="n"
#     print("смэрт")
# else:
#     print("норм")
#     x=input("Играем дальше?")
#     if x == "n":
#         game="n"

# lst=["Антон1, Антон2, Антон3, Антон4"]
# for antoha in lst:
#     print(antoha, end="*")
# print()
# for i in range(0, 10):
#     print("пон")

# word = input("Введи слово: ")
# while word:
#     print(word)
#     word = word[:-1]
# x = int(input("введити число: "))
# while x:
#     x -= 1
#     if x % 2==0:
#         print(x, end=" ")
x = int(input())
step=0
while x != 1:
    step += 1
    if x % 2 == 0:
        print(f"{step}", end=" ")
        print(x, "* 3 + 1 =", end=" ")
        x = x // 2
    else:
        print(f"{step}", end=" ")
        print(x, " / 2 =", end=" ")
        x = 3 * x +1
print(x)