class employee:
    company = "tata"
    name = "rahul"
    salary = 1000
    def show(self):
        print(f"the name of the employee{self.name} and salary is {self.salary}")
        
class coder:
    language = "python"
    def printlangauge(self):
        print(f"the language is {self.language}")
                      
class programmer(employee,coder):
    company = "microsoft"
    def showlanguage(self):
        print(f"the name ot the language {self.company} and the language is {self.language}")        
    
    
a = employee()
b = programmer()
#print(b.company,a.company)

b.show()
b.printlangauge()
b.showlanguage()