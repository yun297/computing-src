class TreeNode:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left = left # left child
        self.right = right # right child
    
    # we will not use setters/getters for data/left/right as they are messy

    # binary search is an efficient algorithm for finding a target value in a sorted list by repeatedly dividing the search interval in half. Starting with the middle element, it compares the target to this element, and if they are not equal, it narrows the search to the left or right half of the list based on whether the target is smaller or larger. This process continues until the target is found or the search range is empty,

    # left child is smaller than right child in a BST

class BSTree:
    def __init__(self, root = None) -> None:
        self.root = root

    def insert(self, new_data):
        new_node = TreeNode(new_data)
        if self.root == None:
            self.root == new_node
            return
        
        # travesal
        inserted = False
        ptr = self.root

        while not inserted: # while inserted is False, while loop will continue to run
            if new_data > ptr.data: # belongs to right side subtree

                if ptr.right is None: # if right side is empty
                    ptr.right = new_node # insert as right child
                    inserted = True # stops the while loop
                else:
                    ptr = ptr.right # shift pointer to the right child
            
            else: # belongs to the left side subtree

                if ptr.left is None:
                    ptr.left = new_node
                    inserted = True
                else:
                    ptr = ptr.left # shift pointer to the left child
    
    def search(self, target):
        ptr = self.root
        while ptr: # while ptr is not None
            if ptr.data == target: # target found
                return True
            
            elif ptr.data is None: # reached the end of the tree
                return False
            
            elif ptr.data < target: # search towards left subtree
                ptr = ptr.left
                
            else: # search towards the right subtree
                ptr = ptr.right
