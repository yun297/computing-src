class StaticArray:
    def __init__(self, capacity) -> None:
        self.data = [''] * capacity
        self.logical_size = 0
        self.physical_size = capacity
        
    def push(self, data):
        if self.logical_size == self.physical_size:
            print("Array is full, no nodes inserted!")
            return
        
        else:
            for i in range(self.logical_size - 1, -1, -1):
                self.data[i + 1] = self.data[i]
            
            self.data[0] = data
            self.logical_size += 1
            return
    
    def insert(self, data, position):
        if self.logical_size == self.physical_size:
            print("Array is full! No nodes inserted!")
            return
        
        else:
            for i in range(self.logical_size - 1, position - 1, -1):
                self.data[i + 1] = self.data[i]
                
            self.data[position] = data
            self.logical_size += 1
            return
            
    def delete(self, target):
        if self.logical_size == 0:
            print("Array is empty, no nodes deleted!")
            return
        else:
            deleted_data = self.data[target]
            for i in range(target, self.logical_size):
                self.data[i] = self.data[i + 1]
                
            return deleted_data
        
    def display(self):
        print(self.data)
        
array1 = StaticArray(5)
array1.push("1")
array1.push("2")
array1.push("3")
array1.display()
array1.insert("A", 2)
array1.display()
array1.delete(2)
array1.display()