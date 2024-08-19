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
        
        if current.data == target:
            return current, None # if root is target, then it has no parent
        
        elif target < current.data:
            return self.finder(current.left, target, current) # current shifts down to the left, current becomes the new parent
        
        else:
            return self.finder(current.right, target, current) #  current shifts down to the right, current becomes the new parent
            
    
    def delete(self, target):
        current, parent = self.finder(self.root, target)
        # delete current
        # connect parent to successor

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
