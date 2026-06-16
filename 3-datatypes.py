#day 3
#types of data types


#text data type

#1-string data type
name = "John"
print("My name is", name)
print("Data type of name:", type(name))


#numeric data types

#1-integer data type
age = 25    
print("My age is", age)
print("Data type of age:", type(age))


#2-float data type
height = 5.9    
print("My height is", height)
print("Data type of height:", type(height))


#3-complex data type
complex_number = 2 + 3j
print("My complex number is:", complex_number)
print("Data type of complex_number:", type(complex_number))


#boolean data type
is_student = True   
print("Am I a student?", is_student)
print("Data type of is_student:", type(is_student))

#sequence data types

#1-list data type
fruits = ["apple", "banana", "cherry"]
print("My favorite fruits are:", fruits)
print("Data type of fruits:", type(fruits))


#2-tuple data type
coordinates = (10, 20)  
print("My coordinates are:", coordinates)
print("Data type of coordinates:", type(coordinates))


#3-range data type
numbers = range(1, 10)
print("My numbers are:", list(numbers))
print("Data type of numbers:", type(numbers))   


#dictionary data type
person = {"name": "Alice", "age": 30}
print("My person dictionary is:", person)
print("Data type of person:", type(person))


#set data type
unique_numbers = {1, 2, 3,3, 4, 5}#sets do not allow duplicate values, so the duplicate '3' will be ignored
print("My unique numbers are:", unique_numbers)
print("Data type of unique_numbers:", type(unique_numbers))

#none data type
nothing = None  
print("My nothing variable is:", nothing)
print("Data type of nothing:", type(nothing))