

"""
Space Complexity: O(1)
Time Complexity: O(n*d)

"""



arr = [1, 2, 3, 4, 5]
def rotateArrLeft(arr, d):
    n=len(arr)
    split_point=d%n
    for _ in range(split_point):
        rotateLeft(arr, n)

def rotateArrRight(arr, d):
    n=len(arr)
    split_point=d%n
    for _ in range(split_point):
        rotateRight(arr, n)


def rotateLeft(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

def rotateRight(arr, n):
    temp = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

rotateArrLeft(arr, 3)
print(arr)
rotateArrRight(arr, 2)
print(arr)