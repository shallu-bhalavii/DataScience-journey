# Day 2: Python Data Structures Practice

# 1. List example  (ordered, allows duplicate,changeable)mutable
fruits = ["apple", "banana", "cherry",2,True, 3.14]
fruits.append("mango")
print("List of fruits:", fruits)
print(fruits[0])


# 2. Tuple example  (ordered,immutable,allows duplicate )
coordinates = (10, 20, True, "x")
print("Coordinates:", coordinates)
print(coordinates[1])


# 3. Set example    (unordered,changeable, no duplicate members and cannot accesed with index)
unique_numbers = {1, 2, 3, 3, 2,True,'r'}
print("Unique numbers:", unique_numbers)
# print(unique_numbers[3])  #error

# 4. Dictionary example (ordered,mutable and can't have duplicate key❌ bt value✔️)
student = {"name": "Shallu", "age": 20, "course": "Data Science"}
print("Student Info:", student)
print(student["age"])  #dictionary access by key not index
