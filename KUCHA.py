def siftup(i):
    while i > 0 and kucha[i//2-1] < kucha[i]:
       if i <= 2:
           if kucha[i] > kucha[0]:
               kucha[i], kucha [0] = kucha[0], kucha[i]
       else:    
           kucha[i], kucha [i//2-1] = kucha[i//2-1], kucha[i]
           i = i//2-1
def sifdown(i):
    while 2 * i + 1 <= len(kucha) - 1:
        big = i
        if kucha[2*i+1] > kucha[big]:
            big = 2 * i
        if 2 * i + 2 <= len(kucha) - 1 and kucha[2*i+2] > kucha[big]:
            big = 2*i+2
        if i == big:
            break
            
n = int(input())
cnt = -1
kucha = []
maxes = []
for j in range(n):
    line = list(map(lambda x: x, input().split()))
    if len(line) > 1:
        kucha.append(int(line[1]))
        cnt += 1
        if len(kucha) > 1:
            siftup(cnt)
    else:
        kucha[0], kucha[-1] = kucha[-1], kucha[0]
        maxes.append(kucha.pop(-1))
        sifdown(0)
        cnt -= 1
print(*maxes)
