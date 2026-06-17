#arithametic operators
a=10
b=5
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication 
print("Division:", a / b)          # Division
print("Modulus:", a % b)           # Modulus
print("Exponentiation:", a ** b)   # Exponentiation
print("Floor Division:", a // b)    # Floor Division


#assignment operators
x = 5
print("Initial value of x:", x)
x += 3  # Equivalent to x = x + 3
print("After addition assignment (x += 3):", x)
x -= 2  # Equivalent to x = x - 2
print("After subtraction assignment (x -= 2):", x)
x *= 4  # Equivalent to x = x * 4
print("After multiplication assignment (x *= 4):", x)
x /= 2  # Equivalent to x = x / 2
print("After division assignment (x /= 2):", x)
x %= 3  # Equivalent to x = x % 3
print("After modulus assignment (x %= 3):", x)
x **= 2  # Equivalent to x = x ** 2
print("After exponentiation assignment (x **= 2):", x)



#comparison operators
a = 10
b = 5
print("Is a equal to b?", a == b)           # Equal to
print("Is a not equal to b?", a != b)       # Not equal to
print("Is a greater than b?", a > b)        # Greater than
print("Is a less than b?", a < b)           # Less than
print("Is a greater than or equal to b?", a >= b)  # Greater than or equal to
print("Is a less than or equal to b?", a <= b)     # Less than or equal to



#logical operators
x1=5
y1=10
print("Logical AND (x1 > 0 and y1 > 0):", x1 > 0 and y1 > 0)  # Logical AND
print("Logical OR (x1 > 0 or y1 < 0):", x1 > 0 or y1 < 0)    # Logical OR
print("Logical NOT (not(x1 > 0)):", not(x1 > 0))  # Logical NOT



#identity operators
a1 = [1, 2, 3]
b1 = a1
c1 = [1, 2, 3]
print("Is a1 the same object as b1?", a1 is b1)  # True, because b1 references the same object as a1
print("Is a1 the same object as c1?", a1 is c1)  # False, because c1 is a different object with the same content
print("Is a1 not the same object as c1?", a1 is not c1)  # True, because a1 and c1 are different objects


#membership operators
print("is 'a' in 'apple'?", 'a' in 'apple')  # True, because 'a' is present in 'apple'
print("is 'b' not in 'apple'?", 'b' not in 'apple')  # True, because 'b' is not present in 'apple'


