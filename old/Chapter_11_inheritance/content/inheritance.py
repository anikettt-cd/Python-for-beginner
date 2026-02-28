class employee:
    company = "tata"
    def show(self):
        print(f"the name of the employee{self.name} and salary is {self.salary}")
        
class programmer(employee):
    company = "microsoft"
    def showlanguage(self):
        print(f"the name ot the language {self.name} andthe language is {self.language}")        
    
    
a = employee()
b = programmer()
print(b.company,a.company)
    