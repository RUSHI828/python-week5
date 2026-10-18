

# First class
class Dog:
    def sound(self):
        print("Dog barks: Woof Woof!")

# Second class
class Cat:
    def sound(self):
        print("Cat meows: Meow Meow!")

# Create objects
d1 = Dog()
c1 = Cat()

# Call the same method on different objects
d1.sound()
c1.sound()