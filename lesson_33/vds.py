input()
color = list(input())
per = 0
while per != len(color)-1:
    if color[per] == color[per+1]:
        color.pop(color[per])
    else:
        per += 1
        print(color)