# Dynamic (no size limit)

class ArrayStack:
    def __init__(self) -> None:
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
            return
        
        return self.stack.pop()
    
    def display(self):
        for item in self.stack[::-1]:
            print(item)
        print("End of stack")
        
stack1 = ArrayStack

for i in range(5):
    stack1.push(f"Item {i}")
    
stack1.display()

# Fixed-sized

class ArrayStack:
    CAPACITY = 10
    def __init__(self):
        self.data = [''] * ArrayStack.CAPACITY
        self.top = -1 # same as None

    def push(self,data):
        if self.top == ArrayStack.CAPACITY -1:
            print("Stack is full.")
            return
        else:
            self.top += 1 # add 1 to top shifts the top pointer down in the list
            self.data[self.top] = data # set the next element to data
            return

    def pop(self):
        if self.top == -1:
            return "Stack is empty."
        else:
            ret = self.data[self.top] # shift the pointer up, but element doesn't have to be removed in the context of an ArrayStack
            self.top -= 1
            return ret

    def display(self): # display the stack (qn may want display of array inc. free space)
        if self.top == -1:
            print("stack is empty")
            return
        for item in self.data[self.top::-1]:
            print(item)
        print("end of stack")

staaack = ArrayStack()
staaack.display()
print(staaack.pop())

for i in range(7):
    staaack.push(f"P{i}")
staaack.display()

print()

print(staaack.pop())
print()

staaack.display()

print(staaack.data)