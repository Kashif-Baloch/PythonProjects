""" First Programme
Dic = sorted({"Kashif":"Programmer","Haseeb":"Kashif\'s Brother","Zohaib":"Kashif\'s friend",
        "Tayyab":"a student","Harry":"Programmer","Shoaib":"President"})
nu = input("Whom you Indentify ? :")
print("He is", nu) """


""" Second Programme
num = input("What do you want to do ( - + * / % ) : ")
n = int(input("Enter first number to : "))
n1 = int(input("Enter first number to : "))
if num=='*' and n==45 and n1==3:
    a = 555
    print(a)
if num=='+' and n==56 and n1==9:
    a = 76
    print(a)
if num=='/' and n==56 and n1==4:
    a = 4
    print(a)
if num=='-' and n==n and n1==n1:
    a = n - n1
    print(a)
if num=='+' and n==n and n1==n1:
    a = n + n1
    print(a)
if num=='*' and n==n and n1==n1:
    a = n * n1
    print(a)
if num=='/' and n==n and n1==n1:
    a = n / n1
    print(a)
if num=='%' and n==n and n1==n1:
    a = n % n1
    print(a) """


""" Third Programme
g = 17
o = 1
print("You have only 10 time to guess")
while (o<=10):
    num = int(input("Guess The Number : "))
    if num<g:
        print("You entered too Low")
        print(f"You guessing is now {o} ")
    elif num>g:
        print("You entered too high")
        print(f"You guessing is now {o}")
    elif num==g:
        print("You Win")
        print(f"You taken {o} time to guess")
        break
    o = o+1
    if o==11:
        print("Game over") """

""" Fourth Programme
n = input("Number of Rows : ")
bolean = input("1 to 0 : ")

if bolean=='1':
    for t in range(0,int(n)):
        t = t+1
        print("*"*t)

elif bolean=='0':
    for t in range(int(n),0):
        t = t-1
        print("*"*t) """

""" Fifth Programme
import datetime
def gettime():
    return datetime.datetime.now()

def Lock(a):
    if (a==1):
        c = int(input("Enter 1 for Exercise 2 for Food : "))
        if (c==1):
            value = input("Type Here : ")
            with open("K-Ex.txt", "a") as y:
                y.write(str([str(gettime())]) + " : " +value+ "\n")
                print("Successfully Written")
        elif (c==2):
            value = input("Type Here : ")
            with open("K-Food.txt", "a") as y:
                y.write(str([str(gettime())]) + " : " +value+ "\n")
                print("Successfully Written")

    elif (a==2):
        c = int(input("Enter 1 for Exercise 2 for Food : "))
        if (c==1):
            value = input("Type Here : ")
            with open("Z-Ex.txt", "a") as y:
                y.write(str([str(gettime())]) + " : " +value+ "\n")
                print("Successfully Written")
        elif (c==2):
            value = input("Type Here : ")
            with open("Z-Food.txt", "a") as y:
                y.write(str([str(gettime())]) + " : " +value+ "\n")
                print("Successfully Written")
    elif (a==3):
        c = int(input("Enter 1 for Exercise 2 for Food : "))
        if (c==1):
            value = input("Type Here : ")
            with open("T-Ex.txt", "a") as y:
                y.write(str([str(gettime())]) + " : " +value+ "\n")
                print("Successfully Written")
        elif (c==2):
            value = input("Type Here : ")
            with open("T-Food.txt", "a") as y:
                y.write(str([str(gettime())]) + " : " +value+ "\n")
                print("Successfully Written")

def Retrieve(b):
    if (b==1):
        c = int(input("Enter 1 for Exercise 2 for Food : "))
        if (c==1):
            with open("K-Ex.txt") as y:
                for k in y:
                    print(k, end="")
        elif (c==2):
            with open("K-Food.txt") as y:
                for k in y:
                    print(k, end="")

    elif (b==2):
        c = int(input("Enter 1 for Exercise 2 for Food : "))
        if (c==1):
            with open("Z-Ex.txt") as y:
                for k in y:
                    print(k, end="")
        elif (c==2):
            with open("Z-Food.txt") as y:
                for k in y:
                    print(k, end="")

    elif (b==3):
        c = int(input("Enter 1 for Exercise 2 for Food : "))
        if (c==1):
            with open("T-Ex.txt") as y:
                for k in y:
                    print(k, end="")
        elif (c==2):
            with open("T-Food.txt") as y:
                for k in y:
                    print(k, end="")

a = int(input("Press 1 for Lock and 2 for Retrieve : "))

if a==1:
    l = int(input("Press 1 for Kashif 2 for Zohaib 3 for Tayyab : "))
    Lock(a)

elif a==2:
    r = int(input("Press 1 for Kashif 2 for Zohaib 3 for Tayyab : "))
    Retrieve(r)

else:
    print("Invalid Choice") """

