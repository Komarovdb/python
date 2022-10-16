# x = 7
# if x == 10:
#     print("я сработал")
# else:
#     print("я тож сработал")
# phrase = "i am a map"
# if phrase == "i am a map":
#     print(12)
# game = "dota2"
# if game != "genshin impact":
#     print("можно и поиграть")
# if x <= 10 and x == 7 or x == 2:
#     print(456)
# else:
#     print(123)
# number = int(input("input:"))
# if number > 0:
#     print("+")
# elif number == 0:
#     print(0)
# else:
#     print("-")
# year = int(input("input:"))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print("високосно")
# else:
#     print("no")
#number_1 = int(input("input.1:"))
#operation = input("input.sign:").strip()
#number_2 = int(input("input.2:"))
#lis=["-","=","/","*"]
#if operation in lis:
   # if operation=="-":
    #   print(number_1 - number_2)
   # elif operation=="+":
 #      print(number_1 + number_2)
  #  elif operation=="/":
#       print(number_1 / number_2)
   # else:
    #    print(number_1 * number_2)
# num1 = int(input("input.1:"))
# num2 = int(input("input.2:"))
# num3 = int(input("input.3:"))
# countpol=0
# countotr=0
# if num1 < 0:
#     countotr += 1
# else:
#     countpol += 1
# if num2 < 0:
#     countotr += 1
# else:
#     countpol += 1
# if num3 < 0:
#     countotr += 1
# else:
#     countpol += 1
# print("+",countpol)
# print("-",countotr)
num1 = int(input("input.1:"))
num2 = int(input("input.2:"))
num3 = int(input("input.3:"))
lst=[num1,num2,num3]
mini = min(lst)
maxi = max(lst)
print("max:",maxi,"min:",mini)
ticket=input("input ticket num(6 nums):")
if len(ticket)==6:
    firsthalf = ticket[:3]
    lasthalf = ticket[-3:]
    firstsum=firsthalf[0]+firsthalf[1]+firsthalf[2]
    lastsum=lasthalf[0]+lasthalf[1]+lasthalf[2]
    if firstsum == lastsum:
         print("rare ticket")
    else:
         print("common ticket")
else:
    print("wrong ticket")