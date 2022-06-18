k, l = map(int, input().split())
DirCode = {}
tmp = []
for i in range(k):
    tmp.append(tuple(map(str, input().split(': '))))
    DirCode[tmp[i][1]] = tmp[i][0]
SCode = input()
result = ''
code = ''
for i in SCode:
    code += i
    if code in DirCode:
        result += DirCode[code]
        code = ''
    else:
        continue
print(result)
