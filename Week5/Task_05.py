from abc import ABC, abstractmethod

# ---------------------------------------------------------------
# ABSTRACT PARENT CLASS
# ---------------------------------------------------------------
# By inheriting from ABC (Abstract Base Class), this class becomes
# abstract, meaning you CANNOT create an object directly from it.
# e.g., BankAccount("Rahul", 5000) would raise a TypeError.
# It acts as a blueprint that child classes must follow.
class BankAccount(ABC):

    # Constructor: runs automatically when an object is created.
    # 'self' refers to the current object being created.
    def __init__(self, name, balance):
        # Public attribute: can be accessed directly (account1.name)
        self.name = name

        # Private attribute (ENCAPSULATION):
        # The double underscore (__) triggers "name mangling", so Python
        # internally renames it to _BankAccount__balance. This prevents
        # accidental access like account1.__balance from outside the class.
        self.__balance = balance

    # Getter method:
    # Since __balance is private, outside code can't read it directly.
    # This method provides controlled, read-only access to it.
    def get_balance(self):
        return self.__balance

    # Method to modify the balance safely:
    # Instead of letting anyone change the balance directly, we force
    # changes to go through this method, where we can add validation.
    def deposit(self, amount):
        # Validation: only positive amounts are allowed.
        # This protects the data from invalid values (e.g., -500).
        if amount > 0:
            self.__balance += amount   # Allowed: we're inside the class
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount!")

    # Abstract method (ABSTRACTION):
    # This only declares WHAT must be done, not HOW.
    # Every child class is forced to provide its own implementation.
    # If a child class doesn't implement it, Python will raise an error
    # when you try to create an object of that child class.
    @abstractmethod
    def calculate_interest(self):
        pass


# ---------------------------------------------------------------
# CHILD CLASS (INHERITANCE)
# ---------------------------------------------------------------
# SavingsAccount inherits from BankAccount, so it automatically gets:
#   - the __init__ constructor
#   - the name attribute and the private balance
#   - get_balance() and deposit() methods
# It doesn't need to rewrite any of these.
class SavingsAccount(BankAccount):

    # Implementing the abstract method:
    # SavingsAccount provides the actual logic for calculate_interest().
    # Here, savings accounts earn 5% interest on the balance.
    # Note: we use get_balance() because the child class cannot access
    # the parent's private __balance directly.
    def calculate_interest(self):
        interest = self.get_balance() * 0.05   # 5% of the balance
        print("Interest:", interest)


# ---------------------------------------------------------------
# CREATING OBJECTS (INSTANTIATION)
# ---------------------------------------------------------------
# Each object has its own separate name and balance.
# The constructor from BankAccount is used automatically.
account1 = SavingsAccount("Rahul", 10000)
account2 = SavingsAccount("Amit", 20000)

# ---------------------------------------------------------------
# USING THE OBJECTS
# ---------------------------------------------------------------
# Accessing the public attribute directly
print("Account Holder:", account1.name)          # Output: Rahul

# Accessing the private balance through the getter method
print("Balance:", account1.get_balance())        # Output: 10000

# Updating the balance through the deposit method (not directly)
account1.deposit(2000)                           # Output: Amount deposited: 2000
print("Updated Balance:", account1.get_balance())  # Output: 12000

# Calling the method implemented from the abstract method
# 5% of 12000 = 600.0
account1.calculate_interest()                    # Output: Interest: 600.0

# ---------------------------------------------------------------
# SECOND OBJECT
# ---------------------------------------------------------------
# account2 is independent of account1; changes to one
# do not affect the other.
print("\nSecond Account:")
print("Account Holder:", account2.name) 
print("Balance:", account2.get_balance())
account2.calculate_interest()                    