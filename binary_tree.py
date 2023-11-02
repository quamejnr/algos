from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    data: int

@dataclass
class TreeNode:
    parent: Optional[Node, None]=None
    left: Optional[Node, None]=None
    right: Optional[Node, None]=None

# def find_minimum(root: Tree):
#     while root.left:
#         root = root.left
#     
#     return root
#
# def traverse(root: Tree):
#     if root != None:
#         traverse(root.left)
#         process(root.item)
#         traverse(root.right)
#
# def traverse_iter(root: Tree):
#     stack = []
#     current = root
#
#     while True:
#         if current is not None:
#             stack.append(current)
#             current = current.left
#
#         elif stack:
#             current = stack.pop()
#             process(current)
#             current = current.right
#             stack.append(current)
#
#         else:
#             break

# EASY
def find_height(root):
    if root is None:
        return 0

    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return max(right_height, left_height) + 1

balance = True

def maxDepth(self, root: Optional[TreeNode]) -> int:
    nonlocal balance
    if root is None: 
        return 0
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    if abs(left-right) > 1:
        balance = False
    return max(left, right) + 1
    
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    self.maxDepth(root)
    return self.balance

