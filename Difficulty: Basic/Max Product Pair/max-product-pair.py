class Solution:
	def maxProduct(self,arr):
	    n = len(arr)
	    if n < 2:
	        return -1
	    arr.sort()
	    product = arr[n - 1] * arr[n - 2]
	    return product
	        
	        
	    
	    
	   
	   
		
		