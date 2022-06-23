def binary_search(sorted_arr, findable_value):
    l = 0
    r = len(sorted_arr) - 1

    while l <= r:
        m = (l + r) // 2
        if sorted_arr[m] == findable_value:
            return m+1
        elif sorted_arr[m] > findable_value:
            r = m - 1
        else:
            l = m + 1

    return -1

n, *A = map(int, input().split())
k, *nums = map(int, input().split())


for i in range(k):
    print(binary_search(A, nums[i]), end=' ')
