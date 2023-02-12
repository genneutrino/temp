#[Passenger_number, Name, Amount].

#Write a program to implement function:
#Write() to implement writing records in filr
#Read () to read all records from file 
#Countrec( ) to read contents of file “passenger.dat” and display the details of those passengers where amount is above 5000. 
#Also display number of passengers with amount above 5000.	

import pickle
def write():
    f=open("Passenger.dat","wb")
    rec=[]
    while True:
        Passenger_number=int(input("Enter passenger no:"))
        Name=input("Enter passenger name:")
        Amount=int(input("Enter amount between 1000 to 10,000:"))
        data=[Passenger_number,Name,Amount]
        rec.append(data)
        ch=input("Do you want to enter more records?(y/n)")
        if ch=='n' or ch=='N':
            break
    pickle.dump(rec,f)
    f.close()

def countrec():
    f=open("Passenger.dat","rb")
    print(['Passenger_number','Name','Amount'])
    found=0
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                if i[2]>5000:
                    print(i)
                    found=1
    except EOFError:
        f.close()
    if found==0:
        print("No Record found.")
           
def search():
    f=open("Passenger.dat","rb")
    found=0
    count=0
    a=int(input("enter Amount to be searched::"))
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                if i[2]>a:
                    count=count+1
                    found=1
            print("The number of passengers having greater amount than",a," are:",count)
    except EOFError:
        f.close()
    if found==0:
        print("No Record found.")
        
def MainMenu():
    print("1.Write records in binary file")
    print("2.Read and Count records in binary file")
    print("3.Search records in binary file")
while True:
    MainMenu()
    ch=int(input("Enter choice:"))
    if ch==1:
        write()
    elif ch==2:
        print("Details of passengers whose amount is above 5000:")
        countrec()
    elif ch==3:
        search()    
    else:
        break
    
    
