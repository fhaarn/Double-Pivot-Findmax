
def findmax(arr):
    n = len(arr)
    max = 0
    for i in range(1, len(arr)//2 + 1):
        if arr[max] < arr[i]:
            max = i
        if arr[max] < arr[n - i]:
            max = n
    return arr[max]


# Test for both odd and even array

arrOdd = [12, 11, 13, 5, 6]
arrEv = [12, 11, 13, 5, 6, 2]

print(findmax(arrOdd))
print(findmax(arrEv))