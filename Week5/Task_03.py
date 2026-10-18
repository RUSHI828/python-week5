# Parent/Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Common method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child/Derived class
class Student(Person):
    def __init__(self, name, age, roll_no, branch):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.branch = branch

    # Specific method of Student class
    def display_student(self):
        self.display()  # Inherited method
        print("Roll Number:", self.roll_no)
        print("Branch:", self.branch)


# Create objects
s1 = Student("Rahul", 18, 1, "AIML")
s2 = Student("Amit", 19, 2, "Computer Engineering")

# Display information
print("Student 1 Details:")
s1.display_student()

print("\nStudent 2 Details:")
s2.display_student()