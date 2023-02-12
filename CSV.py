"""Create a csv file user.csv, entering user id and password, read and search
the password for given userid"""

import csv

def write():
    f=open(r"user.csv","w",newline="\n")
    trimax=csv.writer(f)
    trimax.writerow(["User-id","Password"])
    record=[]
    while True:
        user_id=int(input("Enter user id:"))
        password=input("Enter password:")
        temp=[user_id,password]
        record.append(temp)
        trimax.writerow(temp)
        ch=input("Do you want to enter more records? (y/n)")
        if ch=="n" or ch=="N":
            break
    f.close()

def read():
    f=open(r"user.csv","r",newline="\n")
    trimax=csv.reader(f)
    for i in trimax:
        print (i)
    f.close()

def search():
    f=open(r"user.csv","r",newline="\n")
    trimax=csv.reader(f)
    record=[]
    for i in trimax:
        if i[0]=="User-id":
            continue
        record.append(i)
    found=0
    userid=int(input("Enter the user-id whose password you require:"))
    for i in record:
        if int(i[0])==userid:
            print ("The corresponding password is:")
            print (i[1])
            found=1
            break
    if found==0:
        print ("User-id not found")

print ("Welcome to menu driven program for csv file")
point="y"
while point=="y" or point=="Y":
    print ("1 : Enter user-id and password")
    print ("2 : Read all records")
    print ("3 : Search for required password")
    print ("4 : Exit from program")
    choice=input("What do you want to do? (1/2/3/4):")
    if choice=="1":
        write()
    elif choice=="2":
        read()
    elif choice=="3":
        search()
    elif choice=="4":
        print ("Program aborted")
        break
    else:
        print ("Invalid choice")
        print ("Choose from 1 to 4")
        continue
    print ("If you want to continue, press y")
    point=input("")
print ("Thank you for using the menu")
        
    









