import random as r
cards=[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
hand_c = [r.choice(cards)]
hand_p = [r.choice(cards)]
score_p = 0
score_c = 0
get_card = "y"
while get_card == "y":
    hand_p.append(r.choice(cards))
    if sum(hand_p) > 21 and 11 in hand_p:
        for i in range(0,len(hand_p)):
            if hand_p[i] == 11:
                hand_p[i] == 1
    score_p = sum(hand_p)
    print(F"твоя рука: {hand_p}. Очков: {score_p}")
    print("первая карта компьютера:", hand_c[0])
    if score_p>21:
        get_card = "n"
    else:
        get_card = input("y - взять карту n - остановится: ")
        if sum(hand_c) > 21 and 11 in hand_c:
            for i in range(0, len(hand_c)):
                if hand_c[i] == 11:
                    hand_c == 1
    score_c = sum(hand_c)
    print("="*10)
    print(f"Твоя итоговая рука: {hand_p}. Очков: {score_p}")
    print(f"Итоговая рука бота: {hand_c}. Очков: {score_c}")
if score_c>21 and score_p>21:
    print("ничья")
elif score_p==score_c:
    print("ничья")
elif score_p>21:
    print("поражение")
elif score_c>21:
    print("победа")
elif score_c>score_p:
    print("поражение")
elif score_c<score_p:
    print("победа")