""" Sixth Programme
def speak():
    import random
 
    # The three states are:
    # 0 - rock
    # 1 - scissors
    # 2 - paper
    
    # the computer chooses a number
    pc = random.randint(0,2)
    
    # the user enters a number
    print("Choose your option:")
    print("0 - rock")
    print("1 - scissors")
    print("2 - paper")
    
    user = input("")
    # convert the string to an integer
    user = int(user)
    
    # make a sanity check
    # if (user &lt; 0) or (user &gt; 2):
    #     print("Wrong input")
    #     exit()
    
    print("The computer chose: ",end="")
    if (pc == 0):
        print("rock")
    elif (pc == 1):
        print("scissors")
    elif (pc == 2):
        print("paper")
    
    print("The user chose: ",end="")
    if (user == 0):
        print("rock")
    elif (user == 1):
        print("scissors")
    elif (user == 2):
        print("paper")
    
    # decide who wins
    if (pc == 0):
        if (user == 0):
            print("Tie game")
        elif (user == 1):
            print("Computer wins")
        elif (user == 2):
            print("User wins")
    elif (pc == 1):
        if (user == 0):
            print("User wins")
        elif (user == 1):
            print("Tie game")
        elif (user == 2):
            print("Computer wins")
    elif (pc == 2):
        if (user == 0):
            print("Computer wins")
        elif (user == 1):
            print("User wins")
        elif (user == 2):
            print("Tie game")
    elif user>3:
        print('Your choice is wrong ')
while True:
    speak() """


# """ from turtle import *
# # Doraemon with Python Turtle
# def ankur(x, y):
#     penup()
#     goto(x, y)
#     pendown()


# def aankha():
#     fillcolor("#ffffff")
#     begin_fill()

#     tracer(False)
#     a = 2.5
#     for i in range(120):
#         if 0 <= i < 30 or 60 <= i < 90:
#             a -= 0.05
#             lt(3)
#             fd(a)
#         else:
#             a += 0.05
#             lt(3)
#             fd(a)
#     tracer(True)
#     end_fill()


# def daari():
#     ankur(-32, 135)
#     seth(165)
#     fd(60)

#     ankur(-32, 125)
#     seth(180)
#     fd(60)

#     ankur(-32, 115)
#     seth(193)
#     fd(60)

#     ankur(37, 135)
#     seth(15)
#     fd(60)

#     ankur(37, 125)
#     seth(0)
#     fd(60)

#     ankur(37, 115)
#     seth(-13)
#     fd(60)


# def mukh():
#     ankur(5, 148)
#     seth(270)
#     fd(100)
#     seth(0)
#     circle(120, 50)
#     seth(230)
#     circle(-120, 100)


# def muflar():
#     fillcolor('#e70010')
#     begin_fill()
#     seth(0)
#     fd(200)
#     circle(-5, 90)
#     fd(10)
#     circle(-5, 90)
#     fd(207)
#     circle(-5, 90)
#     fd(10)
#     circle(-5, 90)
#     end_fill()


# def nak():
#     ankur(-10, 158)
#     seth(315)
#     fillcolor('#e70010')
#     begin_fill()
#     circle(20)
#     end_fill()


# def black_aankha():
#     seth(0)
#     ankur(-20, 195)
#     fillcolor('#000000')
#     begin_fill()
#     circle(13)
#     end_fill()

#     pensize(6)
#     ankur(20, 205)
#     seth(75)
#     circle(-10, 150)
#     pensize(3)

