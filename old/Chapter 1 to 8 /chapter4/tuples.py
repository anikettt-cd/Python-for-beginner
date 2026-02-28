# Creating a tuple in Python

my_tuple = (1, 2, 3, 'apple', 'banana')
# print(my_tuple)

# a = my_tuple.index(3)
# print (a)
a = my_tuple.index(3)
print (a)


t1 = ((1, 2, 3), (3, 4), (12))
# t2 = ('a', 'b', 'c', 'd', 'e')
# print(t1+ t2)
# print(t1*3)

print(t1[0])
print(t1[1][1])  


t = (1, 2, 3, 4, 5)
lst = list(t)
lst[0] = 100
t = tuple(lst)
print(t)

