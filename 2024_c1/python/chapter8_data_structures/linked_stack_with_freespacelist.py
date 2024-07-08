# 8.4.6 LinkedStack() with FreeSpaceList

# Example of implementation of stack using a free space list

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
    
class List:
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
    
    def display(self):
        ptr = self.root # pointer starts at root
        while ptr != None: # while the pointer is not at the last node that has no next yet
            print(f"{ptr.get_data()}") # print the data of the node the pointer is at
            ptr = ptr.get_next() # reset pointer to the next node
        print("End of linked list")
                
class Game:
    def __init__(self):
        self.free = List() # free is empty
        self.players = List() # players is empty
        
        for i in range(5):
            self.free.push(f'empty space {i}')
            
    def display(self):
        print("Players: ")
        self.players.display()
        print("\nFree: ")
        self.free.display()

    def join_party(self, name):
        new_node = self.free.root # top node in freespace LL
        self.free.root = self.free.root.get_next()
        new_node.set_data(name) # 
        new_node.set_next(self.players.root)
        self.players.root = new_node
        
    def leave_party(self, name):
        ptr = self.player.root
        prev = None
        while ptr:
            if ptr.get_gata() == name:
                if prev is None: # root of self.player bring removed
                    self.player.root = ptr.get_next()
                    ptr.set_next(self.free.root)
                    ptr.set_data("-")
                    self.free.root = ptr
                    return
                
                else:
                    prev.set_next(ptr.get_next)
                    ptr.set_next(self.free.root)
                    ptr.set_data("-")
                    self.free.root = ptr
                    return
                
            else:
                prev = ptr
                ptr = ptr.get_next()
                
        print(f"{name} not found in party! No players left the party.")
    
game1 = Game()
for i in range(5):
    game1.join_party(f"P{i}")
game1.display()