#МНОЖЕСТВА:
# d1 = {"anton","anton", False,}
# d1.add(5)
# print(d1)
# x = set()
#СЛОВАРИ:
# anton = ""
# d = {}
# d={anton: 1
# }
# print(d)
# m = dict()

# phrase =(input("text:")).lower()
# ne_dolche_milk=list(".,?!/=+-{}[]()*^':;")
# for eee in phrase:
#     if eee not in ne_dolche_milk:
#         anton += eee
# l = anton.split(" ")
# for discord in l:
#     if discord not in d:
#         d[discord]=1
#     else:
#         d[discord] += 1
# print(d)
# s = 0
# d = {"Хлеб": 250,
#       "Дольче милк": 280,
#       "Сырок": 30,
#       "Ёлка": 50,
#       }
# #for price in d: #перебор по ключем
# for price in d.values(): #и по ключам
#    s += price
# print(s)

# hog_rider = max(d.values())
# for (key, values) in d.items():
#     if values == hog_rider:
#        print(f"kluch:{key},znachenie:{values}")

delusion = {
    3:2,
    9:2,
    1:2,
    "KEY1":2,
    False:2,
    "eee":3,}
delusion["eee"], delusion[3] = delusion[3], delusion["eee"]