#     ankur(-17, 200)
#     seth(0)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(5)
#     end_fill()
#     ankur(0, 0)


# def face():
#     fd(183)
#     lt(45)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(120, 100)
#     seth(180)
#     # print(pos())
#     fd(121)
#     pendown()
#     seth(215)
#     circle(120, 100)
#     end_fill()
#     ankur(63.56, 218.24)
#     seth(90)
#     aankha()
#     seth(180)
#     penup()
#     fd(60)
#     pendown()
#     seth(90)
#     aankha()
#     penup()
#     seth(180)
#     fd(64)


# def taauko():
#     penup()
#     circle(150, 40)
#     pendown()
#     fillcolor('#00a0de')
#     begin_fill()
#     circle(150, 280)
#     end_fill()


# def Doraemon():
#     taauko()

#     muflar()

#     face()

#     nak()

#     mukh()

#     daari()

#     ankur(0, 0)

#     seth(0)
#     penup()
#     circle(150, 50)
#     pendown()
#     seth(30)
#     fd(40)
#     seth(70)
#     circle(-30, 270)

#     fillcolor('#00a0de')
#     begin_fill()

#     seth(230)
#     fd(80)
#     seth(90)
#     circle(1000, 1)
#     seth(-89)
#     circle(-1000, 10)

#     # print(pos())

#     seth(180)
#     fd(70)
#     seth(90)
#     circle(30, 180)
#     seth(180)
#     fd(70)

#     # print(pos())
#     seth(100)
#     circle(-1000, 9)

#     seth(-86)
#     circle(1000, 2)
#     seth(230)
#     fd(40)

#     # print(pos())

#     circle(-30, 230)
#     seth(45)
#     fd(81)
#     seth(0)
#     fd(203)
#     circle(5, 90)
#     fd(10)
#     circle(5, 90)
#     fd(7)
#     seth(40)
#     circle(150, 10)
#     seth(30)
#     fd(40)
#     end_fill()

#     seth(70)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(-30)
#     end_fill()

#     ankur(103.74, -182.59)
#     seth(0)
#     fillcolor('#ffffff')
#     begin_fill()
#     fd(15)
#     circle(-15, 180)
#     fd(90)
#     circle(-15, 180)
#     fd(10)
#     end_fill()

#     ankur(-96.26, -182.59)
#     seth(180)
#     fillcolor('#ffffff')
#     begin_fill()
#     fd(15)
#     circle(15, 180)
#     fd(90)
#     circle(15, 180)
#     fd(10)
#     end_fill()

#     ankur(-133.97, -91.81)
#     seth(50)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(30)
#     end_fill()
#     # Doraemon with Python Turtle

#     ankur(-103.42, 15.09)
#     seth(0)
#     fd(38)
#     seth(230)
#     begin_fill()
#     circle(90, 260)
#     end_fill()

#     ankur(5, -40)
#     seth(0)
#     fd(70)
#     seth(-90)
#     circle(-70, 180)
#     seth(0)
#     fd(70)

#     ankur(-103.42, 15.09)
#     fd(90)
#     seth(70)
#     fillcolor('#ffd200')
#     # print(pos())
#     begin_fill()
#     circle(-20)
#     end_fill()
#     seth(170)
#     fillcolor('#ffd200')
#     begin_fill()
#     circle(-2, 180)
#     seth(10)
#     circle(-100, 22)
#     circle(-2, 180)
#     seth(180 - 10)
#     circle(100, 22)
#     end_fill()
#     goto(-13.42, 15.09)
#     seth(250)
#     circle(20, 110)
#     seth(90)
#     fd(15)
#     dot(10)
#     ankur(0, -150)
#     black_aankha()
# if __name__ == '__main__':
#     screensize(800, 600, "#f0f0f0")
#     pensize(3)
#     speed(9)
#     Doraemon()
#     ankur(100, -300)
#     write('by Ankur Gajurel', font=("Bradley Hand ITC", 30, "bold")) """


# """ from sketchpy import library as lib
# # obj=lib.rdj()
# # obj=lib.apj()
# #obj=lib.bts()
# #obj=lib.gojo()
# # obj=lib.flag()
# # obj=lib.vijay()
# # obj=lib.ironman_ascii()

