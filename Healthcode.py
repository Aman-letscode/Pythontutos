def getdate():
    import datetime
    return datetime.datetime.now()
while(True):
    lis = ["Harry=1","Rohan=2","Harad=3"]
    print(lis)
    m = int(input("Enter the number from the list:"))

    if m==1:
        c = int(input("Enter 1 for food and 2 for exercise:"))
        if c==1:
            info = input("Enter the food items you have consumed:\n")
            f = open("Harryfood.txt","a")
            f.write(str([str(getdate())])+":"+info+"\n")
            print("successfully updated")
        elif c==2:
            info = input("Enter the exercises you have done:\n")
            f = open("Harryex.txt","a")
            f.write(str([str(getdate())])+":"+info+"\n")
            print("successfully updated")
    elif m==2:
        c = int(input("Enter 1 for food and 2 for exercise:"))
        if c == 1:
            info = input("Enter the food items you have consumed:\n")
            f = open("Rohanfood.txt", "a")
            f.write(str([str(getdate())])+":"+info+"\n")
            print("successfully updated")
        elif c == 2:
            info = input("Enter the exercises you have done:\n")
            f = open("Rohanex.txt", "a")
            f.write(str([str(getdate())])+":"+info+"\n")
            print("successfully updated")
    elif m==3:
        c = int(input("Enter 1 for food and 2 for exercise:"))
        if c == 1:
            info = input("Enter the food items you have consumed:\n")
            f = open("Haradfood.txt", "a")
            f.write(str([str(getdate())])+":"+info+"\n")
            print("successfully updated")
        elif c == 2:
            info = input("Enter the exercises you have done:\n")
            f = open("Haradex.txt", "a")
            f.write(str([str(getdate())])+":"+info+"\n")
            print("successfully updated")
    else :
        print("Not in the list")