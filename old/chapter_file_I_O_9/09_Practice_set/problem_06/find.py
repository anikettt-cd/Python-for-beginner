with open("/Users/aniketsaini/Desktop/Python/chapter_file_I_O_9/09_Practice_set/problem_06/words.txt", "r") as f:
    content = f.read()
    
    if ("python in content"):
        print("Yes,python is present in the file")
    else:
        print("no python is not present in the file")
    
    