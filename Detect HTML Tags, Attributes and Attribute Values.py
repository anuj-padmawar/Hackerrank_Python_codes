# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->"," > ".join(attr))

parser = MyHTMLParser()

html = ""
for i in range(int(input())):
    html += input()
    html += '\n'

parser.feed(html)
