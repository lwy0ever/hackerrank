# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

n = int(input())
for _ in range(n):
    e = input()
    #print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
    #print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
    s = email.utils.parseaddr(e)
    #print(s[1])
    if re.search(r'^[a-zA-Z][a-zA-Z0-9-\._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$',s[1]):
        print(email.utils.formataddr(s))
