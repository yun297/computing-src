class Train:
    def __init__(self, name, year, pax, seats, lines):
        self._model = name
        self._commission = year
        self._capacity = pax
        self._seating = seats
        self._operation = lines

    def show_details(self):
        print("Model:", self.model)
        print("Year of commission:", self.commission)
        print("Capacity:", self.capacity)
        print("No. of seats:", self.seating)
        print("Lines of Operation:", self.operation)

class Train3(Train):
    def __init__(self, name, year, pax, seats, lines, length):
        super().__init__(name, year, pax, seats, lines)
        self._length = length