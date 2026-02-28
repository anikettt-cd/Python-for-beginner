n = int(input('ENTER THE NUMBER : '))

table = [n * i for i in range(1,11)]
with open ("/Users/aniketsaini/Desktop/Python/Chapter_Adance_12_py/practice_set/problem_05.py/text.txt", "a") as f:
    f.write(f" the table of {n}: {str(table)}")
    f.write("\n")