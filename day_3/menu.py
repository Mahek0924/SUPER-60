import sys

def add():
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    print(a+b)

def sub():
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    print(a-b)

def mul():
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    print(a*b)

def div():
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    print(a/b)


while True:
    print("1.addition")
    print("2.substraction")
    print("3.division")
    print("4.multiplication")
    print("5.exit")
    choice = int(input("Enter your choice : "))

    if (choice==1):
        add()
    elif (choice==2):
        sub()
    elif (choice==3):
        mul()
    elif (choice==4):
        div()
    elif (choice==5):
        sys.exit()