"""
@github: github.com/alikhalilli

Time Complexity: O(n)
Space Complexity: O(1)

arr = [1, 2, 3, 4, 5, 6]
[3, 4, 5, 6, 1, 2]
[5, 6, 1, 2, 3, 4]

n = 6, d=2
A = [1, 2]
B = [3, 4, 5, 6]
rA = [2, 1]
rB = [6, 5, 4, 3]

rArB = [2, 1, 6, 5, 4, 3]
r(rArB) = [3, 4, 5, 6, 1, 2]

[5, 6, 1, 2, 3, 4]
[4, 3, 2, 1, 6, 5]
rB = [6, 5]
rA = [4, 3, 2, 1]
rArB = [4, 3, 2, 1, 6, 5]
r(rArB) = [5, 6, 1, 2, 3, 4]
[1, 2, 3, 4, 5, 6]

"""


class Solution(object):
    def __init__(self, arr, direction, d, printarr=True):
        self.arr = arr
        self.n = len(arr)
        self.d = d % self.n
        self.print = printarr
        self.direction = direction

    def rotateArr(self):
        if self.direction == 'left':
            self.__reverseArr(0, self.d-1)
            self.__reverseArr(self.d, self.n-1)
            self.__reverseArr(0, self.n-1)
        else:
            self.__reverseArr(self.n-self.d, self.n-1)
            self.__reverseArr(0, self.n-self.d-1)
            self.__reverseArr(0, self.n-1)

        if self.print:
            print(self.arr)

    def __reverseArr(self, start, end):
        while start < end:
            temp = self.arr[start]
            self.arr[start] = self.arr[end]
            self.arr[end] = temp
            start += 1
            end -= 1


arr = [1, 2, 3, 4, 5, 6]
sol = Solution(arr, 'right', 2)
sol.rotateArr()
