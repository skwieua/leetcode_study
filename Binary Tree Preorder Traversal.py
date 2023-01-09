class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.preOrder(root)
        return self.result

    def preOrder(self, root):
        if not root:
            return
        self.result.append(root.val)
        if root.left:
            self.preOrder(root.left)

        if root.right:
            self.preOrder(root.right)
