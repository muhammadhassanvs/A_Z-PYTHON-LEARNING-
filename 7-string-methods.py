#string methods

#remove whitespace
name="   hassan   "
print(name)
print(name.strip()) #hassan

#convert into capital letters
name="hassan"
print(name.upper()) #HASSAN

#convert into proper case
name="hassan"
print(name.title()) #Hassan

#convert into lowercase
name="HASSAN"   
print(name.lower()) #hassan

#replace text
product="laptop pro 2024"   
print(product.replace("laptop","desktop")) #desktop pro 2024

#count occurrences of a substring
product="laptop pro 2024"
print(product.count("p")) #3

#check if string starts with a substring
product="laptop pro 2024"
print(product.startswith("laptop")) #True

#check if only contains numbers
product="2024"  
print(product.isnumeric()) #True

#converting into list of words
product="laptop pro 2024"
print(product.split()) #['laptop', 'pro', '2024']

#join back with hyphen or anyhting
joined_text="-".join(product.split())
print(joined_text) #laptop-pro-2024

# find position of a letter or substring
product="laptop pro 2024"  
print(product.find("p")) #2