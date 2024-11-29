def akinator(x, array, low, high):
    while low <= high:
        mid = (high + low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

array = [0, 1, 2, 3, 4, 5]
x = 0
result = akinator(x, array, 0, len(array)-1)
print("O seu x é " + str(result))