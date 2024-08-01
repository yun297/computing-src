class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.root = None

    def push(self, data = Node()):
        data.next = self.root
        self.root = data

    def insert(self, data: Node, position):
        if position == 0:
            self.push(data)
        else:
            count = 0
            ptr = self.root
            while ptr.next is not None:
                if count == position:
                    data.next = ptr.next
                    ptr.next = data
                    return
                else:
                    count += 1
                    ptr = ptr.next
    
    def delete(self, target):
        if self.root is None:
            print("Linked list is empty!")
            return
        else:
            ptr = self.root
            while ptr.next is not None:
                if ptr.next == target:
                    popped_node = ptr.next
                    ptr = ptr.next.next
                    return popped_node
                else:
                    ptr = ptr.next

            print("Target not found, no nodes removed!")
            return
    
class Game:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.data = LinkedList()
        self.free = LinkedList()
        
    def create_party(self):
        for i in range(self.capacity):
            self.free.push()

    def join_party(self, data: Node, position):
        self.free.root = data.data
        self.data.insert(self.free.delete(), position)
        
    def leave_party(self, target):
        self.free.push(self.data.delete(target))