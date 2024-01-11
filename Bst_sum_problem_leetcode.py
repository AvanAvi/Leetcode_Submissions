class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:  
                return dfs(node.left)
            else:
                return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

# Sample binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

solution = Solution()
low = 3
high = 18
print(solution.rangeSumBST(root, low, high))