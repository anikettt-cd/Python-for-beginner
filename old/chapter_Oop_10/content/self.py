class employee():
    salary = 100000. #this is a class attributes
    language = "python"
    
    @staticmethod
    def greet():
        print("Hello welcome to the company")
    
    def getinfo(self):
        print(f"The salary is {self.salary} and the language is {self.language}")
    
    
harry = employee()
# harry.language = "harry poter" this is an instance attributes
harry.greet()
harry.getinfo()