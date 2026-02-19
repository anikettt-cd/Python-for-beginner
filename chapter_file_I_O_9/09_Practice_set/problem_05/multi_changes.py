words = ["donkey", "scam", "donkeyism"]

with open("/Users/aniketsaini/Desktop/Python/chapter_file_I_O_9/09_Practice_set/problem_04/donkey.txt", "r") as f:
    content = f.read()
   
for word in words:  
 content = content.replace(word, "#" * len(word))

with open("/Users/aniketsaini/Desktop/Python/chapter_file_I_O_9/09_Practice_set/problem_04/donkey.txt", "w") as f:
    f.write(content)