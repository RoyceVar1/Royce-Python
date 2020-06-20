import random 
possibleanswer = ("Rock","Paper","Sciccors")
player = input("What does your hand look like?")
cpu = random.choice(possibleanswer)
if player == cpu:
    print("you tie")

elif player == "Rock" and cpu == "Sciccors":
    print("You win")
elif player == "Rock" and cpu == "Paper":
    print("You loose")
elif player == "Paper" and cpu == "Rock":
    print("You win")
elif player == "Paper" and cpu == "Sciccors":
    print("You loose")
elif player == "Sciccors" and cpu == "paper":
    print("You win")
elif player == "Sciccors" and cpu == "Rock":
    print("You loose")


    
#if player == cpu: #Two ='s is used for comparison and one = is used for decleration
   # print("You tied")
#else:
    #print("You probabaly lost to my cpu")






















































