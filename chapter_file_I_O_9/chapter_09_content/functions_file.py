f = open("chapter_file_I_O_9/myfile.txt","r")
# lines = f.readlines()
# print(lines,type(lines))

# f.close()


# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4 == "" )

line = f.readline()
while(line != ""):
    print(line,type(line))
    line = f.readline() 

f.close()