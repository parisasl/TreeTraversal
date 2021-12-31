#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# RECURSIVE VERSION

# def helper(root,TreeList):
#     if root != None :
#         helper(root.left,TreeList)
#         TreeList.append(root.val)
#         helper(root.right,TreeList)
            
# def inorderTraversal(root):
#     TreeList = []
#     helper(root,TreeList)
#     return TreeList

    
    
def inorderTraversal(root):
    TreeList, stack = [], []
    currNode = root
    while currNode or stack:
        while currNode: # travel to each node's left child, till reach the left leaf
            stack.append(currNode)
            currNode = currNode.left
        currNode = stack.pop() # this node has no left child
        TreeList.append(currNode.val) # so let's append the node value 
        currNode = currNode.right # visit its right child --> if it has left child ? append left and left.val, otherwise append node.val, then visit right child again... cur = node.right
    return TreeList

# root = TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}
root = TreeNode(1, None, TreeNode(2, TreeNode(3,None,None),None))       
print(inorderTraversal(root))         
                
                
        