class Animal:
    def make_sound(self):
        print("Some sound")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Meow")

cat = Cat()
cat.make_sound()
