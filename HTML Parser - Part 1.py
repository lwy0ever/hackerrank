# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for k,v in attrs:
            print('-> %s > %s'%(k,v))
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for k,v in attrs:
            print('-> %s > %s'%(k,v))

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
N = int(input())
text = ''
for _ in range(N):
    text += input() + '\n'
parser.feed(text)
#parser.feed("<html><head><title>HTML Parser - I</title></head>"
#            +"<body><h1 en hoho=oh>HackerRank</h1><br /></body></html>")
