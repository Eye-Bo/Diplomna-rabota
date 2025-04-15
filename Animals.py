class Animal:

    def make_sound(self):
        pass # Дефинираме интерфейс
class Dog (Animal):
    def make_sound(self):
        return "Bay!"
class Cat (Animal):
    def make_sound(self): return "May!"
class Parrot (Animal):
    def make_sound(self): return " I'm not a bird, birds don't talk!"

animals = [Dog(), Cat(), Parrot()]
for animal in animals:
    print (animal.make_sound()) # bay! Mяy!