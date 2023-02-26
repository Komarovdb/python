
try:
    f = open("filt.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("error")
txt = f.readlines()
print(f"Строк: {len(txt)}")
ft = " ".join(txt).replace("\n", "")
print(ft)
words = ft.split()
print(f"Слов: {len(words)}")
s = ft.replace(" ","")
print(f"Символов: {len(s)}")

word = input()
try:
    f = open("filt.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("error")
text = f.read()




try:
    f = open("filt.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("error")
