#range&loops

#print 1 to 5
for i in range(1,6):
    print(i)

#print even numbers
for i in range(2,11,2):
    print(i)

#countdown from 10 to 1
for i in range(10,0,-1):
    print(i)

#loop though a list usining index
mylist=["apple","banana","cherry"]  
for i in range(len(mylist)):
    print(mylist[i])

#generate employee ids using range
for i in range(1001,1006):
    print("Employee ID:",i) 

#clean city name using loop
cities=["  New York  ","  Los Angeles  ","  Chicago  "] 
for i in range(len(cities)):
    cities[i]=cities[i].strip().title()
print(cities)



#extract last four digits from ids
ids=["EMP1001","EMP1002","EMP1003"]
for i in range(len(ids)):
    print(ids[i][-4:])  


#nested loop

for i in range(1,4):
    for j in range(1,4):
        print(i,j)
