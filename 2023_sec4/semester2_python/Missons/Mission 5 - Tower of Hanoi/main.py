class Tower():
    def __init__(self) -> None:
        self._disks = []
        
    def push_disk(self, disk) -> None:
        self._disks.append(disk)
        
    def pop_disk(self) -> int:
        return self._disks.pop()
    
    def peek_top_disk(self) -> int:
        return self._disks[-1]
    
    def __str__(self) -> str:
        return str(self._disks)
    
class TowerOfHanoi():
    def __init__(self, n: int) -> None:
        self.__towers = {"A": Tower(), "B": Tower(), "C": Tower()}
        self._n = n
        self._step = 1
    
    def get_tower(self, name: str):
        return self._towers[name]

    def get_n(self) -> int:
        return self._n
    
    def get_step(self) -> int:
        return self._step

    def reset_step(self) -> None:
        self._step = 1
    
    def reset_towers(self) -> None:
        self._towers = {"A": Tower(), "B": Tower(), "C": Tower()}
        self._towers["A"]._disks = [i for i in range(self._n, 0, -1)]
        
    def print_towers(self) -> None:
        for name, tower in self._towers.items():
            print(f"{name}: {tower}")
    
    def check_win(self):
        return len(self._towers["C"]._disks) == self._n or len(self._towers["B"]._disks) == self._n
    
    def move_disk(self, src: str, dst: str) -> None:
        # Check if src tower is empty
        if len(self._towers[src]._disks) == 0:
            print(f"Error: {src} tower is empty. Cannot move disk from {src} to {dst}!")
            return

        # Move disk
        self._towers[dst].push_disk(self._towers[src].pop_disk())
        self.print_towers()

        # Check for a win condition
        if self.check_win():
            print(f"Congrats! You have completed the game in {self._step} steps!")
            self.reset_step()
            self.reset_towers()
            return

        self._step += 1 # Increment the step counter
        
    def solve(self):
        self.reset_towers()
        print(f"Solving for {self._n} disks...")
        print("Initial state:")
        self.print_towers()

        # Call the recursive function to solve the Tower of Hanoi problem
        self.solve_recursive(self._n, "A", "C", "B")
        
        print(f"Optimal steps expected (2^{self._n} - 1) = {2**self._n - 1} steps")

    def solve_recursive(self, n, source, target, auxiliary):
        if n == 1:
            # Base case: Move the top disk from source to target
            print(f"Step {self.get_step()}:")
            self.move_disk(source, target)
        else:
            # Move n-1 disks from source to auxiliary using target as auxiliary peg
            self.solve_recursive(n - 1, source, auxiliary, target)

            # Move the nth disk from source to target
            print(f"Step {self.get_step()}:")
            self.move_disk(source, target)

            # Move the n-1 disks from auxiliary to target using source as auxiliary peg
            self.solve_recursive(n - 1, auxiliary, target, source)


def main():
    n = int(input("Enter number of disks: "))
    game = TowerOfHanoi(n)
    game.solve()

main()