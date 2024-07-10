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
            self.length -= 1
            self.top = self.top.get_next()
            return ret # return data of popped node, like how .pop() returns when used on a list
    
    def len(self):
        return self.length
    
    def display(self):
        ptr = self.top # pointer starts at root
        while ptr != None: # while the pointer is not at the last node that has no next yet
            print(f"{ptr.get_data()}") # print the data of the node the pointer is at
            ptr = ptr.get_next() # reset pointer to the next node
        print("End of linked list")
        
def infix_to_postfix(infix):
    stack = LinkedStack()
    postfix = ""
    for char in infix:
        if char in "+-*/":
            stack.push(char)
            
        elif char == "(":
            stack.push(char)
            
        elif char == ")":
            while stack.len() != 0:
                stack.peek
                pop = stack.pop()
                if pop != "(":
                    postfix += pop
        
        else:
            postfix += char
            print(postfix)
            
    return postfix

infix_to_postfix("3*(a+b)–c*d")