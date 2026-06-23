security_code=int(input("Enter your security code: "))
if security_code==1234:
    department=input("enter your department: ")
    if department.lower()=="hr":
        access_level=int(input("enter your access level (1-10): "))
        if access_level>=5:
            print("You have full access to the HR department.")
        else:
            print("insufficient access level. You have limited access to the HR department.")    
    else:
        print("You do not have access to this department.")
else:
    print("Invalid security code. Access denied.")
