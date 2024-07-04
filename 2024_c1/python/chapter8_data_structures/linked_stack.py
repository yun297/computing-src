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
    
    # def peek(self): # get_next_date()
    #     return self.next.data # or self.get_next().get_data()

class LinkedStack:
    def __init__(self) -> None:
        self.top = None
        self.length = 0
    
    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node
        self.length += 1
    
    def pop(self):
        if self.top == None:
            print("Error! Stack is empty.")
            return
        else:
            ret = self.top.get_data() # store data of node being popped
            self.top = self.top.get_next()
            return ret # return data of popped node, like how .pop() returns when used on a list
    
    def len(self):
        return self.length
    
jenga = LinkedStack()

for char in "ABCDE":
    jenga.push(char)

for i in range(6):
    print(jenga.pop())