# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, name):
        self.val = x
        self.left = None
        self.right = None
        self.name = name


class Solution:
    def removeLeafNodes(self, root, target):
        if root.left: root.left = self.removeLeafNodes(root.left, target)
        if root.right: root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root

        # if root is None:
        #     return None
        
        # def postorder(node, target):
        #     if node.left: node.left = postorder(node.left, target)
        #     if node.right: node.right= postorder(node.right, target)
        #     if node.left == None and node.right == None:
        #         if node.val == target:
        #             return None
        #     return node
        # return postorder(root, target)


if __name__ == "__main__":
    solution = Solution()
    TreeNode1 = TreeNode(1, 1)
    TreeNode2 = TreeNode(2, 2)
    TreeNode3 = TreeNode(3, 3)
    TreeNode4 = TreeNode(2, 4)
    TreeNode6 = TreeNode(2, 6)
    TreeNode7 = TreeNode(4, 7)

    TreeNode1.left = TreeNode2
    TreeNode1.right = TreeNode3
    TreeNode2.left = TreeNode4
    TreeNode3.left = TreeNode6
    TreeNode3.right = TreeNode7

    print("Result", solution.removeLeafNodes(TreeNode1, 2))
