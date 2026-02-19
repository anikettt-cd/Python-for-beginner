import random 
n = random.randint(1,100)
a = -1
guesses = 0
while ( a != n):
    a = int(input("guess a number betwen 1 and 100 : "))
    if ( a > n):
         print(f"guess lower then number {a} ")
         guesses +=1
    elif ( a < n): 
        print(f"guess higher then number {a} ")
        guesses +=1
        
print(f"congratulations you guessed the number {n} in ", guesses, "guesses")