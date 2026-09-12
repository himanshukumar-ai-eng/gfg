from collections import Counter
class Solution:
	def topKFreq(self, arr, k):
	    freq = Counter(arr)
	    elements = sorted(freq, key = lambda x: (-freq[x], -x))
	    
	    return elements[:k]
		# Code here
		
		