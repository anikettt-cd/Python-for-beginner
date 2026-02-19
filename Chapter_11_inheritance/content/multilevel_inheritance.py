class employee:
     a = 1

class programmer(employee):
    b = 2

class manager(programmer):
    c = 3

o = employee()
print(o.a)
# print(o.b)# This will raise an AttributeError since 'employee' does not have 'b' or 'c')
 
o = programmer()
print(o.a,o.b) #This will raise an AttributeError since 'programmer' does not have '

o = manager()
print(o.a,o.b,o.c)
