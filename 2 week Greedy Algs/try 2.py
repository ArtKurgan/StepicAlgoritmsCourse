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
        if sortlines[k+i][0] <= sortlines[k][1] <= sortlines[k+i][1]:
            del sortlines[k+i] # нужно заменить на что-то что бы сохранить индекс
    del sortlines[k] # нужно заменить на что-то что бы сохранить индекс

print(dots)
