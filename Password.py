import random

randoms = ["$%S", "#H%", "H%S", "$07", "A?S", "L&S", "!&7", "5&A"]

def coding(pas):
    if len(pas)<=3:
        a = pas[1:4]
        b = random.choice(randoms)
        f = random.choice(randoms)
        c = pas[0]
        return f"{b}{a}{c}{f}"

    else:
        a = pas[::-1]
        return a

def decoding(pas):
    a = pas[3:5]
    b = pas[5]
    return f"{b}{a}"


password = input("Enter your Password : ")

question = input("Type D for Decoding and C for Coding : ").capitalize()

if len(password)<=3:
    print("You Can't Deocode, It because you cannot code it.First code it and than decode it")
else:
    if question=='D':
        print(decoding(str(password)))
    else:
        print(coding(str(password)))