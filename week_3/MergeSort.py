n = int(input())
array_input = list(map(int, input().split()))


def separation(array, left_edge, right_edge):
    while left_edge < right_edge:
        middle = (left_edge + right_edge) // 2
        merge(separation(array, left_edge, middle), separation(array, middle+1, right_edge))


def merge(array_1, array_2):
    sorted_array = []
    for i in range(len(array_1) + len(array_2)):
        if len(array_1) == 0:
            sorted_array= sorted_array + array_2
            break
        elif len(array_2) == 0:
            sorted_array = sorted_array + array_1
            break
        if array_1[0] > array_2[0]:
            sorted_array.append(array_2.pop(0))
        elif array_1[0] < array_2[0]:
            sorted_array.append(array_1.pop(0))
    return(sorted_array)

separation(array_input, 0, n-1)
print(array_input)