n = 1
while n:
    def add():
        i = 1
        while i:
            print("--------CALCULATER FOR ADDITION--------")
            a = int(input("ENTER THE NUMBER : "))
            b = int(input("ENTER ANOTHER NUMBER : "))
            c = a+b
            print("YOUR ANSWER : ",c)
            z = 1
            num9 = int(input("PRESS 1 FOR ADD ANOTHER NUMBER OTHERWISE 0: "))
            if num9 != 1:
                break
            else:
                while z:
                    num7 = int(input("ENTER ANOTHER NUMBER : "))
                    c += num7
                    print("YOUR ANSWER : ",c)
                    num = int(input("PRESS 1 FOR ADD ANOTHER NO. OTHERWISE 0: "))
                    if num != 1:
                        break
                    z += num
            choice = int(input("PRESS 1 FOR START AGAIN ADD CALCULATER OTHERWISE 0 : "))
            if choice != 1:
                break
            i += choice
    def subtraction():
        i = 1
        while i:
            print("--------CALCULATER FOR SUBTRACTION--------")
            a = int(input("ENTER THE NUMBER : "))
            b = int(input("ENTER ANOTHER NUMBER : "))
            c = a-b
            print("YOUR ANSWER : ",c)
            z = 1
            num9 = int(input("PRESS 1 FOR SUBTRACT TO ANOTHER NO. OTHERWISE 0: "))
            if num9 != 1:
                break
            else:
                while z:
                    num7 = int(input("ENTER ANOTHER NUMBER : "))
                    c -= num7
                    print("YOUR ANSWER : ",c)
                    num = int(input("PRESS 1 FOR SUBTRACT WITH ANOTHER NO. OTHERWISE 0: "))
                    if num != 1:
                        break
                    z += num

            choice = int(input("PRESS 1 FOR START SUBTRACT CALCULATER AGAIN OTHERWISE 0 : "))
            if choice != 1:
                break
            i += choice

    def division():
        i = 1
        while i:
            print("------CALCULATER FOR DIVISION------")
            a = int(input("ENTER THE NUMBVER : "))
            b = int(input("ENTER ANOTHER NUMBER : "))
            c = a/b
            print("YOUR ANSWER : ",c)
            choice = int(input("PRESS 1 FOR DIVIDE AGAIN OTHERWISE 0 : "))
            if choice != 1:
                break
            i += choice

    def multiplication():
        i = 1
        while i:
            print("--------CALCULATER FOR MULTIPLICATION--------")
            a = int(input("ENTER THE NUMBER : "))
            b = int(input("ENTER ANOTHER NUMBER : "))
            c = a*b
            print("YOUR ANSWER : ",c)
            z = 1
            num9 = int(input("PRESS 1 FOR MULTIPLY ANOTHER NO. OTHERWISE 0 : "))
            if num9 != 1:
                break
            else:
                while z:
                    num7 = int(input("ENTER ANOTHER NUMBER : "))
                    c *= num7
                    print("YOUR ANSWER : ",c)
                    num = int(input("PRESS 1 FOR MULTIPLICATION WITH ANOTHER NO. OTHERWISE 0 : "))
                    if num != 1:
                        break
                    z += num
            choice = int(input("PRESS 1 FOR START AGAIN MULTIPLICATION CALCULATER OTHERWISE 0 : "))
            if choice != 1:
                break
            i += choice
            
    print(" PRESS 1 FOR ADDITION \n PRESS 2 FOR SUBTRACT \n PRESS 3 FOR DIVISION \n PRESS 4 FOR MULTIPLICATION ")
    choice1 = int(input(' ENTER YOUR CHOICE : '))    
    if choice1 == 1:
        add()
    elif choice1 == 2:
        subtraction()
    elif choice1 == 3:
        division()
    elif choice1 == 4:
        multiplication()
    ch = int(input("PRESS 1 FOR START CALCULATER AGAIN OTHERWISE 0 : "))
    if ch != 1:
        print("----THANK_YOU----")
        break
    n+=ch       
