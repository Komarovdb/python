# month = input("введите номер месяца: ")
# if month.isdigit() and 1 <= int(month) <= 12:
#     month = int(month)
#     if 3 <= month <= 5:
#         print("весна")
#     elif 6 <= month <= 8:
#         print("лето")
#     elif 9 <= month <= 11:
#         print("осень")
#     else:
#         print("зима")
# else:
#     print("неправильно")
#
#
# h = int(input("часы:"))
# m = int(input("минуты:"))
# s = int(input("секунды"))
# if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
#     print("формат правильный")
#     print(f"{h}:{m}:{s}")
# else:
#     print("ошибка")
#     if h > 23 or h < 0:
#         print("часы в формате 0-23")
#     if m > 59 or m < 0:
#         print("минуты в формате 0-59")
#     if s > 59 or s < 0:
#         print("секунды в формате 0-59")
q1 = input("Какого цвета трава?\n"
           "а)пон б)мандарин в) геншен г) цвет шрека\n")
score = 0
if q1 == "г":
    score = score + 10
    print("yes")
else:
    print("no")
    print(score)
