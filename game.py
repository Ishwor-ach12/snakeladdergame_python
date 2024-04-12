import random
import module1
import module2
import time
print("welcome to snake ladder game: ")
s=input("enter player1 name: ")
p=input("enter player2 name: ")
p11=0
p22=0
while p11!=100 and p22!=100:
    print(" ")
    print('''snakes: 8-24, 32-10, 36-6, 48-26, 62-18, 88-20, 95-56, 97-27

    ladder: 4-14, 8-30, 20-76, 21-42, 50-67, 71-92, 80-99''' )
    print(" ")
    a=module1.player1(p11)
    if p11==95:
        if a>=6:
            print("oops! ")
        else:
            p11=p11+a
            p11=module2.snake(p11,0)
            p11=module2.ladder(p11,0)
            if p11==p22:
                p22=0
    elif p11==96:
        if a>=6 or a==5:
             print("oops! ")
        else:
            p11=p11+a
            p11=module2.snake(p11,0)
            p11=module2.ladder(p11,0)
            if p11==p22:
                p22=0
    elif p11==97:
        if a>=6 or a==5 or a==4:
             print("oops! ")
        else:
            p11=p11+a
            p11=module2.snake(p11,0)
            p11=module2.ladder(p11,0)
            if p11==p22:
                p22=0
    elif p11==98:
        if a>=2 or a==1:
            p11=p11+a
            p11=module2.snake(p11,0)
            p11=module2.ladder(p11,0)
            if p11==p22:
                p22=0
        else:
             print("oops! ")
    elif p11==99:
        if a>=1:
            p11=p11+a
            p11=module2.snake(p11,0)
            p11=module2.ladder(p11,0)
            if p11==p22:
                p22=0 
        else:
             print("oops! ")
    else:
        p11=p11+a
        p11=module2.snake(p11,0)
        p11=module2.ladder(p11,0)
        if p11==p22:
            p22=0
    print('''Scorecard:
    Name     |   position''')
    print("   ",s,"        ",p11)
    print("   ",p,"         ",p22)
    b=module1.player2(p22)
    if p22==95:
        if b>=6:
            print("oops! ")
        else:
            p22=p22+b
            p22=module2.snake(0,p22)
            p22=module2.ladder(0,p22)
            if p22==p11:
                p11=0
    elif p22==96:
        if b>=6 or b==5:
             print("oops! ")
        else:
            p22=p22+b
            p22=module2.snake(0,p22)
            p22=module2.ladder(0,p22)
            if p22==p11:
                p11=0
    elif p22==97:
        if b>=6 or b==5 or b==4:
             print("oops! ")
        else:
            p22=p22+b
            p22=module2.snake(0,p22)
            p22=module2.ladder(0,p22)
            if p22==p11:
                p11=0
    elif p22==98:
        if b>=2 or b==1:
            p22=p22+b
            p22=module2.snake(0,p22)
            p22=module2.ladder(0,p22)
            if p22==p11:
                p11=0
        else:
             print("oops! ")
    elif p22==99:
        if b>=1:
            p22=p22+b
            p22=module2.snake(0,p22)
            p22=module2.ladder(0,p22)
            if p22==p11:
                p11=0 
        else:
             print("oops! ")
    else:
        p22=p22+b
        p22=module2.snake(0,p22)
        p22=module2.ladder(0,p22)
        if p22==p11:
            p11=0
    print('''Scorecard:
    Name     |   position''')
    print("   ",s,"        ",p11)
    print("   ",p,"         ",p22)
    if p11==100:
        print(s ,"has won the match")
        print(p, "better luck next time")
    if p22==100:
        print(p, "has won the match")
        print(s, "better luck next time")
    time.sleep(1)


         


