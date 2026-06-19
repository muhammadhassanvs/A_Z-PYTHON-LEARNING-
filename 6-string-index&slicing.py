#sting indexing

name="hassan"
print(name)
print(name[0]) #h
print(name[1]) #a
print(name[-1]) #n



#string sclicing
product="laptop pro 2024"
print(product[0:6]) #laptop
print(product[-4:]) #2024

#extract from beginnning
print(product[:6]) #laptop
#extract from end  
print(product[-4:]) #2024
#extract from middle
print(product[7:10]) #pro   

#skip text 
print(product[0:12:2]) #lpo r
print(product[0:12:3]) #lt o

#reverse using slicing
print(product[::-1]) #4202 orp potpal
print(product[4::-1]) #otpal