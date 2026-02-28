with open("/Users/aniketsaini/Desktop/Python/chapter_file_I_O_9/09_Practice_set/problem_06/words.txt", "r") as f:
     lines = f.readlines()
    
lineno  = 1
for line in lines:
    if ("python" in line):
        print(f"Yes,python is present in the file, at line no {lineno}")
        break
    lineno += 1
else:
        print("no python is not present in the file")