#!/usr/bin/python

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        count = 0
        ans = []
        p = []
        selected = [0] * len(num)
        self.helper(count, num, ans, p, selected)
        return ans

    def helper(self, count, num, ans, p, selected):
        if (count == len(num)):
            ans.append(list(p))
            return
        for i in range(len(num)):
            if (selected[i] == 0):
                if (i > 0 and
                    num[i] == num[i-1] and
                    selected[i-1] == 0):
                    continue
                selected[i] = 1
                p.append(num[i])
                self.helper(count+1, num, ans, p, selected)
                selected[i] = 0
                p.pop()
num = [1,1,2]
sol = Solution()
print sol.permuteUnique(num)