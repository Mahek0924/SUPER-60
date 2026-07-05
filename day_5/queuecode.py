import sys
class Queue:
    def __init__(self,queueSize):
        self.queueSize = queueSize
        self.myQueue = []

    def isFull(self):
        if len(self.myQueue) == self.queueSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.myQueue == []:
            True
        else:
            False

    def enQueue(self,value):
        if self.isFull():
            print("Queue is full")
        else:
            self.myQueue.append(value)

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue = ", self.myQueue)
    
    def deQueue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            print(self.myQueue.pop(0))

    def frontPeek(self):
        if self.isEmpty():
            print("queue is empty")
        else: 
            print(self.myQueue[0])
    
    def deleteQueue(self):
        del self.myQueue
        #self.myStack=None

size = int((input("Enter the size of the queue:")))
queObj = Queue(size)
while(True):
    print("1. enQueue")
    print("2. display")
    print("3. deQueue")
    print("4. frontPeek")
    print("5. Delete Queue")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if (choice==1):
        value = int(input("Enter value to add in queue: "))
        queObj.enQueue(value)
    elif (choice==2):
        queObj.display()
    elif (choice==3):
        queObj.deQueue()
    elif (choice==4):
        queObj.frontPeek()
    elif (choice==5):
        queObj.deleteQueue()
    elif (choice==6):
        sys.exit()