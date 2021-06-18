def bubble_sort(l: list):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1, i, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
    return l


print(bubble_sort(list(map(int, input().split()))))
