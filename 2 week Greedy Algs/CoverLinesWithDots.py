n = int(input())
alllines = []
for i in range(n):
    (a, b) = map(int, input().split())
    alllines.append((a , b))
sortlines = sorted(alllines, key=lambda x: x[1])

dots = set()

def rmlines():
    k = 0
    dots.add(sortlines[k][1])
    for i in range(1, n):
        if sortlines[k+i][0] <= sortlines[k][1] <= sortlines[k+i][1]:
            del sortlines[k+i]
    del sortlines[k]
    if len(sortlines) == 0:
        return(dots)
    return rmlines()

///