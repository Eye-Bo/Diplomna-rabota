class Animal:

    def make_sound(self):
        pass # Дефинираме интерфейс
class Dog (Animal):
    def make_sound(self):
        return "Bay!"
    def fetch(self):
        return "The dog fetched a stick."
    def describe(self):
        return "The dog is a domesticated descendant of the gray wolf. " \
        "Also called the domestic dog, it was selectively bred from an extinct population of wolves during the Late Pleistocene by hunter-gatherers. " \
        "The dog was the first species to be domesticated by humans, over 14,000 years ago and before the development of agriculture."
class Cat (Animal):
    def make_sound(self): return "May!"
    def purr(self): return "The cat purred."
    def describe(self):
        return "The cat, also referred to as the domestic cat or house cat, is a small domesticated carnivorous mammal. " \
        "It is the only domesticated species of the family Felidae. " \
        "Advances in archaeology and genetics have shown that the domestication of the cat occurred in the Near East around 7500 BC."
class Parrot (Animal):
    def make_sound(self): return " I'm not a bird, birds don't talk!"
    def fly(self):return "The parrot flied."
    def describe(self):
        return "Parrots, also known as psittacines, are birds with a strong curved beak, upright stance, and clawed feet. " \
        "They are classified in four families that contain roughly 410 species in 101 genera, found mostly in tropical and subtropical regions."

animals = [Dog(), Cat(), Parrot()]
for animal in animals:
    print (animal.make_sound()) # bay! Mяy!