### 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

### 2
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
### 3
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")
    
    def get_balance(self):
        print(f"Current balance: ${self.balance}")

### 4
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def is_long(self):
        return self.pages > 300
    
### 5
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
### 6
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)
    
### 7
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def age(self, current_year):
        return current_year - self.year
    
### 8
class Flight:
    def __init__(self, airline, duration):
        self.airline = airline
        self.duration = duration
    
    def convert_duration(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return f"{hours} hours {minutes} minutes"
    
### 9
class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        return "Generic animal sound"
    
class Dog(Animal):
    def make_sound(self):
        return "Bark"
    
### 10
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def vehicle_info(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def vehicle_info(self):
        return f"{self.brand} {self.model} (Battery capacity: {self.battery_capacity} kWh)"