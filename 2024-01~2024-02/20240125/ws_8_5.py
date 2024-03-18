
class Dog():
    sound = "멍멍"
    def __init__(self):
        self.sound = Dog.sound

class Cat():
    sound = "야옹"
    def __init__(self):
        self.sound = Cat.sound

class Pet(Cat, Dog):

    def __str__(self):
        return f"애완동물은 {self.sound} 소리를 냅니다."

pet1 = Pet()
print(pet1)
