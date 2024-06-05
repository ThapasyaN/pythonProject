# CLASS INHERITANCE- the process of inheriting the behaviour and appearance from an existing class.

# to inherit the class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        # to inherit the method
        super().breath()
        print("doing this in water")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)
