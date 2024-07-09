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
            self.length -= 1
            return ret # return data of popped node, like how .pop() returns when used on a list
    
    def len(self):
        return self.length
    
    def display(self):
        ptr = self.top # pointer starts at root
        while ptr != None: # while the pointer is not at the last node that has no next yet
            print(f"{ptr.get_data()}") # print the data of the node the pointer is at
            ptr = ptr.get_next() # reset pointer to the next node
        print("End of linked list")
    
def brackets(exp):
    stack = LinkedStack()
    for char in exp:
        if char in "([{":
            stack.push(char)
            # print(f"pushed {char}")
            
        elif char in ")]}": # if a close bracket is passed in, we have to check the top of the stack for the corresponding open bracket
            
            if stack.len() == 0: # if the stack is empty, there is no brackets to match
                print("Closing bracket without opening!")
                return False
            
            open = stack.pop() # store the open bracket
            # print(f"popped {open}")
            
            if open == "{": # check if open bracket popped from the stack matches
                if char != "}": # the close bracket passed
                    return False
            
            if open == "[":
                if char != "]":
                    return False
            
            if open == "(":
                if char != ")":
                    return False
                
    stack.display()
    print(stack.len())
    # brackets might still be in stack that hasn't been popped, so we need to check
    if stack.len() == 0: # stack is empty
        return True # if all characters in exp are iterated through and no False was rerturned, exp is valid
    
    else:
        return False

if brackets("[(2+3)-5]"):
    print("Valid")