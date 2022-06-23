nums_lines, nums_dots = map(int, input().split())
starts_lines = []
ends_lines = []
for i in range(nums_lines):
    tmp = input().split()
    starts_lines.append(int(tmp[0]))
    ends_lines.append(int(tmp[1]))
dots = list(map(int, input().split()))


def partition(array, left_edge, right_edge):
    x = array[left_edge]
    j = left_edge
    for i in range(left_edge + 1, right_edge+1):
        if array[i] <= x:
            j = j + 1
            array[j], array[i] = array[i], array[j]
    array[j], array[left_edge] = array[left_edge], array[j]
    return j


def quicksort(array, left_edge, right_edge):
    if left_edge >= right_edge:
        return
    m = partition(array, left_edge, right_edge)
    quicksort(array, left_edge, m - 1)
    quicksort(array, m + 1, right_edge)


def compare_in(array, dot):
    count = 0
    for i in range(len(array)):
        if dot >= array[i]:
            count += 1
    return count


def compare_out(array, dot):
    count = 0
    for i in range(len(array)):
        if dot > array[i]:
            count += 1
    return count


quicksort(starts_lines, 0, nums_lines-1)
quicksort(ends_lines, 0, nums_lines-1)
print(starts_lines)
print(ends_lines)

for i in range(nums_dots):
    print(compare_in(starts_lines, dots[i]) - compare_out(ends_lines, dots[i]), end=' ')

