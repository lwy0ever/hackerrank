# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(input())
phonebook = {}
for _ in range(n):
    name,phone = input().split()
    #phonebook.update({name:phone})
    phonebook[name] = phone
#print(phonebook)
for query in sys.stdin:
    query = query.rstrip('\r\n')
    phone = phonebook.get(query,'')
    if phone != '':
        print('%s=%s' % (query,phone))
    else:
        print('Not found')
'''
while True:
    query = input()
    if len(query) > 0:
        phone = phonebook.get(query,'')
        if phone != '':
            print('%s=%s' % (query,phone))
        else:
            print('Not found')
    else:
        break
'''
