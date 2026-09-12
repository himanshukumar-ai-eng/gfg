class Solution:
    def minIncrements(self, arr):
        arr.sort()
        operation = 0

        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                new_value = arr[i - 1] + 1
                operation += new_value - arr[i]
                arr[i] = new_value

        return operation