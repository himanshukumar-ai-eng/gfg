class Solution:
	def kLargest(self, arr, k):
	    arr.sort(reverse = True)
	    return arr[:k]
		
		