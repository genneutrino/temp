def isempty(stk):
    if stk == []:
        return True
    else:
        return False


#top value is default -1 when all elements are 0. that is why top will always be length - 1 to correct the earlier assumption.

def push(stk,a):
    stk.append(a)
    top = len(stk)-1

def pop(stk):
    top = len(stk)-1
    stk.pop(top)





def display(stk):
    if isempty(stk):
        print("The stack is empty")
    else:
        top = len(stk)-1
        print(stk[top], "<-top")
        for a in range(top-1, -1, -1):
            print(stk[a])

            
stack = []
top = None
while True:
    print("\n"*5)
    print("\t", "STACK OPERATIONS", "\t")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    ch = int(input("Please enter your choice (1-4):"))

    if ch == 1:
        rno = int(input("Enter roll no. of student:"))
        name = input("Enter name of student:")
        marks = int(input("Enter marks of student:"))
        item = [rno, name, marks]
        push(stack, item)
        input()
             
    elif ch == 2:
        pop(stack)

    elif ch == 3:
        display(stack)
        input()

    elif ch == 4:
        print("!!ABORTING!!")
        break

    else:
        print("Invalid choice")
        input()
