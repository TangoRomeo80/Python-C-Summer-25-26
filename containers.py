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
# def calculate(a: int, b: int) -> tuple:
#     sum_result = a + b
#     product_result = a * b
#     return sum_result, product_result

# output = calculate(5, 10)
# print(output)  # Output: (15, 50)
# print(type(output))  # Output: <class 'tuple'>

# We can mutate a mutable object in an immutable object
# data = ([1, 2], [3, 4])
# data[1].append(5)
# print(data)
# data = [(1, 2), (3, 4)]
# # data.append((5, 6))
# data[1] = (3, 4, 5)
# print(data)

# Use set when:
# 1. Duplicate should not be there
# 2. Order does not matter
# 3. Mathematical set operations are needed
# 4. Fast membership checking is required

# unique_numbers = {1, 2, 3, 4, 5}
# unique_ids = {} # This is not a set, it's a dictionary.
# unique_ids = set() # This is a set.
marks = [80, 85, 80, 90, 90, 95, 92, 92, 98, 80, 86]
unique_marks = set(marks)
# print(unique_numbers)
# print(unique_marks)
# unique_marks.add(100)  # Adding a new value
# print(unique_marks)
# unique_marks.remove(85)  # Removing a value
# unique_marks.discard(86) # Discarding a value (no error if not present)
# print(unique_marks)
# print(86 in unique_marks)  # Membership checking

# ds_students = {'Alice', 'Bob', 'Charlie', 'David'}
# club_members = {'Charlie', 'David', 'Eve', 'Frank'}
# print(ds_students.union(club_members))  # Union
# print(ds_students | club_members)  # Union using operator
# print(ds_students.intersection(club_members))  # Intersection
# print(ds_students & club_members)  # Intersection using operator
# print(ds_students.difference(club_members))  # Difference
# print(ds_students - club_members)  # Difference using operator
# print(ds_students.symmetric_difference(club_members))  # Symmetric Difference
# print(ds_students ^ club_members)  # Symmetric Difference using operator

# Set can only contain immutable objects
# mixed_set = {1, (3, 4), 'hello'} # This is valid
# mixed_set = {1, [3, 4], 'hello'} # This is invalid

# Use a dictionary when:
# 1. you want to associate keys with values
# 2. You need fast lookups by key
# 3. You want to store data in a structured way
test = {}
student ={
    "id": 1,
    "name": "Alice",
    "age": 20,
    'department': 'Computer Science'
}
# # print(student["name"])
# print(student.get('cgpa', 'Key not available'))
# student['cgpa'] = 3.8  # Adding a new key-value pair
# student['age'] = 21  # Updating an existing key-value pair
# print(student)
# student.pop('department')  # Removing a key-value pair
# print(student)
# for key in student:
#     print(f"{key}: {student[key]}")
# student.items()  # Returns a view of key-value pairs
# for key, value in student.items():
#     print(f"{key}: {value}")
