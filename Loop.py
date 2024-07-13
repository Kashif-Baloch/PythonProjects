num = input("Enter the Number : ")

def Nat(a):
    sum = 0
    for i in range(1, int(a)+1):
        sum = i+sum
    return sum

print(Nat(num))