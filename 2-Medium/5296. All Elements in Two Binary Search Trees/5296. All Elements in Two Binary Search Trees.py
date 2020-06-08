# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1, root2):

        res = []
        self.preorder(root1, res)
        self.preorder(root2, res)
        res.sort()
        return res

    def preorder(self, node, arr):
        if not node:
            return None
        if node.left:
            self.preorder(node.left, arr)
        arr.append(node.val)
        if node.right:
            self.preorder(node.right, arr)
        return arr


if __name__ == "__main__":
    solution = Solution()

    TreeNode11 = TreeNode(1)
    TreeNode12 = TreeNode(2)
    TreeNode14 = TreeNode(4)
    TreeNode20 = TreeNode(0)
    TreeNode21 = TreeNode(1)
    TreeNode23 = TreeNode(3)

    root1 = TreeNode12
    TreeNode12.left = TreeNode11
    TreeNode12.right = TreeNode14

    root2 = TreeNode21
    TreeNode21.left = TreeNode20
    TreeNode21.right = TreeNode23

    print(solution.getAllElements(root1, root2))
