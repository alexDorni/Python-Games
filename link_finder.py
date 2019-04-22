from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):  # page-url - base_url/index.html/ceva
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        # If the tag is a link ( HTML <a href="ceva" > NUMe </a> )
        if tag == 'a':
            for attribute, val in attrs:
                if attribute == "href":
                    url = parse.urljoin(self.base_url, val)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass


# link_finder = LinkFinder()
# link_finder.feed("cod html")
