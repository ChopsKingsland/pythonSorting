def insertSort(data):
    temp = 0
    current = 0
    atLHS = False

    for i in range(0, len(data)):
        current = i
        atLHS = False

        while data[current] < data[current - 1] and not atLHS:
            temp = data[current]
            data[current] = data[current - 1]
            data[current - 1] = temp

            if current > 1:
                current -= 1
            else:
                atLHS = True
    return data

unsortedArr = [25, 4, 643, 10, 454, 1, 4, 2, 100, 1, 1, 1, 645]
sortedArr = insertSort(unsortedArr)

print(sortedArr)