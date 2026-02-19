class calculator:  
    def __init__ (self, n):
     self.n = n 
     
    def greet(self):
         print("Hello welcome to teh calculator")
         
    def square(self):
         print(f"the square of the number: {self.n * self.n}")
         
    def cube(self):
         print(f"the square of the number: {self.n * self.n * self.n}")
         
    def squareroot(self):
         print(f"the square of the number: {self.n ** 1/2}")          
         
a = calculator(4)
a.greet()         
a.square()
a.cube()
a.squareroot()  