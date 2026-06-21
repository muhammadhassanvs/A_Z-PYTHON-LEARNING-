#if  else condition

age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")  
else:
    print("You are not eligible to vote.")

#else if condition
marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
else:
    print("fail")