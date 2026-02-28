class coder:
    a = 10
    @classmethod
    def show(cls):
        print(f"Value of a is {cls.a}")
        
e = coder() #to print  class atribute value by a using class method
e.a = 20
e.show()        