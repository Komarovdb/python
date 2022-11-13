# # lst = [0, 1, 2, 3]
# # for k in lst: #пробежка по всем элементам списка
# # for zabivnoy_anton in lst:
# #     print(zabivnoy_anton)
# # for zabivnoy_anton in range(0, 10 + 1):
# #     print(zabivnoy_anton)
# x1=int(input( ))
# x2=int(input( ))
# # while x1 <= x2:
# #     print(x1, end=" zabiv")
# #     x1 += 1
# for zhoskiy_i_rickoviy_anton in range(x1, x2 + 1):
#     print(zhoskiy_i_rickoviy_anton)

num = int(input("Ярусов: "))
while True:
    symbol = input("Символ: ")
    if len (symbol.strip()) == 1:
        break
    else:
        print("one symbol")
for movavi in range(1, num + 1):
    print(" " * (num-movavi), end="")
    print(movavi * symbol, end="")
    print (movavi * symbol)

