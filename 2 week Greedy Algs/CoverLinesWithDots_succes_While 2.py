n = int(input())
alllines = []
for i in range(n):
    (a, b) = map(int, input().split())
    alllines.append((a , b))
sortlines = sorted(alllines, key=lambda x: x[1])

dots = set()

while len(sortlines) != 0:
    k = 0
    dots.add(sortlines[k][1])
    for i in range(1, n):
        i = i - k
        if len(sortlines) == 1 or i == len(sortlines):
            break
        if sortlines[i][0] <= sortlines[0][1] <= sortlines[i][1]:
            del sortlines[i]
            k += 1
    del sortlines[0]

print(len(dots))
for i in dots:
    print(i, '' , end='')

