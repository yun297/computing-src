class TreeNode:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left = left # left child
        self.right = right # right child

class BSTree:
    def __init__(self, root = None) -> None:
        self.root = root

    def insert(self, root, item): # RECURSIVE insert
        if root is None: # inserting into empty tree
            self.root = TreeNode(item)

        elif item < root.data: # new item < root of SUBTREE

            if root.left: # if root.left has a SUBTREE
                self.insert(root.left, item) # traverse to the left
                # recursive stage, only can continue after recusion is done
            
            else: # space to insert on left
                root.left = TreeNode(item)
        
        else: # new item > root of SUBTREE

            if root.right: # if root.right has a SUBTREE
                self.insert(root.right, item) # traverse to the right
            
            else: # space to insert on the right
                root.right = TreeNode(item)

        return # returns None
    
    def finder(self, current, target, parent): # current takes in self.root from delete function
        if current is None:
            return None, None # tree is empty
        
        elif current.data == target:
            return current, None # if root is target, then it has no parent
        
        elif target < current.data:
            return self.finder(current.left, target, current) # current shifts down to the left, current becomes the new parent
        
        else:
            return self.finder(current.right, target, current) #  current shifts down to the right, current becomes the new parent
            
    
    def delete(self, target):
        current, parent = self.finder(self.root, target, None) # find the delete target and its parent using finder() helper function first
        
        if (current.left is None) and (current.right is None): # case 1: current has no child (i.e. leaf node)
            if parent is None: # one singular node
                self.root = None # entire tree is empty
                
            elif current == parent.left: # current child is left child relative to parent
                parent.left == None
                
            elif current == parent.right: # current child is right child relative to parentn
                parent.right == None
                
        elif (current.left is None) or (current.right is None): # case 2: current has 1 child 
            # if both child is None, technically this if statement is still true, but the above if statement already handles the case of both child being None
            
            # find the successor
            if current.left: # current has a left child (no right child because it has 1 child)
                successor = current.left
                
            else: # current has a right chiild
                successor = current.right
            
            
            # determine if successor is a left child or right child
            if parent is None: # no parent
                self.root = successor
                
            elif current == parent.left: # current child is left child relative to parent
                parent.left == successor    
                
            elif current == parent.right: # current child is right child relative to parent
                parent.right == successor
                
        else: # case 3: current has 2 children
            # find the successor
            
            successor = current.left # we want LARGEST in the LEFT subtree (we want largest possible node in the subtree that is smaller than the target)
            successor_parent = current # connecting successor's parent to successor child (if any), so that the successor can be promoted
            
            while successor.right: # successor has a right subtree/node (we want the largest in the subtree so we traverse right)
                successor_parent = successor
                successor = successor.right # traverse to the right
                
            # connect successor's parent to successor's child
            # we don't have check if the child is right child because we know we have traversed to the right
            
            if successor_parent != current:
                successor_parent.right = successor.left
                successor.left = current.left # successor node get promoted
                successor.right = current.right
                
            # if successor has no right child but only left child, no need to redefine the left child
            # successor_parent == current when successor is already the biggest number in the left subtree of current
            # i.e. no travesal was completed at all
               
            successor.right = current.right # so in both cases we will redefine the right child
            
            # connect parent to successor
            if parent is None:
                self.root = successor
                
            elif current == parent.left: # current child is left child relative to parent
                parent.left == successor    
                
            elif current == parent.right: # current child is right child relative to parent
                parent.right == successor

    def inorder(self, root): # in numerical order
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
 
    def preorder(self, root): 
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
            
    def count(self, current): # returns number of nodes in a tree
        if current is None: # tree is empty
            return 0
        
        else: # tree is not empty
            left_size = self.count(current.left) # split left subtree again into left and right (recusive)
            right_size = self.coutn(current.right) # split right subtree again into left and right (recursive)
            return left_size + right_size + 1 # + 1 comes from the root of the tree

    def search(self, root, target):
        if not root: # check if tree is empty
            return False
        
        elif root.data is None:
            return False # end of tree reached
        
        elif root.data == target: # target found
            return True

        elif target < root.data: # target smaller, search left subtree
            return self.search(root.left, target)

        else: # target larger, search right subtree
            return self.search(root.right, target)
        

apple_tree = BSTree()
apple_tree.insert(apple_tree.root, 12)
apple_tree.insert(apple_tree.root, 5)
apple_tree.insert(apple_tree.root, 17)
apple_tree.insert(apple_tree.root, 4)
apple_tree.insert(apple_tree.root, 10)
apple_tree.insert(apple_tree.root, 15)
apple_tree.insert(apple_tree.root, 16)
apple_tree.insert(apple_tree.root, 20)

print(apple_tree.search(apple_tree.root, 21))

apple_tree.inorder(apple_tree.root)
print()
apple_tree.preorder(apple_tree.root)
print()
apple_tree.postorder(apple_tree.root)
