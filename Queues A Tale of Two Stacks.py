class MyQueue(object):
    def __init__(self):
        self.old2new = []
        self.new2old = []
    
    def peek(self):
        self.digest()
        return self.new2old[-1]
        
    def pop(self):
        self.digest()
        return self.new2old.pop()
        
    def put(self, value):
        self.old2new.append(value)
    
    def digest(self):
        if not self.new2old:
            while self.old2new:
                self.new2old.append(self.old2new.pop())

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

