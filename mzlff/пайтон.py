# adolf = open("нокия2004.txt", "w")
# adolf.write("nerpi vse")
# adolf.write("nerpi vse\n")
# shaltay_boltay = adolf.read()
# print(shaltay_boltay)
# adolf.close()

# adolf = open("нокия2004.txt", "r", encoding="utf-8")
# mazelov = adolf.readlines()
# print(mazelov)
# for kareyka in mazelov:
#     print(kareyka.rstrip())
# adolf.close()

# x = input("write file name: ")
# m = x + ".txt"
# adolf = open(m, "w", encoding="utf-8")
# i = input("write random text: ")
# adolf.write(i)
# while adolf != "":
#     adolf.write(i + "\n")
#
#
#
#
# a = input("write file name: ")
# f = open(a, 'r')
# cont = f.readlines()
# v = len(cont)
# for i in range(v):
#     print((f"{i+1}"), cont[i].strip())

f = open("нокия2004.txt", "r",encoding="utf-8")
text = f.readlines()
f.close()
count = 0
print(text)
while text != []:
    el = text[:3]
    count += 1
    f = open(str(count) + ".txt", "w", encoding="utf-8")
    for i in el:
        f.write(i)
    f.close()
    print(text[:3])
    del text[:3]