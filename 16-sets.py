#sets

fruits={"apple","banana","cherry","apple"}
print(fruits)

#add items
fruits.add("orange")
print(fruits)


#remove items
fruits.remove("banana")
print(fruits)


#set operations
A={1,2,3,4,5}
B={3,4,5,6,7}

#union
print(A|B)
#intersection
print(A&B)
#difference
print(A-B)
#symmetric difference
print(A^B)

#remove duplicates from list
mylist=[1,2,3,4,5,1,2,3]
newlist=set(mylist)
print(newlist)

#missing values in set  
list1={1,2,3,4,5}
list2={4,5,6,7,8}   
print(list1-list2)


#common values in set
list1={1,2,3,4,5}
list2={4,5,6,7,8}
print(list1&list2)