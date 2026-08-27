class Solution:
    def findMin(self, n: int) -> int:
        count = 0
        denomination = [1,2,5,10]
        for i in range(len(denomination) - 1, -1, -1):
            count += n // denomination[i]
            n = n % denomination[i]
        return count
       
       