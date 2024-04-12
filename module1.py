
def player1(p11):
    import random
    p1=0
    x=int(input("press 0 to roll the dice:- "))
    while x!=0:
        x=int(input("press 0 to roll the dice:- "))
    if x==0:
        result1=random.randint(1,6)
        print(result1)
        if result1==1 or p11>0:
            p1=p1+result1
            while result1==1 or result1==6:
                x=int(input("press 0 to roll the dice again:- "))
                while x!=0:
                    x=int(input("press 0 to roll the dice again:- "))
                if x==0:
                    result1=random.randint(1,6)
                    print(result1)
                    p1=p1+result1
    return p1

def player2(p22):
    import random
    p2=0
    y=int(input("press 0 to roll the dice:- "))
    while y!=0:
        y=int(input("press 0 to roll the dice:- "))
    if y==0:
        result2=random.randint(1,6)
        print(result2)
        if result2==1 or p22>0:
            p2=p2+result2
            while result2==1 or result2==6:
                y=int(input("press 0 to roll the dice again:- "))
                while y!=0:
                    y=int(input("press 0 to roll the dice again:- "))
                if y==0:
                    result2=random.randint(1,6)
                    print(result2)
                    p2=p2+result2
    return p2