s = input()
symb = set()
l = []
moms = []
for i in range(len(s)):
    if s[i] not in symb:
        symb.add(s[i])
        l.append([s[i], s.count(s[i])])
H = sorted(l, key=lambda x: x[1], reverse=True)
Htmp =  sorted(l, key=lambda x: x[1], reverse=True)
code1 = '1'
code2 = '0'
allin = {}
res = ''
if len(s) > 1:
    for i in range(len(H)+1, 2*len(H)):
        a = H.pop(H.index(min(H, key=lambda x : x[1])))
        b = H.pop(H.index(min(H, key=lambda x : x[1])))
        moms.append(['k'+str(i), a[0], b[0]])
        Htmp.append(['k' + str(i), a[1]+b[1]])
        H.append((['k' + str(i), a[1]+b[1]]))
    Hfinal =  sorted(Htmp, key=lambda x: x[1], reverse=True)
    for i in range(len(moms)-1, -1 , -1):
        if i == len(moms)-1:
            allin[moms[i][2]] = code2
            allin[moms[i][1]] = code1
        else:
            allin[moms[i][2]] = allin[moms[i][0]] + code2
            allin[moms[i][1]] = allin[moms[i][0]] + code1
    for i in s:
        res += allin[i]
else:
    allin[s[0]] = 0
    res = '0'
print(len(l), '', len(res))
for key, value in allin.items():
    if len(key) == 1:
        print(key+':' , value)
print(res)
#asdasdgfsdfgsfdgsaadsdasdaasdsd