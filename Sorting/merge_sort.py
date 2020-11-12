def merge(left, right):
    list = []
    right_index = 0
    left_index = 0
    while right_index < len(right) and left_index < len(left):
        if right[right_index] <= left[left_index]:
            list.append(right[right_index])
            right_index += 1
        else:
            list.append(left[left_index])
            left_index += 1
    while left_index < len(left):
        list.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        list.append(right[right_index])
        right_index += 1
    return list


def merge_sort(list):
    if len(list) <= 1:
        return list
    left = []
    right = []
    midpoint = len(list)/2
    index = 0
    while index <= midpoint - 1:
        left.append(list[index])
        index += 1
    while index < len(list):
        right.append(list[index])
        index += 1
    return merge(merge_sort(left), merge_sort(right))


x = [33, 22, 1, 1, 1, 3, 343, 3, 4, 5, 8, 7, 5, 4, ]
print(merge_sort(x))
