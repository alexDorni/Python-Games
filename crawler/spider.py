from urllib.request import urlopen  # Connect web pages
from crawler.link_finder import LinkFinder
from crawler.general import *


class Spider:
    """
     For each page start a spider
    """

    # Class variables share among all instances

    project_name = ''  # Project name
    base_url = ''
    domain_name = ''

    # Saved on drive to prevent electric crush
    queue_file = ''
    crawled_file = ''

    # Saved on RAM for quicker time
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + "/queue.txt"
        Spider.crawled_file = Spider.project_name + "/crawled.txt"
        self.boot()
        self.crawl_page("Thread 0", Spider.base_url)  # Connect to a page

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)  # Faster operations
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name='', page_url=''):
        # Thread actions ( Spider )
        if page_url not in Spider.crawled:
            print(thread_name + " crawling " + page_url)
            print("Number of elements in queue " + str(len(Spider.queue)) +
                  " | Crawled " + str(len(Spider.crawled)))

            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)

            # Update the files
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        # Convert the bytes 10001 into string ( The response is in bytes )
        html_string = ''
        try:
            # If the page link is correct; it's not a error from page or server etc.
            response = urlopen(page_url)

            # Check if the link is a page, not a pdf or executable etc.
            if response.info()["Content-Type"].split(";")[0] == "text/html":
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print("{} can not crawl this page". format(e))
            return set()
        return finder.page_links()

    # Take links from web page
    @staticmethod
    def add_links_to_queue(links):
        for url in links:

            if url in Spider.queue or Spider.crawled:
                continue

            # The domain is https://www.gamesradar.com     /how-to-play-fortnite/
            if Spider.domain_name not in url:
                continue

            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)


