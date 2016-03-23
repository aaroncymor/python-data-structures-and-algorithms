"""
Here is a simple solution- If a tree is a binary search tree, then 
traversing the tree inorder should lead to sorted order of the values 
in the tree. So, we can perform an inorder traversal and check whether 
the node values are sorted or not. 
"""
class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

tree_vals = []

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild())
        
def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)

inorder(tree)
sort_check(tree_vals)

"""
Another classic solution is to keep track of the minimum and 
maximum values a node can take. And at each node we will check 
whether its value is between the min and max values it’s allowed 
to take. The root can take any value between negative infinity and 
positive infinity. At any node, its left child should be smaller 
than or equal than its own value, and similarly the right child 
should be larger than or equal to. So during recursion, we send 
the current value as the new max to our left child and send the min 
as it is without changing. And to the right child, we send the current
 value as the new min and send the max without changing.
"""

class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None

def tree_max(node):
    if not node:
        return float("-inf")
    maxleft  = tree_max(node.left)
    maxright = tree_max(node.right)
    #print "MAX",maxleft, maxright,node.key,max(node.key,maxleft,maxright)
    return max(node.key, maxleft, maxright)

def tree_min(node):
    if not node:
        return float("inf")
    minleft  = tree_min(node.left)
    minright = tree_min(node.right)
    #print "MIN",minleft, minright,node.key, min(node.key,minleft,minright)
    return min(node.key, minleft, minright)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        return True
    else:
        return False

root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

#print(verify(root)) # prints True, since this tree is valid

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15,"Fifteen")
#root.right.left = Node(15, "Fifteen")

print(verify(root)) # prints False, since 15 is to the left of 10

a = TreeNode(17)
b = TreeNode(5)
c = TreeNode(35)
d = TreeNode(2)
e = TreeNode(11)
f = TreeNode(29)
g = TreeNode(38)
h = TreeNode(9)
i = TreeNode(16)
j = TreeNode(7)
k = TreeNode(8)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i
h.left = j
j.right = k

print isValidBST(a)