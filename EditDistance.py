#!/usr/bin/python

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        dis = [[0 for j in range(len2+1)] for i in range(len1+1)]

        for i in range(len1+1):
            dis[i][0] = i
        for j in range(len2+1):
            dis[0][j] = j

        for i in range(len1):
            c1 = word1[i]
            for j in range(len2):
                c2 = word2[j]
                if (c1 == c2):
                    dis[i+1][j+1] = dis[i][j]
                else:
                    replace = dis[i][j] +1
                    delete = dis[i+1][j] +1
                    insert = dis[i][j+1] +1

                    m = replace if (replace < delete) else delete
                    if (insert < delete):
                        m = insert 
                    dis[i+1][j+1] = m
        return dis[len1][len2]


sol = Solution()
ans = sol.minDistance('', 'a')
print ans