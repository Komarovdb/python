
# f = open("file.json", "w", encoding="utf-8")
# f = open("file.txt","w")
# f.write("true")
# var = [1, 12.6, "tun", #
# # try:
# #     f = open("filt.txt", "r", encoding="utf-8")
# # except FileNotFoundError:
# #     print("error")
# # txt = f.readlines()
# # print(f"Строк: {len(txt)}")
# # ft = " ".join(txt).replace("\n", "")
# # print(ft)
# # words = ft.split()
# # print(f"Слов: {len(words)}")
# # s = ft.replace(" ","")
# # print(f"Символов: {len(s)}")
# #
# # word = input()
# # try:
# #     f = open("filt.txt", "r", encoding="utf-8")
# # except FileNotFoundError:
# #     print("error")
# # text = f.read()
# #
# #
#
# # try:
# #     f = open("filt.txt", "r", encoding="utf-8")
# # except FileNotFoundError:
# #     print("error")
# #
# # try:
# #     number = int(input())
# #     print(12/number)
# # except ValueError:
# #     print("Ы")
# # except ZeroDivisionError:
# #     print("ЫЫ")
# # else:
# #     print("ЫЫЫ")
# # finally:
# #     print("ЫЫЫЫ")
# # f = open("kniga.json","w")
# # f.write("true")
# # f.close()
# importTrue, "обед"]
# json.dump(var, f, ensure_ascii=False)
# f.close()
#
#
# f = open("file.json", "r", encoding="utf-8")
# cont = json.load(f)
# print(cont)
# f.close()
import json
# s = open("file.txt", "r", encoding="utf-8")
# u = s.readlines()
# spic = {}
# print(u)
# for i in u:
#     p = i.split(": ")
#     print(p)
#     spic[p[0]] = p[1].rstrip()
# print(spic)
# o = open("file.json", "w", encoding="utf-8")
# json.dump(spic, o, ensure_ascii=False)

f = open("file.json", "r")
sod = json.load(f)
f.close()
print(sod)
for indx, elem in enumerate(sod):
    if type(elem) == str:
       sod[indx] += "!"
    elif type(elem) in (int, float):
       sod[indx] += 1
    elif type(elem) == bool:
       sod[indx] = not elem
    elif type(elem) == list:
       sod[indx] += elem
    elif type(elem) == dict:
        sod[indx]["newkey"] = None
print(sod)