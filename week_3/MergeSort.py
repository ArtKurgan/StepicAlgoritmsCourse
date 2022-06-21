n = int(input())
array_input = list(map(int, input().split()))
inversion = 0

def separation(array, left_edge, right_edge):
        if len(array) > 1:
            print(array)
            middle = (left_edge + right_edge) // 2
            array_left = array[0:middle]
            array_right = array[middle:len(array)]
            return merge(separation(array_left, 0, middle), separation(array_right, middle+1, len(array_right)-1))
        return array


def merge(array_1, array_2):
    sorted_array = []
    inversion = 0
    for i in range(len(array_1) + len(array_2)):
        if len(array_1) == 0:
            sorted_array= sorted_array + array_2
            break
        elif len(array_2) == 0:
            sorted_array = sorted_array + array_1
            break
        if array_1[0] > array_2[0]:
            sorted_array.append(array_2.pop(0))
            inversion += 1
        elif array_1[0] <= array_2[0]:
            sorted_array.append(array_1.pop(0))
            inversion += 1
    return sorted_array


print(separation(array_input, 0, n-1))
