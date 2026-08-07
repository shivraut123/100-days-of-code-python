# Class inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Breathing under Water")


    def swim(self):
        print("Swimming")

salmon = Fish()
salmon.breathe()
salmon.swim()

