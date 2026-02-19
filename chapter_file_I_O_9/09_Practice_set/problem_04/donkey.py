words = "######"

with open("/Users/aniketsaini/Desktop/Python/chapter_file_I_O_9/09_Practice_set/problem_04/donkey.txt", "r") as f:
    content = f.read()
    
contentnew = content.replace(words, "donkey")

with open("/Users/aniketsaini/Desktop/Python/chapter_file_I_O_9/09_Practice_set/problem_04/donkey.txt", "w") as f:
    f.write(contentnew)