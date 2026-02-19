a = int(input("enter your number :"))
b = int(input("enter your number :"))

if(b == 0):
    raise ZeroDivisionError("hey program  not meant to divide by number zero")
else:
    print(f"division of {a} and {b} is {a/b}")
 
