def bubble_sort(data):
    for i in range(0, len(data)-1):
        for j in range(i+1, len(data)):
            if(data[i] > data[j]):
                data[i], data[j] = data[j], data[i]

    return data


x = [33, 22, 1, 1, 1, 3, 343, 3, 4, 5, 8, 7, 5, 4, ]
print(bubble_sort(x))
