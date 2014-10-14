#!/usr/bin/python

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        ans = [[0 for j in range(n)] for i in range(n)]
        left = 0
        right = n
        top = 0
        bottom = n
        i = 0;
        j = 0;
        count = 1
        while 1:
            for j in range(left, right):
                ans[i][j] = count
                count += 1
            top += 1
            for i in range(top,bottom):
                ans[i][j] = count
                count += 1
            right -= 1
            for j in reversed(range(left,right)):
                ans[i][j] = count
                count += 1
            bottom -= 1
            for i in reversed(range(top,bottom)):
                ans[i][j] = count
                count += 1
            left += 1
            if ((right <= left) or
                (top >= bottom)):
                break
        return ans

n = 4
sol = Solution()
ans = sol.generateMatrix(n)
print ans

#for i in range(n):
#    for j in range(n):
#        print str(ans[i][j])+' ',
#    print ' '