from urllib.request import urlopen  # Connect web pages
from link_finder import LinkFinder
from general import *


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
        Spider.queue_file = Spider.project_name + "/crawled.txt"
        self.boot()
        self.crawl_page("First spider", Spider.base_url)  # Connect to a page

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)  # Faster operations
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        # Thread actions ( Spider )
        if page_url not in Spider.crawled:
            print(thread_name + " crawling " + page_url)
            print("Number of elements in queue " + str(len(Spider.queue)) +
                  " | Crawled " + str(len(Spider.crawled)))

            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)

            # Update the files
            Spider.update_files()


