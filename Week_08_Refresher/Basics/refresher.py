# Variables and Data Types
x = 5  # Integer
name = "John"  # String
is_active = True  # Boolean
height = 5.9  # Float

# Lists and Basic Operations
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Accessing the first element
numbers.append(6)  # Adding an element
numbers.remove(3)  # Removing an element

# Math Operations
sum_result = x + 10  # Addition
product_result = x * 2  # Multiplication
division_result = x / 2  # Division
modulo_result = x % 2  # Modulo
print("Sum:", sum_result)
print("Product:", product_result)
print("Division:", division_result)
print("Modulo:", modulo_result)

# Data Structures
# Tuple (immutable list)
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Dictionary (key-value pairs)
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}
print("Student Name:", student["name"])

# Set (collection of unique items)
unique_numbers = {1, 2, 3, 4, 5, 5, 2}  # Duplicates will be removed
unique_numbers.add(6)
unique_numbers.discard(3)
print("Unique Numbers:", unique_numbers)

# Conditional Statements
if x > 3:
    print("x is greater than 3")
elif x == 3:
    print("x is equal to 3")
else:
    print("x is less than 3")

# For Loop
for num in numbers:
    if num == 4:
        continue  # Skip the rest of the loop for this iteration
    if num == 6:
        break  # Exit the loop completely
    print(num)

# While Loop
counter = 0
while counter < 3:
    if counter == 2:
        break  # Exit the loop when counter reaches 2
    print("Counter is", counter)
    counter += 1

# Basic Input/Output
your_name = input("Enter your name: ")
print("Hello,", your_name)