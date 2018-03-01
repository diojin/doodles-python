class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.current = None
    def preorder(self, node):
        if node:
            print(node)
            self.preorder(node.left)
            self.preorder(node.right)
    def preorder_stack(self, node):
        '''Preorder traverse implemented by stack'''
        cur = node
        # Using Lists as Stacks
        stack = []
        # mimic do while statement
        while True :
            if cur:
                print(cur)
                stack.append(cur)
                while cur.left :
                    print(cur.left)
                    stack.append(cur.left)
                    cur = cur.left
            cur = stack.pop()
            if cur :
                cur = cur.right

            if not ( len(stack) > 0 or cur ):
                break

    def preorder_stack_elegant(self, node):
        '''Preorder traverse implemented by stack in a more natural way'''
        stack = []
        cur = node
        stack.append(cur)
        while len(stack)>0 :
            cur = stack.pop()
            if cur:
                print(cur)
                stack.append(cur.right)
                stack.append(cur.left)

    def inorder(self,node):
        if (node):
            self.inorder(node.left)
            print(node)
            self.inorder(node.right)

    def inorder_stack(self, node):
        cur = node
        stack = []
        while len(stack)>0 or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur:
                print(cur)
                cur = cur.right

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node)

    def postorder_stack(self, node):
        visitCount = {}
        stack = []
        cur = node
        while len(stack) > 0 or cur:
            while cur:
                stack.append(cur)
                visitCount[cur]=0
                cur = cur.left
            cur = stack.pop()
            if cur:
                if visitCount[cur] == 0:
                    stack.append(cur)
                    visitCount[cur]=1
                    cur=cur.right
                else:
                    print(cur)
                    cur = None
        
class Tree:
    def __init__(self, root):
        self.root = root
        self.current = None

class Forest(Tree):
    def __init__(self, root):
        Tree.__init__(self, root)  

class Node:
    def __init__(self, data):
        self.data = data
    def __cmp__(self, other):
        return cmp(self.data, other.data)
    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("incompatible type")
        return self.data < other.data
    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("incompatible type")
        return self.data > other.data
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("incompatible type")
        return self.data == other.data
    def __str__(self):
        return str(self.data)  # int is not implicitly convert to string
    # this hashcode is simplified one, inaccurate if there are same data Nodes
    def __hash__(self):
        return self.data.__hash__()
    
    # define 2 optional operators, ge,le
    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("incompatible type")
        return self.data >= other.data
    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("incompatible type")
        return self.data <= other.data

class BinaryTreeNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
    def __init__(self, data, left=None, right=None):
        Node.__init__(self, data)
        self.left = left
        self.right = right

class TreeNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
    def __init__(self, data, firstChild=None, rightBrother=None):
        Node.__init__(self, data)
        self.firstChild = firstChild
        self.rightBrother = rightBrother

# test data is defined here

#The structure of binaryTree is:
#                                   83
#                           /               \
#                   9                               20
#            /       \ 
#       10               25 

binaryTree = BinaryTree(
    BinaryTreeNode(83, 
      BinaryTreeNode(9, BinaryTreeNode(10), BinaryTreeNode(25)),
      BinaryTreeNode(20)))

print("Binary Tree preorder traverse")
binaryTree.preorder(binaryTree.root)
print("Binary Tree preorder traverse via stack")
binaryTree.preorder_stack(binaryTree.root)
print("Binary Tree preorder traverse via stack more elegant")
binaryTree.preorder_stack_elegant(binaryTree.root)

print("Binary Tree inorder traverse")
binaryTree.inorder(binaryTree.root)
print("Binary Tree inorder traverse via stack")
binaryTree.inorder_stack(binaryTree.root)

print("Binary Tree postorder traverse")
binaryTree.postorder(binaryTree.root)
print("Binary Tree postorder traverse via stack")
binaryTree.postorder_stack(binaryTree.root)

#The structure of tree is:
#                                   83                                                          
#                           /       |       \                                           
#                   9               5               20                      
#            /       \                                              
#       10               25   

tree = Tree(
      TreeNode( 83, 
          TreeNode(9, 
              TreeNode(10, None, TreeNode(25)), 
              TreeNode(5, None, TreeNode(20))), 
          None           
      )       
)   

#The structure of forest is:
#                                   83                                                              86
#                           /       |       \                                               /         |     \
#                   9               5               20                          10              7           24
#            /       \                                               /        \
#       10               25                                  11                     1

forest = Forest(
      TreeNode( 83, 
          TreeNode(9, 
              TreeNode(10, None, TreeNode(25)), 
              TreeNode(5, None, TreeNode(20))), 
          TreeNode(86, 
              TreeNode(10,
                  TreeNode(11,None,TreeNode(1)),
                  TreeNode(7,None,TreeNode(24))),
              None)
      )       
)


