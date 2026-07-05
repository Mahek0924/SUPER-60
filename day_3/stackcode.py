# 1. push  2. pop   3. peek   4. isEmpty  5. isFull  6. 
import sys
class Stack:
    def __init__(self,stackSize):
        self.stackSize = stackSize #stack size define
        self.myStack=[]  #list represent stack
        print("Stack has created")

    def push(self,value):
        if self.isFull():
            print("Stack is full")
        else:
            self.myStack.append(value)

    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.myStack == []:
            True
        else:
            False

    def display(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack = ", self.myStack)

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.myStack.pop())

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else: 
            print(self.myStack[-1])

    def deleteStack(self):
        del self.myStack
        #self.myStack=None

size = int(input("Enter size of stack: "))
obj=Stack(size)
while True:
    
    print("1.push")
    print("2.display")
    print("3.pop")
    print("4.peek")
    print("5.delete stack")
    print("6.exit")
    choice = int(input("Enter your choice: "))
    if (choice==1):
        value = int(input("Enter value to push in stack: "))
        obj.push(value)
    elif (choice==2):
        obj.display()
    elif (choice==3):
        obj.pop()
    elif (choice==4):
        obj.peek()
    elif (choice==5):
        obj.deleteStack()
    elif (choice==6):
        sys.exit()

#stack using list - easy implementation
#stack using linked list  - fast perform ance


