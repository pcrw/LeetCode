#!/usr/bin/python
# definition of a binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        ans = []
        if (root):
            self.helper(root, ans)
        return ans

    def helper(self, node, ans):
        if (node.left):
            self.helper(node.left, ans)
        if (node.right):
            self.helper(node.right, ans)
        ans.append(node.val)

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

sol = Solution()
ans = sol.postorderTraversal(node)
print ans
