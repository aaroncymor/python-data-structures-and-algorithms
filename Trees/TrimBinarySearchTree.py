class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

	def postorder(self):
		if self.left:
			self.left.postorder()
		if self.right:
			self.right.postorder()
		print self.val

def trimBST(tree, minVal, maxVal): 
    
    if not tree: 
        return 
    
    tree.left=trimBST(tree.left, minVal, maxVal) 
    tree.right=trimBST(tree.right, minVal, maxVal) 
    
    if minVal<=tree.val<=maxVal:
    	print "This: " + str(tree.val)
        return tree 
    
    if tree.val<minVal:
    	if tree.right == None:
    		print "None"
    	else:
    		print "Right: " +  str(tree.right.val)
        return tree.right 
    
    if tree.val>maxVal:
    	if tree.left == None:
    		print "None"
    	else:
    		print "Left: " +  str(tree.left.val) 
        return tree.left

def levelOrderPrint(tree):
	l = [tree]
	s = ""
	while True:
		nl = []
		i = 0
		while i < len(l):
			s += str(l[i].val) + " "
			if l[i].left != None:
				nl.append(l[i].left)
			if l[i].right != None:
				nl.append(l[i].right)
			i += 1
		if nl != []:
			l = nl
		else:
			break
		s += '\n'
	return s

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

#a.postorder()

new = trimBST(a,5,13)
new.postorder()