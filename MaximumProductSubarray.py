class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if (A == None or len(A) == 0):
            return
        pos = max(0, A[0])
        neg = min(0, A[0])
        ans = A[0]
        for i in range(1, len(A)):
            num = A[i]
            if (num == 0):
                pos = 0
                neg = 0
                continue
            elif (num > 0):
                pos = max(1, pos)*num
                neg = neg*num
            else:
                pos2 = pos
                pos = neg*num
                neg = min(num, num*pos2)
            ans = max(ans, pos)
        return ans
