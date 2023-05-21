a = input().split()
pribl1 = int(a[0])
pribl2 = int(a[1])
print(a)
count = 0
while a[0]> a[1]:
    pribl1[1] *= 2
    pribl2[0] *= 3
    count += 1
print(count)
