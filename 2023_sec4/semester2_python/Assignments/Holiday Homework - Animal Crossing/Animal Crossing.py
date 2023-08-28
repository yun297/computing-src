# Task 1.1

class AC_Object:
    def __init__(self, name: str, symbol: str, o_type: str = None) -> None:
        self._name = name
        self._symbol = symbol
        self._o_type = o_type
        self._coordinate = None
    
    # Accessor
    def get_name(self) -> str:
        return self._name
    
    def get_symbol(self) -> str:
        return self._symbol
    
    def get_o_type(self) -> str:
        return self._o_type
    
    def get_coordinate(self) -> tuple:
        return self._coordinate
    
    def __str__(self) -> str:
        return self._symbol
    
class Plant(AC_Object):
    def __init__(self, name: str, o_type: str, symbol: str, days_to_mature: int) -> None:
        super().__init__(name, symbol, o_type)
        self._days_to_mature = days_to_mature
        self._day_timer = 0
    
    # Accessor
    
    def pass_one_day(self) -> None:
        self._day_timer += 1
        
    def check_mature(self) -> bool:
        return self._day_timer >= self._days_to_mature
    
    def mature(self) -> None:
        if self.check_mature():
            return None

        if self.get_o_type() == "flower":
            self._symbol = "¥"
            return None

        if self.get_o_type() == "tree":
            self._symbol = "Y"
            return None
            
# Task 1.2
class Map:
    def __init__(self, max_row: int, max_col: int) -> None:
        self._map = [[None for i in range(max_col)] for j in range(max_row)]
        self._max_row = max_row
        self._max_col = max_col
        
    def add_new_obj(self, new_object: AC_Object, row: int, col: int):
        if row >= self._max_row or col >= self._max_col:
            print("Invalid position")
            
        elif self._map[row][col] != None:
            print("Unable to add object. The position is occupied by {}".format(self._map[row][col]))
            
        elif new_object.get_o_type() == "tree":
            # Check if the specified position and its surroundings are empty
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if not (0 <= i < self._max_row and 0 <= j < self._max_col):
                        continue  # Skip out-of-bounds positions
                    if self._map[i][j] != None:
                        print("Unable to add object. The position is occupied by {}".format(self._map[i][j]))
                        return
            # All positions are empty, so add the tree
            self._map[row][col] = new_object
            new_object._coordinate = (row, col)
        else:
            self._map[row][col] = new_object
            new_object._coordinate = (row, col)

        
    def display(self) -> None:
        print("+{}+".format("-" * self._max_col))
        for row in self._map:
            print("|", end="")
            for col in row:
                if col == None:
                    print(" ", end="")
                else:
                    print(col, end="")
            print("|")
        print("+{}+".format("-" * self._max_col))
    
    def pass_a_day(self) -> None:
        for row in self._map:
            for col in row:
                if col is not None:
                    if isinstance(col, Plant):
                        col.pass_one_day()
                        if col.check_mature():
                            col.mature()
                            if col.get_o_type() == "tree":
                                row_coord, col_coord = col.get_coordinate()
                                
                                # add apple at the left, right and top of tree
                                if col_coord + 1 >= 0:
                                    self.add_new_obj(AC_Object("Apple", "@"), row_coord, col_coord + 1)
                                if col_coord - 1 >= 0:
                                    self.add_new_obj(AC_Object("Apple", "@"), row_coord, col_coord - 1)
                                if row_coord - 1 < self._max_row:
                                    self.add_new_obj(AC_Object("Apple", "@"), row_coord - 1, col_coord)
                                                        
                            elif col.get_o_type() == "flower":
                                # change symbol to ¥
                                col._symbol = "¥"


# Test
m = Map(10, 20)

# Add 5 rock objects
m.add_new_obj(AC_Object("Rock", "*"), 0, 0)
m.add_new_obj(AC_Object("Rock", "*"), 2, 3)
m.add_new_obj(AC_Object("Rock", "*"), 0, 18)
m.add_new_obj(AC_Object("Rock", "*"), 8, 12)

# Attempt to add 1 Tree and 2 flowers
m.add_new_obj(Plant("Apple Tree", "tree", "Y", 4), 4, 5)
m.add_new_obj(Plant("Rose", "flower", "v", 3), 4, 5)
m.add_new_obj(Plant("Lily", "flower", "v", 3), 7, 9)


for i in range(5):
    print("Day {}:".format(i))
    m.display()
    m.pass_a_day()