# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
# def postorderTraversal(self, root):
#     TreeList, stack = [], [root]
#     while stack:
#         currNode = stack.pop()
#         if currNode:
#             TreeList.append(currNode.val)
#             stack.append(currNode.left)
#             stack.append(currNode.right)
#     return TreeList[::-1]

#RECURSIVE VERSION
def postorderTraversal(root):
    TreeList =[]
    if root is None:
        return TreeList
    helper(root,TreeList)
    return TreeList
    
def helper(root,TreeList):
    if root != None:
        helper(root.left,TreeList)
        helper(root.right,TreeList)
        TreeList.append(root.val)

# root = TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}
root = TreeNode(1, None, TreeNode(2, TreeNode(3,None,None),None))  
print(postorderTraversal(root))