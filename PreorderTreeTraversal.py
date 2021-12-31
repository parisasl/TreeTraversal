#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def preorderTraversal(root):
    TreeList = []
    if root is None:
        return TreeList 
    stack = [root]
    while len(stack)>0:
        currNode = stack.pop()
        # add the root to the list
        TreeList.append(currNode.val)
        # add the right tree to the stack
        if currNode.right != None:
            stack.append(currNode.right)
        # add teh left tree to the stack    
        if currNode.left != None:
            stack.append(currNode.left)
    return TreeList

#root = {TreeNode.val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}
root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
print(preorderTraversal(root))
