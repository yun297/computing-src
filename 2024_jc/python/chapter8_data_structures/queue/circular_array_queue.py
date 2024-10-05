class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class ArrayQueueC:
    CAPACITY = 16

    def __init__(self) -> None:
        self.data = [''] * ArrayQueueC.CAPACITY
        self.tail = -1
        self.head = -1

    def enqueue(self, data):
        # temp = (self.head - 1) % ArrayQueueC.CAPACITY # when the queue is full, head is at 1 position above 
        if self.head == -1: # if queue is empty
            self.tail = 0
            self.head = 0
            self.data[self.tail] = data

        elif self.head == (self.tail + 1) % ArrayQueueC.CAPACITY: # if queue is full
            # when queue is full, tail will loop back around and be behind of head
            # head index is 0, tail index has to be 15
            # when you enqueue 1 more item, tail index becomes 16, 16 % 16 = 0 = head index
            # so the queue is full
            print("queue is full!")
            return

        else: # queue is not full
            self.tail += 1
            self.tail %= ArrayQueueC.CAPACITY
            # since this is a CIRCULAR QUEUE, have to mod bu capacity else tail will go out of range
            # for example, if i have 16 items already, and I store one more, it will WRAP around and replace the first item in the queue (i.e. mod(16) = 0, replaces the first item in index 0)

            self.data[self.tail] = data # store data in corresponding index
            return
    
    def display(self):
        # big brain math way
        if self.tail < self.head:
            for i in range(self.head, self.tail + 1 + ArrayQueueC.CAPACITY): # + capacity so that tail runs in chronological order after head
                print(self.data[i % ArrayQueueC.CAPACITY]) # mod 16 to jumb back before head to print corresponding items
        else:
            for i in range(self.head, self.tail + 1):
                print(self.data[i])

    def display2(self):
        if self.tail < self.head: # tail has wrapped around behind head
            for i in range(self.head, ArrayQueueC.CAPACITY): # run from head to end of queue first
                print(self.data[i])
            
            # run from tail to head (remaining section)
            for i in range(0, self.tail + 1):
                print(self.data[i])
        
        else: # normal case just runs from head to tail
            for i in range(self.head, self.tail + 1):
                print(self.data[i])

    def dequeue(self): # dequeue from the head
        ret = self.data[self.head] # store return value from head
        
        if self.head == -1: # if queue is empty, nothing to dequeue
            print("queue is empty")
            return
        
        elif self.head == self.tail: # one item left
            self.head = -1 # empty state
            self.tail = -1 # empty state
        
        elif self.head == ArrayQueueC.CAPACITY - 1: # if head is at the end
            self.head = 0 # reset position of head to 0 (first item)
            # the item in the previous head position can be ignored as it won't be displayed and it will be replaced when more items are enqueued
        
        else: # default case
            self.head += 1 # move head forward, item in original spot can be ignored

        return ret # if something is dequeued, just return the return value
    
# test

merry_go_round = ArrayQueueC()

for i in range(merry_go_round.CAPACITY - 3):
    merry_go_round.enqueue(f"child {i}")

merry_go_round.dequeue()
merry_go_round.enqueue("new")
merry_go_round.dequeue()
merry_go_round.enqueue("hi")
merry_go_round.display()