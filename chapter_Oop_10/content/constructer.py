class employee:
    salary = 100000 #this is a class attributes
    language = "javascript"
    
    def __init__(self, name , salary ,language): #
        self.name = name
        self.salary = salary 
        self.language = language 
        print("Employee object is created")
    
    @staticmethod
    def greet():
        print("Hello welcome to the company")
    
    def getinfo(self):
        print(f"The salary is {self.salary} and the language is {self.language}")
    
    
harry = employee("harry", 1300000, "python")
# harry.language = "harry poter" this is an instance attributes
print(harry.salary, harry.name,harry.language )