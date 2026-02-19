class employee:
    salary = 200
    increment = 20
    
    @property
    def salaryAfterincrement(self):
        return self.salary + (self.salary * (self.increment / 100))
    
    @salaryAfterincrement.setter
    def salaryafterincremnet(self,salary):
        self.increment = ((salary / self.salary ) * 100)
        
    
e = employee()
print(e.salaryAfterincrement)
e.salaryafterincrement = 240
print(e.increment)