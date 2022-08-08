class Dog:
    def __init__(self,animal):
        self.animal = animal

    def voice(self):
        print(f"{self.animal} : Gaf Gaf Gaf")

dog = Dog('Dog')
dog.voice()


class Bear:
    def __init__(self, animal):
        self.animal = animal

    def voice(self):
        print(f"{self.animal} : GRRRRR GRRRRR GRRRRR")

bear = Bear('Bear')
bear.voice()


class Cow:
    def __init__(self, animal):
        self.animal = animal

    def voice(self):
        print(f"{self.animal} : Moo Moo Moo")


cow = Cow('Cow')
cow.voice()


class Cat:
    def __init__(self, animal):
        self.animal = animal

    def voice(self):
        print(f"{self.animal} : Meow Meow Meow")


cat = Cat('Cat')
cat.voice()


