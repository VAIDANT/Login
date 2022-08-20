lp=["Hokage1","Hokage2","Hokage3","Hokage4","Hokage5","Hokage6","Hokage7"]
lu=["Hashirama","Tobirama","Hiruzen","Minato","Tsunade","Kakashi","Naruto"]
fp=str(input("Do you remember your password enter yes or no\n"))
y='yes'
n='no'
if fp==y:
    u=str(input("Enter The Username\n"))
    p=str(input("Enter The Password\n"))
    if u==lu[0] and p==lp[0]:
            print("Welcome Hashirama")
    elif u==lu[1] and p==lp[1]:
            print("Welcome Tobirama")
    elif u==lu[2] and p==lp[2]:
            print("Welcome Hiruzen")
    elif u==lu[3] and p==lp[3]:
            print("Welcome Minato")
    elif u==lu[4] and p==lp[4]:
            print("Welcome Tsunade")
    elif u==lu[5] and p==lp[5]:
            print("Welcome Kakashi")
    elif u==lu[6] and p==lp[6]:
        print("Welcome Naruto")
    else:
        print("Invalid Username or Password")
elif fp==n:
    fpu=str(input("Enter the user name"))
    if fpu in lu:
        print("answer the following question to retrieve your Password")
        q=int(input("Which number hokage are you"))
        if fpu==lu[0] and q==1:
            print("Your paaswor is Hokage1")
        elif fpu==lu[1] and q==2:
            print("Your paaswor is Hokage2")
        elif fpu==lu[2] and q==3:
            print("Your paaswor is Hokage3")
        elif fpu==lu[3] and q==4:
            print("Your paaswor is Hokage4")
        elif fpu==lu[4] and q==5:
            print("Your paaswor is Hokage5")
        elif fpu==lu[5] and q==6:
            print("Your paaswor is Hokage6")
        elif fpu==lu[6] and q==7:
            print("Your paaswor is Hokage7")
        else:
            print("wrong answer")
    else:
        print("Invalid user name")
else:
    print("Invalid input(you can only enter yes or no)")
