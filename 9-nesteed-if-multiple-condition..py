#nested if multiple condition
age=int(input("Enter your age: "))  
if age>=18:
    print("You are eligible to vote.")
    citizenship=input("Are you a citizen? (yes/no): ")
    if citizenship.lower()=="yes":
        print("You can vote in the elections.")
    else:
        print("You cannot vote as you are not a citizen.")
else:
    print("You are not eligible to vote.")


#multiple condition (and)
age=int(input("Enter your age: "))
residency=input("Are you a resident? (yes/no): ")
if age>=18 and residency.lower()=="yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#multiple condition (or)
age=int(input("Enter your age: "))  
residency=input("Are you a resident? (yes/no): ")
if age>=18 or residency.lower()=="yes":
    print("You are eligible to vote.")  
else:    print("You are not eligible to vote.")