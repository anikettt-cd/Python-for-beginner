

import random
bot = random.randint(0,2)
youstr = input(("enter you choice:"))
youdict = {"r":0 ,"s":1 ,"p":2}
reversedict = {0:"rock", 1:"sisser",2:"paper"}

you = youdict[youstr]

print(f"you choose {reversedict[you]} \n bot choose {reversedict[bot]}")


if(bot ==you):
    print("Its a draw")

else:
    if(bot == 1 and you == 2):
        print("bot wins!!! , you lose")
    
    elif(bot == 2 and you == 0):
        print("bot wins!!! , you lose")
        
    elif(bot == 0 and you == 1):
        print("bot wins!!! , you lose")
        
    elif(bot == 1 and you == 0):
        print("you win!!! , bot lose") 
        
    elif(bot == 0 and you == 2):
        print("you wi!!! , bot lose")    
            
    elif(bot == 2 and you == 1):
        print("you win!!! , bot lose")   
        
    else:      
        print("Something went wrong!!!")