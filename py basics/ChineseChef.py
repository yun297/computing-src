from Chef import Chef

class ChineseChef:
    # Lets say the Chinese chef can do all the things a normal chef can do

    # Instead of just copying everything on the other file, we can inherit the function from the chef class (by doing from Chef import Chef)

    def make_special_dish(self):
        print("They chef makes orange chicken") # Overwriting the original Chef attribute of making special dish

    def make_fried_rice(self):
        print("The chef makes fried rice")