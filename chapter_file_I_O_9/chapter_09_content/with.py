f = open("chapter_file_I_O_9/file.txt","r")
date = f.write()
print(date)
f.close()

# same can be done with 'with' statement

with open("chapter_file_I_O_9/file.txt","r") as f:
    date = f.read()
    print(date)
    
    # no need to  close the file explicitly 