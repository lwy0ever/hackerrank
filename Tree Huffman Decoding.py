

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    cur = root
    ans = ''
    #print(s)
    for c in s:
        if c == '0':
            cur = cur.left
        else:
            cur = cur.right
        if cur.data != '\0':
            ans += cur.data
            cur = root
    print(ans)

