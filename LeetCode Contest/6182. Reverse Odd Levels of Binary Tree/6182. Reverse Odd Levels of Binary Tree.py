# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def swap_nodes(self, node, height):
        if node.left and node.right:
            if height % 2 == 0:
                node.left.val, node.right.val = node.right.val, node.left.val
            height += 1
            self.swap_nodes(node.left, height)
            self.swap_nodes(node.right, height)

    def reverseOddLevels(self, root):
        self.swap_nodes(root, 0)
        return root


# [7,13,11]
[0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
treeNode0 = TreeNode(0)
treeNode1 = TreeNode(1)
treeNode2 = TreeNode(2)
treeNode3 = TreeNode(3)
treeNode4 = TreeNode(4)
treeNode5 = TreeNode(5)
treeNode6 = TreeNode(6)
treeNode7 = TreeNode(7)
treeNode8 = TreeNode(8)
# treeNode9 = TreeNode(9)
# treeNode10 = TreeNode(10)
# treeNode11 = TreeNode(11)
# treeNode12 = TreeNode(12)
# treeNode13 = TreeNode(13)
# treeNode14 = TreeNode(14)
treeNode0.left = treeNode1
treeNode0.right = treeNode2
treeNode1.left = treeNode3
treeNode1.right = treeNode4
treeNode2.left = treeNode5
treeNode2.right = treeNode6
treeNode3.left = treeNode7
treeNode3.right = treeNode8
# # treeNode4.left = treeNode9
# treeNode4.right = treeNode10
# treeNode5.left = treeNode11
# treeNode5.right = treeNode12
# treeNode6.left = treeNode13
# treeNode6.right = treeNode14

root = treeNode0
sol = Solution()
res = sol.reverseOddLevels(root)
print(res)
