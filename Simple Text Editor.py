# Enter your code here. Read input from STDIN. Print output to STDOUT
def op(s,t,w):
    if t == 1:
        s += w
    elif t == 2:
        s = s[:-w]
    return s

s = ''
stack = []
for _ in range(int(input())):
    i = input().split()
    t = int(i[0])
    if t == 1:
        w = i[1]
        stack.append((2,len(w)))
        s = op(s,t,w)
    elif t == 2:
        w = int(i[1])
        stack.append((1,s[-w:]))
        s = op(s,t,w)
    elif t == 3:
        w = int(i[1]) - 1
        print(s[w])
    else:   # t == 4
        ot,w = stack.pop()
        s = op(s,ot,w)
    #print(t,s,stack)
