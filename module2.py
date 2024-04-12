def snake(p11,p22):
    if p11==24 or p22==24:
        print("snake caught: ")
        if p11==24:
            p11=8
            return p11
        else:
            p22=8
            return p22
    elif p11==32 or p22==32:
        print("snake caught: ")
        if p11==32:
            p11=10
            return p11
        else:
            p22=10
            return p22
    elif p11==36 or p22==36:
        print("snake caught: ")
        if p11==36:
            p11=6
            return p11
        else:
            p22=6
            return p22
    elif p11==48 or p22==48:
        print("snake caught: ")
        if p11==48:
            p11=26
            return p11
        else:
            p22=26
            return p22
    elif p11==62 or p22==62:
        print("snake caught: ")
        if p11==62:
            p11=18
            return p11
        else:
            p22=18
            return p22
    elif p11==88 or p22==88:
        print("snake caught: ")
        if p11==88:
            p11=20
            return p11
        else:
            p22=20
            return p22
    elif p11==95 or p22==95:
        print("snake caught: ")
        if p11==95:
            p11=56
            return p11
        else:
            p22=56
            return p22
    elif p11==97 or p22==97:
        print("snake caught: ")
        if p11==97:
            p11=27
            return p11
        else:
            p22=27
            return p22
    else:
        if p11==0:
            return p22
        else:
            return p11

    
def ladder(p11,p22):
    if p11==4 or p22==4:
        print("ladder climbed: ")
        if p11==4:
            p11=14
            return p11
        else:
            p22=14
            return p22
    elif p11==8 or p22==8:
        print("ladder climbed: ")
        if p11==8:
            p11=30
            return p11
        else:
            p22=30
            return p22
    elif p11==28 or p22==28:
        print("ladder climbed: ")
        if p11==28:
            p11=76
            return p11
        else:
            p22=76
            return p22
    elif p11==21 or p22==21:
        print("ladder climbed: ")
        if p11==21:
            p11=42
            return p11
        else:
            p22=42
            return p22
    elif p11==50 or p22==50:
        print("ladder climbed: ")
        if p11==50:
            p11=67
            return p11
        else:
            p22=67
            return p22
    elif p11==71 or p22==71:
        print("ladder climbed: ")
        if p11==71:
            p11=92
            return p11
        else:
            p22=92
            return p22
    elif p11==80 or p22==80:
        print("ladder climbed: ")
        if p11==80:
            p11=99
            return p11
        else:
            p22=99
            return p22
    else:
        if p11==0:
            return p22
        else:
            return p11