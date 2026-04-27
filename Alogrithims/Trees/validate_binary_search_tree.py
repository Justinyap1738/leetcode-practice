# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        def valid_BST(node, left, right):
            if not node:
                return True
            
            if not(node.val < right and node.val > left):
                return False

            return(valid_BST(node.left, left, node.val) and
                    valid_BST(node.right, node.val, right))

        return valid_BST(root, float("-inf"), float("inf"))