import time
import random


def sum3(arr, finder):
    """
    :param arr: the list in which the sum is sought
    :param finder: the value of the sum of 3 numbers
    :return: count of sums of 3 numbers
    """
    count = 0
    arr_uni = set()
    for j in range(len(arr) - 2):
        a = arr[j]
        k = j + 1
        l = len(arr) - 1
        while k < l:
            b = arr[k]
            c = arr[l]
            g = str(a) + str(b) + str(c)
            if a + b + c == finder and g not in arr_uni:
                arr_uni.add(g)
                count += 1
                k += 1
            elif a + b + c > 0:
                l -= 1
            else:
                k += 1
    return count


# определяем список чисел и сортируем его по возрастанию
for n in range(3, 10000, 100):
    start_time = time.time()
    lst = []
    k2 = set()  # множество элементов, которые встречаются в списке 2 раза
    k3 = set()  # множество элементов, которые встречаются в списке 3 раза
    positive = 0
    negative = 0
    for i in range(n):
        y = random.randint(-10000, 10000)
        s = set(lst)
        if y > 0:
            positive += 1
        elif y < 0:
            negative += 1
        if y not in k3:
            if y not in k2:
                if y not in s:
                    lst.append(y)
                else:
                    k2.add(y)
                    lst.append(y)
            else:
                k3.add(y)
                lst.append(y)
    if (positive == 0 or negative == 0) and 0 not in s:
        pass
    else:
        lst.sort()
        sum3(lst, 0)
    print("Для " + str(n) + " элементов " + str(time.time() - start_time) + " секунд")
