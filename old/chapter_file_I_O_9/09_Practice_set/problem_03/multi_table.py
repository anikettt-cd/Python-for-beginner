def generatetable(n):
    table = ""
    for i in range(1 ,11):
        table += f"{n} X {i} = {n*i}\n"
        
        
    with open(f"/Users/aniketsaini/Desktop/Python/chapter_file_I_O_9/09_Practice_set/problem_03/tables/table_of_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generatetable(i)