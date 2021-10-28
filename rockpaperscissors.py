import random
import time
playeroption=["rock","paper","scissors"]
while True:
    computer=playeroption[random.randint(0,2)]
    player=input("enter any one of the three rock,paper or scissors")
    print(f'computer chose {computer}')
    time.sleep(2)
    if(player==computer):
        print("tie")
    elif(player=="rock"):
        if(computer=="paper"):
            print("you lost!paper wraps the rock")    
        else:
            print("you won!scissoors was crushed by the rock") 
    elif(player=="scissors"):
        if(computer=="rock"):
            print("you lost!scissors was crushed by the rock")    
        else:
            print("you won!scissors cut the paper")               
    elif(player=="paper"):
        if(computer=="rock"):
            print("you won!paper wraps the rock")    
        else:
            print("you lost!paper was cut by the scissors")         