# obj.draw() """

# """ import turtle
# from turtle import *

# wn=Screen()
# wn.bgcolor("Black")

# t = turtle.Turtle()
# t.pencolor("Blue")

# def curve():
#     for i in range(200):
#         t.rt(1)
#         t.fd(1)

# def heart():
#     t.fillcolor("red")
#     t.begin_fill()
#     t.lt(140)
#     t.fd(113)
#     curve()
#     t.lt(120)
#     curve()
#     t.fd(112)
#     t.end_fill()

# heart()
# t.ht()

# def write(m, p):
#     x,y=p
#     t.penup()
#     t.goto(x,y)
#     t.color('white')
#     style=('stencil std', '18', 'italic')
#     t.write(m,font=style)

# write('I', (-68,95))
# write('L', (-55,95))
# write('O', (-42,95))
# write('V', (-30,95))
# write('E', (-14,95))
# write('Y', (-10,95))
# write('O', (-26,95))
# write('U', (-45,95))

# wn.mainloop() """

# """ from sketchpy import library

# o=library.tom_holland()
# o=library.gojo()
# o.draw() """

""" # New Programe Snake Water Gun
import random

count=10
total_count=1
_computer=0
human=0
_list=["s","g","w"]
print("\t\t\t\t\t\t\tSnake Water Gun")

while(total_count<=count):
    _input=input("S for Snake, W for Gun, G for Gun : ")
    computer=random.choice(_list)

    if _input==computer:
        print("Game Tie, No One Win")
        print(f"Because You Chose {_input} And Computer chose {computer}")
        print(f"You both have {count} more chance to play the Game")
        with open('Text.txt', 'a') as f:
            f.write(f"Computer Choose {computer}\nHuman Choose{_input}\n")
    elif _input=='s' and computer=='g':
        print("You Lose")
        print(f"Because You Chose {_input} And Computer chose {computer}")
        print(f"You both have {count} more chance to play the Game")
        _computer+=1
        with open('Text.txt', 'a') as f:
            f.write(f"Computer Choose {computer}\nHuman Choose{_input}\n")
    elif _input=='s' and computer=='w':
        print("You Win")
        print(f"Because You Chose {_input} And Computer chose {computer}")
        print(f"You both have {count} more chance to play the Game")
        human+=1
        with open('Text.txt', 'a') as f:
            f.write(f"Computer Choose {computer}\nHuman Choose{_input}\n")
    elif _input=='g' and computer=='s':
        print("You Win")
        print(f"Because You Chose {_input} And Computer chose {computer}")
        print(f"You both have {count} more chance to play the Game")
        human+=1
        with open('Text.txt', 'a') as f:
            f.write(f"Computer Choose {computer}\nHuman Choose{_input}\n")
    elif _input=='g' and computer=='w':
        print("You Lose")
        print(f"Because You Chose {_input} And Computer chose {computer}")
        print(f"You both have {count} more chance to play the Game")
        _computer+=1
        with open('Text.txt', 'a') as f:
            f.write(f"Computer Choose {computer}\nHuman Choose{_input}\n")
    elif _input=='w' and computer=='s':
        print("You Lose")
        print(f"Because You Chose {_input} And Computer chose {computer}")
        print(f"You both have {count} more chance to play the Game")
        _computer+=1
        with open('Text.txt', 'a') as f:
            f.write(f"Computer Choose {computer}\nHuman Choose{_input}\n")
    elif _input=='w' and computer=='g':
        print("You Win")
        print(f"Because You Chose {_input} And Computer chose {computer}")
        print(f"You both have {count} more chance to play the Game")
        human+=1
        with open('Text.txt', 'a') as f:
            f.write(f"Computer Choose {computer}\nHuman Choose{_input}\n")
    else:
        print("Wrong Choice")
    count-=1

if human<_computer:
    print("You Lose this Game")
    print(f"You'r point is {human} And Computer's point is {_computer}")
elif human>_computer:
    print("You Won this Game")
    print(f"You'r point is {human} And Computer's point is {_computer}")
else:
    print("This Game is Tie")
    print(f"You'r point is {human} And Computer's point is {_computer}") """