a, b = map(int, input().split())
l = [a, b]
if l[0] == 0:
    print(b)
elif l[1] == 0:
    print(a)
else:
    while l[0] != 0 and l[1] != 0:
        if l[0] >= l[1]:
            l[0] = l[0] % l[1]
        elif l[1] >= l[0]:
            l[1] = l[1] % l[0]
if l[0] == 0:
    print(l[1])
else:
    print(l[0])

