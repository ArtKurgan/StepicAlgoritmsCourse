n, *A = map(int, input().split())
k, *nums = map(int, input().split())
l = 0
r = n
res = []
for i in range(k):
    while l <= r:
        m = round(((l+r)/2))
        if A[m] == nums[i]:
            res.append((A.index(nums[i])+1))
            break
        elif A[m] > nums[i]:
            r = m - 1
        else:
            l = m + 1
    if len(res) < i+1:
        res.append(-1)
    l = 0
    r = n
print(*res)
