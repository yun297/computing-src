class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next # Next node

    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next
        
    def get_next(self): # get_next_node()
        return self.next
    
    def peek(self): # get_next_date()
        return self.next.data # or get_next().get_data()


    # String method for Node() (usually not in quesiton/not required in all questions)
    
    def __str__(self) -> str:
        cls = self.__class__.__name__ # name of the class
        data = self.data # data of the node
        next = self.next
        return f"{cls}({data}, {next})"
    
# new1 = Node("data 1", None) # no next node
# new2 = Node("data 2", new1)

# print(new1)
# print(new2)

class LinkedList:
    def __init__(self):
        self.root = None
        
    def push(self, data):
        new_node = Node(data, self.root) # new node that points to the root
        self.root = new_node # new node is now the new root