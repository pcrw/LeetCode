#!/usr/bin/python

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        ans = 0
        prev = None
        i = 0
        count = 0
        while (ans < len(A)):
            if (prev == A[ans]):
                count += 1
                if (count > 2):
                    del A[ans]
                else:
                    ans += 1
            else:
                prev = A[ans]
                count = 1
                ans += 1
        return ans

n = [1,1,1,2,2,3]
sol = Solution()
ans = sol.removeDuplicates(n)
print n
print ans

#for i in range(n):
#    for j in range(n):
#        print str(ans[i][j])+' ',
#    print ' '