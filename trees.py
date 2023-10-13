from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def max_depth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    return 1 + (max(self.maxDepth(root.left), self.maxDepth(root.right)))
        
    