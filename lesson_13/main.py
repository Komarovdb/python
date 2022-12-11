# lst = [1, 2, 3, 8,]
# lt = [87, 98, 31, 8]
# a = (lt + lst)
# a = set(a)
# y = len(a)
# l = len(lst)
# t = len(lt)
# tr = (l + t - y)
# print(tr,lt,lst)
# lst = [1, 2, 3, 8,]
# lt = [2, 1, 31, 8]
# a = (lt + lst)
# a = set(a)
# y = len(a)
# l = len(lst)
# t = len(lt)
# a=list(a)
# a.sort()
# sorted(a)
# print(a)
# l1=[22,75,90,89]
# l2=[22,98,90,43,678,89]
# l3=list(set(l1) & set(l2))
# l3.sort(reverse=True)
# print(l3[::-1])
ty=[6,2,3,4,4,6,7,4,9,2]
tp=[]
x=0
for x in range(0, len(ty)):
    if ty[x] in tp:
        print("YES")
    else:
        print("NO")
        tp.append(ty[x])
