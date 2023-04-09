# c1 = input()
# c2 = input()
# c = ("Red", "Yellow", "Blue")
# if c1 not in c or c2 not in c:
#     print("Wrong colour(s)")
# elif (c1 == c[0] and c2 == c[1]) or (c1  == c[1] and c2 == c[0]):
#     print("orange")
# elif (c1 == c[0] and c2 == c[2]) or (c1  == c[2] and c2 == c[0]):
#     print("purple")
# elif (c1 == c[2] and c2 == c[1]) or (c1  == c[1] and c2 == c[2]):
#     print("green")
# else:
#     print(c1.capitalize())
import time
# fl = input("start of the lessons(time) ")
# ll = int(input("how long is lesson "))
# bt = int(input("how long is break "))
# lc = int(input("lesson count "))
# hours, minutes = fl.split(":")
# hours,minutes = int(hours), int(minutes)
# time = hours*60 + minutes
# for i in range(lc):
#     print(f"{i+1} урок:", end='')
#     print(f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')} - ", end = "")
#     time += ll
#     hours = time // 60
#     minutes = time % 60
#     print(f"{str(hours).rjust(2,'0')}:{str(minutes).rjust(2, '0')}")
#     time +=10
#     hours = time // 60
#     hours = time % 60


cz = int(input("Кол-во зомби к началу пандемии:"))
vz = int(input("Максимальне возможное количество:"))
day = int(input("На какой день делается расчёт:"))
print(f"Первый день: {cz}")
for i in range(2, day+1):
    o = cz*vz+cz
    cz=o
    print(f"{i} день:{cz}")
