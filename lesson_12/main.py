# a = int(input("a:"))
# b = int(input("b:"))
# lst = []
# for aaa in range(a + 1, b):
#     lst.append(aaa ** 2)
# print(lst)

# x=input("Ввод:")
# lst = x.split(" ")
# print(lst)
# lst.reverse()
# print(lst)

# num = ""
# chet= 0
# nech = 0
# lst = []
# while num != "end":
#     num = input("число: ")
#     if num.lstrip("-").isdigit():
#         num = int(num)
#         lst.append(num)
#     elif num == "end":
#         break
#     else:
#         print("сори, я не сказал, что нужно писать число")
#         continue
#     if num % 2 == 0:
#         chet += 1
#     else:
#         nech += 1
# print(lst)
# print(f"Чётных: {chet}")
# print(f"Нечётных: {nech}")

lst=[-10, 14, -69, -40, 0, -8, -23]
mini = min(lst)
maxi = max(lst)
lst[lst.index(mini)], lst[lst.index(maxi)] = lst[lst.index(maxi)], lst[lst.index(mini)]
print(lst)