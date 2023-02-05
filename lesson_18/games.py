import easygui as es
import random as rand

def rock_paper_scissors():
    r="amg/duen.png"
    s="amg/bol.png"
    p="amg/дуб.png"
    user=es.buttonbox(
        images=[r,s,p],
        choices=("выйти",),)

    z=rand.choice([r,p,s])

    if user == z:
        es.msgbox(msg="нечья")
    elif user == p and z == s or user == r and z == p or user == s and z == r:
        es.msgbox("ю луз")
    else:
        es.msgbox("ю вин")


def guess_the_number():
    inte=rand.randint(1,100)
    gtn=es.integerbox(upperbound=100, lowerbound=1, msg="Отгадай число от 1 до 100")
    while gtn != inte:
        if gtn > inte:
            gtn=es.integerbox(upperbound=100, lowerbound=1, msg=f"Это число меньше, чем {gtn}", image="amg/down.png")
        elif gtn < inte:
            gtn=es.integerbox(upperbound=100, lowerbound=1, msg=f"Это число больше, чем {gtn}", image="amg/up.png")
    es.msgbox(image="amg/apon.png", msg="пабеда")


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = es.buttonbox('Выбери игру!', choices=games, image="amg/wink.png")
    if res is None:
        break
    games_entry_points[games.index(res)]()