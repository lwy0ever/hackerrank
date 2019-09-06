# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
text = ''
for _ in range(N):
    text += input()
#print(text)
text = re.sub('<!--.*?-->','',text)
#print(text)
for tag in re.findall('<([^/][^>]*)>',text):
    #print(tag)
    if ' ' in tag:
        print(tag.split()[0])
        for att,val in re.findall('([a-z-]+)="([^"]+)"',tag):
            print('-> ' + att + ' > ' + val)
    else:
        print(tag)
#print(text)
