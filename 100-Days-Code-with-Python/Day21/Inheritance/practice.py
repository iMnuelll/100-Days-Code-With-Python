class Animal :
    def __init__(self) :
        self.num_eyes = 2
    
    def breathe(self) :
        print("Inhale and exhale")

class Dog(Animal) :
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("outside the water")
    
    def roar(self):
        print("Woof!")
    
dog = Dog()
dog.breathe()

print(dog.num_eyes)