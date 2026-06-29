# This file contains the codes related to containers
# List
# Use a list when:
# 1. Order matters
# 2. Values may change frequently
# 3. Duplicate values can be there
# 4. You want to use indexing and/or slicing
# marks = []
# marks = [90, 80, 70, 60, 50]
# mixed = [10, 'hello', 3.14, True]
students = ['Alice', 'Bob', 'Charlie', 'David']
# print(students)
# print(students[0])  # Accessing the first element
# # Negative indexing starts from the end of the list
# print(students[-1])  # Accessing the last element
#Iterating using foreach loop
# for student in students:
#     print(student)
# Iterating using index of elements
# for i in range(len(students)):
#     print(students[i])
# Slicing
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[:3])
# print(numbers[2:5])
# print(numbers[1:8:2])
# print(numbers[::-1])
# print(numbers[-2:-4:-1])
# Inserting at the end of a list
# numbers.append(10)
# Inserting in a specific injdex
# numbers.insert(2, 99)  # Inserting at index 2
# Removing values based on value similarity
# numbers.remove(2)
# Deleting by index
# del numbers[3]
# Pop deletes by index and returns the value
# popped = numbers.pop(2)
# List Comprehension
# for x in range(1, 6):
#     print(x**2)
# If-else as shorthand
# x = 11
# print("Even" if x % 2 == 0 else "Odd")
# List comprehension
# squares = [x**2 for x in range(1, 6)]
# print(squares)
# List comprehension with if-else
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [x**2 if x % 2 == 0 else x for x in numbers]
# print(squared_numbers)  # Output: [1, 4, 3, 16, 5]

# Use tuples when 
# 1. order matters
# 2. Values do not change frequently
# 3. Want to represent (mostly) fixed records
point = (10, 20)
# x = [10]
# y = (20,)
# print(type(x))
# print(type(y))
# a, b = point # Tuple unpacking
# Function returns multiple values as tuple
def calculate(a: int, b: int) -> tuple:
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

output = calculate(5, 10)
print(output)  # Output: (15, 50)
print(type(output))  # Output: <class 'tuple'>

