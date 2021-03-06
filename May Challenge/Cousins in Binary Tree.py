"""

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""

"""---SOLUTION---"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        arr = [[0, 0] for _ in range(101)]

        def traverse(r, depth, pv):
            if not r: return
            arr[r.val] = [depth, pv]
            traverse(r.left, depth + 1, r.val)
            traverse(r.right, depth + 1, r.val)

        traverse(root, 0, -1)
        return arr[x][0] == arr[y][0] and arr[x][1] != arr[y][1]