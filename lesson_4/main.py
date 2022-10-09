#print(alphabet[::3])
#[start:end:step]
#print(alphabet[::-3]) #в обратном порядке
#print(phrase.upper())
#freyz="nGa,NiG,NgA,nIg"
#print(freyz.capitalize())
#name=input("имя:").capitalize()
#fathername=input("отчество:").capitalize()
#print(surname, name[0]+".",fathername[0]+".")
#print(f"{surname} {name[0]}. {fathername[0]}.")
#x = input()
#print(x.count('a')) #кол-во мал. "a"
#print(x.lower().count('a')) #кол-во всех "a"x
#x=input()
#lst=x.split(",")
#lst.pop(0)
#print(lst)
#phrase=input()
#find=input()
#rint(phrase.replace(find, replase))
#replase=input()
#phrase=input()
#print(phrase.replace("mum","otchim"))
#alphabet={
#    " ": " ",
#    "a": "1",
#    "b": "2",
#    "c": "3",
#}
#x = input()
#num = ""
#for letter in x:
    #num=num+alphabet[letter]
#print(num)
email=input()
print(email.split("@"))
login=input(email.split("@"))[0]
domain=email.split("@")[-1]