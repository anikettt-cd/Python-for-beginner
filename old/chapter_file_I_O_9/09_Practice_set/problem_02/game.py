import random

def game():
     print("you are playing the game")
     score = random.randint(1,100)
     
     with open("chapter_file_I_O_9/09_Practice_set/01_problem/problem_02/hiscore.txt","r") as f:
         hiscore = f.read()
         if (hiscore != ""):
             hiscore = int(hiscore)
         else:
             hiscore = 0
             
     print(f"your score is {score} and high score is {hiscore}")
     if(score > hiscore):
        with open("chapter_file_I_O_9/09_Practice_set/01_problem/problem_02/hiscore.txt","w") as f:
            f.write(str(score))
            return score
        
game()