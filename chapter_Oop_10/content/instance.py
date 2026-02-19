class employee():
    salary = 100000. #this is a class attributes
    language = "python"
    
    
harry = employee()
harry.language = "harry poter" #this is an instance attributes
print(harry.salary,harry.language)

#instance attributes are given preference over class attribues during assignment and retrivel
 
