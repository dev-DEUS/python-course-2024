### 1
numbers = [4, 8, 15, 16, 23]
print(sum(numbers))

### 2
nums = [10, 15, 20, 25, 30]
for num in nums:
    if num % 2 == 0:
        print(num)

### 3
person = {"name": "John", "age": 30, "city": "New York"}
print(person["age"])

### 4
my_set = {5, 12, 7, 20, 3}
for item in my_set:
    if item > 10:
        print(item)

### 5
nums = [3, 1, 4, 1, 5, 9]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print(largest)

### 6
my_tuple = (1, 2, 3, 4)
for item in my_tuple:
    print(item)

### 7
num_set = {2, 4, 6, 8, 10, 3, 5, 7}
for num in num_set:
    if num % 2 == 0:
        print(num)

### 8
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

### 9
fruits = {"apple": 2, "banana": 1, "cherry": 3}
most_expensive = max(fruits, key=fruits.get)
print(most_expensive)

### 10
word = "banana"
letter_count = word.count("a")
print(letter_count)