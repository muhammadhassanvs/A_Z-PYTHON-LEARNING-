#input function and typecasting


name = input("Enter your name: ")
print("welcome",name)

print("+----------------------------------------------+")
print("| Employee Name:  ",name,"        |")

#input will always take the input as a string data type

#typecating mean changing the data type of a variable to another data type
age =int( input("Enter your age: "))
age+=3
print("your age is",age)
print(type(age))


#concvert number to string
sales=50000
total="Total sales is "+str(sales)
print(total)


#assignment of today's session

employee_name = str(input("Enter employee name: "))
basic_salary = int(input("Enter basic salary: "))
bonus_amount = int(input("Enter bonus amount: "))
tax_percentage = float(input("Enter tax percentage: "))

gross_salary = basic_salary + bonus_amount
tax_amount = (tax_percentage / 100) * gross_salary
net_salary = gross_salary - tax_amount

print("+----------------------------------------------+")
print("| Employee Name:  ", employee_name  ,)
print("| Basic Salary:  ", basic_salary    ,)
print("| Bonus Amount:  ", bonus_amount    ,)
print("| Tax Percentage:  ", tax_percentage,)
print("| Gross Salary:  ", gross_salary    ,)
print("| Tax Amount:  ", tax_amount        ,)
print("| Net Salary:  ", net_salary        ,)
print("+----------------------------------------------+")