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
        self.length = 0
        
    def push(self, data):
        new_node = Node(data, self.root) # new node that points to the root
        self.root = new_node # new node is now the new root
        self.length += 1
    
    def find(self, target):
        ptr = self.root
        while ptr != None:
            if ptr.get_data == target:
                return True # end immediately when found
            
            else: # not found YET
                ptr = ptr.get_next()
        
        return False # return not found at the end of LL
    
    def insert(self, data, position):
        insert = Node(data)
        if position == 1:
            insert.set_next == self.root
            self.root == insert
            self.length += 1
            
        elif position > 1 and position <= self.length:  # Insert into the middle
            current = self.root
            count = 1
            while count < position - 1:  # Traverse to the node before the insertion point
                current = current.get_next()
                count += 1
            insert.set_next(current.get_next())  # Set the new node's next to current node's next
            current.set_next(insert)  # Set current node's next to the new node
            self.length += 1
        
        else:  # Append to the last position
            current = self.root
            while current.get_next() is not None:  # Traverse to the last node
                current = current.get_next()
            current.set_next(insert)  # Set the new node as the next of the last node
            self.length += 1  
            
            
    
    def remove(self, target):
        curr = self.root
        prev = None
        self.length -= 1
        while curr: # while None works the same way as while False, quits when condition, i.e curr, becomes None
            if curr.get_data() == target:
                if prev == None: # if there is no previous i.e root is being removed
                    self.root = curr.get_next()
                    self.length -= 1
                else:
                    prev.set_next(curr.get_next()) # reset the next of the node before the target to the next node after the target
                    self.length -= 1
                return
            else: # not found yet
                prev = curr
                curr = curr.get_next()
        
    def remove2(self, target): # more compact way using peek which is curr.get_next().get_data()
        curr = self.root
        if curr.get_data() == target:
            self.root = curr.get_next()
            self.length -= 1
            return
        while curr.get_next(): # while None works the same way as while False, quits when condition, i.e curr.get_next(), becomes None
            if curr.peek() == target: # next data = target
                curr.set_next(curr.get_next().get_next())
                self.length -= 1
                return
            else:
                curr = curr.get_next()
        
        print(f"{target} not found, no node removed.")
    
    def display(self):
        ptr = self.root # pointer starts at root
        while ptr != None: # while the pointer is not at the last node that has no next yet
            print(f"{ptr.get_data()}") # print the data of the node the pointer is at
            ptr = ptr.get_next() # reset pointer to the next node
        print("End of linked list")
    
my_list = LinkedList()
my_list.push("Skibidi")
my_list.push("Toilet")
my_list.push("Gyat")
my_list.push("Rizz")

my_list.display()

my_list.remove("Skibidi")
my_list.display()