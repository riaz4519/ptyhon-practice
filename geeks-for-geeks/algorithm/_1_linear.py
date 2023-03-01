#arr[] = {10, 20, 80, 30, 60, 50,110, 100, 130, 170}, x = 175;


def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i

    return -1


if __name__ == '__main__':

    arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    x = 170
    n = len(arr)

    result = search(arr, n, x)

    if (result == -1):
        print("Element is not present in the array")
    else:
        print("Element is present at index :", result)
