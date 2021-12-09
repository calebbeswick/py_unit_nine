class Dog:

    def __init__(self, name,):
        self.name = name
        self.trick_list = []


    def get_name(self):
        return self.name

    def sit(self):
        print(self.name + " sits")
        self.trick_list.append("Sits")


    def roll_over(self):
        print(self.name + " rolls over")
        self.trick_list("Rolls over")

    def jump(self):
        print(self.name + " jumps")
        self.trick_list.append("Jumps")

    def print_trick_list(self):
        if len(self.trick_list) == 0:
            print(self.name + " does not know any tricks")
        for tricks in self.trick_list:
            print()


