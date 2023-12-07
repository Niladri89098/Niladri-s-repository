import random
list1=["Rock","Paper","Scissor"]
point=[]
m="r"
n="q"
print("Welcome to Roshambo")
print("Do you like to go through instructions?")
a=int(input("Give integer input\n1.Yes\n2.No\n->"))
if a==1:
    print("How to play: In rock-paper-scissors,\ntwo players will each randomly choose one of three hand signs: \nrock (made by making a fist),\n paper (made by laying your hand flat),\n or scissors (made by holding out two fingers to look like scissors).")
    print("Rock beats scissors, scissors beat paper, and paper beats rock.")
    print("Agree ahead of time whether you will count off rock, paper, scissors, shoot or just rock, paper, scissors.")
    print("Use rock, paper, scissors to settle minor decisions or simply play to p")
else:
    print("Lets continue the game.")
name=input("Enter your name: ")
point1=int(input("Choose your maximum point: \n3\n5\n10\n->"))
for i in range(0,point1):
    choice=int(input("Your turn: \n1.Rock\n2.Paper\n3.Scissor\n->"))
    d_choice=random.choice(list1)
    print("Computer: ",d_choice)
    if choice==1 and d_choice=="Rock":
        print("Draw")
    elif choice==2 and d_choice=="Paper":
        print("Draw")
    elif choice==3 and d_choice=="Scissor":
        print("Draw")
    elif choice==2 and d_choice=="Rock":
        print("You won")
        point.append(n)
    elif choice==2 and d_choice=="Scissor":
        print("You Loose")
        point.append(m)
    elif choice==1 and d_choice=="Paper":
        print("You Loose")
        point.append(m)
    elif choice==1 and d_choice=="Scissor":
        print("You won")
        point.append(n)
    elif choice==3 and d_choice=="Rock":
        print("You Loose")
        point.append(m)
    elif choice==3 and d_choice=="Paper":
        print("You won")
        point.append(n)
w=point.count(n)
l=point.count(m)
if w>l:
    print(f"Congratulations!!!!\n{name} you won the game.")
elif l>w:
    print("Game Over\nYou loose the game.\nBetter luck next time.")
else:
    print("Game Draw")
print(f"Match Scores:\nYou:{w}\nComputer:{l}")
print(f"Thank you {name} for playing this game")
print("Do you want to rate our game")
u=int(input("Give integer input:\n1.Yes\n2.No\n->"))
if u==1:
    print("Rate out us out of 5 star")
    try:
        s=int(input("Rate: "))
        if s>5 or s<0:
            raise ValueError
    except ValueError:
        print("You have to rate us out of 5")
    print(f"Thank you {name} for giving us your valuable time.")

else:
    print("You can also try our another games,for more information visit our website")





