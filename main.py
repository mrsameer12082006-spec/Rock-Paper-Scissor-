import random
computer= random.choice([1,0,-1])

yourchoice=input("Enter your choice: ")    # here you will put your choice in form of words like(s,g,w)
youDict={"r":1 , "p":0 , "s":-1}
reversedict={1:"rock", 0:"paper" , -1:"scissor"}

if yourchoice not in youDict:        #if statement so that user only put thier input in r p and s.
    print("invalid input please put your answer in r,p,s  only")
else:
    your=youDict[yourchoice]   #your choice will convert into number and stored in "your"
# By now we have two nummber you and computer 

    print(f"Your choice {reversedict[your]} \n computer choice {reversedict[computer]}")
# here we have used reverse dict on you and computer both as it change your number to name like ("snake","water","gun")

    if (computer==your):     
         print("Match is Draw")

    else:
        if(computer==1 and your==0):
             print("You Loose")
        elif(computer==1 and your==-1):
             print("You Win")
        elif(computer==0 and your==-1):
             print("You Loose")
        elif(computer==0 and your==1):
             print("You Win")
        elif(computer==-1 and your==1):
             print("You Loose")
        elif(computer==-1 and your==0):
             print("You Win")
        else:
             print("some thing is wrong")
