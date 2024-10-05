class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

    # read question on whether setter and getter is needed

class LinkedQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0

    def enqueue(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.len += 1

        return

    def dequeue(self):
        if self.head is not None:
            target = self.head

        
            if self.head.next is None: # when there is one item left in queue
                self.tail = None
                self.head = None

            else: # more than one item left in queue
                self.head = self.head.next # skip this item

            self.len -= 1

            return target.data
        
        print("Queue is empty!")
        return # if queue is empty, just return nothing
    
    def display(self):
        ptr = self.head

        while ptr: # while ptr is not None
            print(ptr.data)
            ptr = ptr.next # shift pointer to the next node

        print("End of queue!")

    def __len__(self):
        return self.len


canteen = LinkedQueue()

canteen.enqueue("first")
canteen.enqueue("second")
canteen.enqueue("third")

# print(canteen.dequeue())
# print(canteen.dequeue())
# print(canteen.dequeue())

canteen.display()

print(len(canteen))