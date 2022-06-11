n, W = map(int, input().split())
items = [list(map(int, input().split())) for i in range(n)]
sortitems = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
curWei = 0
curVal = 0
for i in sortitems:
    if curWei == W:
        break
    if i[1] + curWei <= W:
        curWei += i[1]
        curVal += i[0]
    elif i[1] + curWei > W:
        if curWei == 0:
            curVal = i[0] / i[1] * W
        else:
            curWei += i[1]
            curVal += i[0] / i[1] * (i[1] - abs(curWei - W))
        break
print(curVal)


