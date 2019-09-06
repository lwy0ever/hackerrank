# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for _ in range(T):
    s = input()
    #print(s)
    '''
    if len(s) != 10:
        print('Invalid')
        continue
    '''
    if not re.search(r'[a-zA-Z0-9]{10}',s):
        print('Invalid')
        continue
    if not re.search(r'[A-Z].*[A-Z]',s):
        print('Invalid')
        continue
    if re.search(r'[^a-zA-Z0-9]',s):
        print('Invalid')
        continue
    if not re.search(r'\d.*\d.*\d',s):
        print('Invalid')
        continue
    if re.search(r'(.).*\1',s):
        print('Invalid')
        continue
    print('Valid')
