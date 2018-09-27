from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print(tag)
    
    def error(self, message):
        pass
    
finder = LinkFinder()
finder.feed('<html><head><title>Document</title></head>'
            '<body><h1>Hello World</h1></body></html>')
