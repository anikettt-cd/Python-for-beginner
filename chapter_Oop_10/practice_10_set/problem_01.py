class programmer: 
    company = "microsoft"
    
    def __init__(self,name,salary,language,pin):
        self.name = name
        self.salary = salary
        self.language = language
        self.pin = pin
        print("programmer object is created")
        
p = programmer("aniket", 100000, "javascript" , 560037)
print( f"  company name : {p.company}\n  employee name : {p.name}\n  employee salary :  {p.salary}\n  employee language : {p.language}\n  employee pin : {p.pin}\n")  
    
q = programmer("mohit", 100000 , "php" , 345767)
print( f"  company name : {q.company}\n  employee name : {q.name}\n  employee salary :  {q.salary}\n  employee language : {q.language}\n  employee pin : {q.pin}\n")  
    
r = programmer("mummy", 100000 ,"python", 235468)
print( f"  company name : {r.company}\n  employee name : {r.name}\n  employee salary :  {r.salary}\n  employee language : {r.language}\n  employee pin : {r.pin}\n")  
    