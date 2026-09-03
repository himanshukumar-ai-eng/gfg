import math
class Solution:
    def heapHeight(self, n, arr):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return int(math.log2(n)) 
        
        
        