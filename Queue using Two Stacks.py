# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def Enqueue(self,e):
        self.stackIn.append(e)

    def Dequeue(self):
        self.i2o()
        return self.stackOut.pop()
    
    def Display(self):
        self.i2o()
        return self.stackOut[-1]
    
    def i2o(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())

q = Queue()
for _ in range(int(input())):
    op = list(map(int,input().split()))
    #print(op)
    if op[0] == 1:
        q.Enqueue(op[1])
    elif op[0] == 2:
        q.Dequeue()
    elif op[0] == 3:
        print(q.Display())
    else:
        print('type error')
