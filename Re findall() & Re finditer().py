# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
v = 'aeiouAEIOU'
c = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
a = re.findall(r'(?<=[%s])([%s]{2,})[%s]' % (c,v,c),s)
print('\n' . join(a or ['-1']))
'''
if a:
    for r in a:
        print(r)
else:
    print(-1)
'''
