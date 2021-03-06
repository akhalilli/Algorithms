
"""
@github: github.com/alikhalilli

Time Complexity: O(n)
Auxiliary Space: O(d)

[1, 2, 3, 4, 5, 6]
rotate by d=2 element to right
[5, 6] - copy 2 elements to temp_arr
[1, 2, 1, 2, 3, 4]
replace by temp array first d elements
[5, 6, 1, 2, 3, 4]
"""


class Solution(object):
    def __init__(self, arr, direction, d, printarr=True):
        self.direction = direction
        self.arr = arr
        self.n = len(self.arr)
        self.d = d % self.n
        self.temp_arr = [None] * self.d
        self.print = printarr

    def rotate(self):
        if self.direction == 'right':
            self.__rightRotate()
        else:
            self.__leftRotate()

        if self.print:
            self.__printArr()

    def __rightRotate(self):
        """
        [1, 2, 3, 4, 5] => 4
        [1, 2, 1, 2, 3]
        [4, 5, 1, 2, 3]
        """
        # Space O(d)
        temp_arr = [None] * self.d
        """
        5-2=3...5
        i=3
        i=4

        5-3-1=1
        5-4-1=0
        """

        # Time => O(n), if n=d
        for i in range(self.d):
            temp_arr[i] = self.arr[self.n-self.d+i]

        for i in range(self.n, self.d, -1):
            self.arr[i-1] = self.arr[i - self.d - 1]

        for i in range(self.d):
            self.arr[i] = temp_arr[i]

    def __leftRotate(self):
        """
        [1, 2, 3, 4, 5] => 5
        [3, 4, 5, 4, 5] => 5-2
        [3, 4, 5, 1, 2]
        """
        temp_arr = [None] * self.d
        for i in range(self.d):
            temp_arr[i] = arr[i]

        for i in range(self.n-self.d):
            arr[i] = arr[i+self.d]
        print(arr)

        for i in range(self.d):
            arr[self.n - self.d + i] = temp_arr[i]

    def __printArr(self):
        print('{} rotated array: {}'.format(self.direction, self.arr))


arr = [1, 2, 3, 4, 5]
sol = Solution(arr, 'right', -2)
sol.rotate()
