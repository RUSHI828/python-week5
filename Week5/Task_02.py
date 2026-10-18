# Define a Student class
class Student:
    # Constructor to initialize attributes
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    # Method to display student information
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Branch:", self.branch)
        print("--------------------")


# Create objects with different values
s1 = Student("Rahul", 1, "AIML")
s2 = Student("Amit", 2, "Computer Engineering")

# Access initialized attributes
print("Student 1 Name:", s1.name)
print("Student 2 Name:", s2.name)

# Display complete information
print("\nStudent 1 Details:")
s1.display()

print("Student 2 Details:")
s2.display()