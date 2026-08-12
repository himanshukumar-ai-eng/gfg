class Solution:
    def sortedMerge(self, a, b):
        a.sort()
        b.sort()

        res = []
        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1

        while i < len(a):
            res.append(a[i])
            i += 1

        while j < len(b):
            res.append(b[j])
            j += 1

        return res