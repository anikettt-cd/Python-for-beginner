class demo:
    a = 10
o = demo()
print(o.a) #prints the class attributes because instance attribues is nnot present.
o.a = 888 # Instance attribute created.
print(o.a) #prints  instance attributes because it is present. 
print(demo.a)
  