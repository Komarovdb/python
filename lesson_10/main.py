
num = int(input("Ярусов: "))
while True:
    symbol = input("Символ: ")
    if len (symbol.strip()) == 1:
        break
    else:
        print("one symbol")
for movavi in range(1, num + 1):
    print(" " * (num-movavi), end="")
    print(movavi * symbol, end="")
    print (movavi * symbol)

