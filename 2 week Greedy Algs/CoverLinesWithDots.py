n = int(input())
alllines = []
for i in range(n):
    (a, b) = map(int, input().split())
    alllines.append((a , b))
sortlines = sorted(alllines, key=lambda x: x[1])

dots = set()

def rmlines(l):
    k = 0
    dots.add(l[k][1])
    for i in range(1, n):
        if l[k+i][0] <= l[k][1] <= l[k+i][1]:
            del l[k+i]
    del l[k]
    if len(l) == 0:
        return(dots)
    return rmlines(l)
