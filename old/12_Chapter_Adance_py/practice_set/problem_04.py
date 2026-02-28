try:
    a = int(input("enter the numbet a:"))
    b = int(input("enter the number b:"))
    print(a/b)
except ZeroDivisionError as e:
    print("infinite")    