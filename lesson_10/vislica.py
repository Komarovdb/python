
intro = """
   ▓▀▀▀▀▄   ▐█    ██   ▄▓▀▀▀▀▄   █▒▀▀▀▒      ▓▀▓      ▐█    ██  ▐█     ▐█        ▓▀▓
   ▒▌▄▄▄▀   ▐█  ▄█▀█  ▓▌         █▌         ▓▌ ▐▓     ▐█  ▄█▀█  ▐█     ▐█       ▓▌ ▐▓ 
   ▒▌  ▀█▄  ▐█╔▓▀ ▐█  █          █▌█▌█▌    ▓▌   ▐▓    ▐█╔▓▀ ▐█  ▐█     ▐█      ▓▌▄▄▄▐▓ 
   ▒▌  ▄█▀  ▐██   ▐█  ▀▓▄    ▄   █▌       ▓▌     ▐▓   ▐██   ▐█   ▀▀▀▀▀▀▀▀▐    ▓▌     ▐▓
   ▀▀▀▀     ▀▀     ▀     ▀▀▀▀    ▓▒▄▄▄▒  ▐█       █▌  ▀▀     ▀           ▐   ▐█       █▌
"""
print(intro)
import random as r
vocab=["кактус", "телефон", "мышка", "компьютер", "дуб", "мудрость",]
w_ans=r.choice(vocab).lower()
w_dis=[]
for i in range(0,len(w_ans)):
    w_dis.append("_")
cou=0
life=6

while cou != len(w_ans) and life > 0:

    let = input("Введи букву: ")
    let_is_be = False
    for i in range(0, len(w_ans)):
        if let == w_ans[i]:
            if w_dis[i] != "_":
                let_is_be = True
            else:
                w_dis[i] = let
                cou += 1
                let_is_be = True
    if not let_is_be:
        life = life - 1
    print(w_dis)
if cou == len(w_ans):
    print("ура, победа")
else:
    print("боже бот")