#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        i = 1
        current = head
        while (i < m-1):
            current = current.next
            i += 1
        node = self.helper(current.next, n-m, current)
        return node

    def helper(self, node, size, first):
        if (size == 0):
            first.next = node
            return node
        ret = self.helper(node.next, size-1, first)

        node.next = ret.next
        ret.next = node

        return node

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e


sol = Solution()
ans = sol.reverseBetween(a, 2, 4)

while (ans != None):
    print ans.val
    ans = ans.next





#for i in range(n):
#    for j in range(n):
#        print str(ans[i][j])+' ',
#    print ' '