import random as r
life=10
lenght=3
ans=r.randint(100,999)
ans=str(ans)
while life:
    is_guessed = False
    print("=" * 10)
    print("lifes:", life)
    guess=input("100 to 999?")
    if len(guess) != lenght or not guess.isdigit:
