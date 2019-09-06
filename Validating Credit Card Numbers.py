# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
for _ in range(N):
    s = input()
    #► It may have digits in groups of 4, separated by one hyphen "-". 
    if '-' in s and re.search('\d{4}-\d{4}-\d{4}-\d{4}',s):
        s = s.replace('-','')
    #► It must start with a 4, 5 or 6. 
    if not re.search('^[4-6]',s):
        print('Invalid')
        continue
    #► It must contain exactly 16 digits. 
    if not re.search('^\d{16}$',s):
        print('Invalid')
        continue
    #► It must only consist of digits (0-9). 
    #► It must NOT use any other separator like ' ' , '_', etc. 
    if re.search('[^\d]',s):
        print('Invalid')
        continue
    #► It must NOT have 4 or more consecutive repeated digits.
    if re.search(r'(\d)\1\1\1',s):
        print('Invalid')
        continue
    print('Valid')  
