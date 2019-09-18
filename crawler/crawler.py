import threading
from queue import Queue
from crawler.spider import Spider
from crawler.domain import *
from crawler.general import *


class Crawler:

    def __init__(self, home_page="", nr_threads=8):
        self.home_page = home_page
        self.domain = get_domain_name(self.home_page)
        self.project_name = CRAWLER_OUTPUT + self.domain
        self.queue_file = self.project_name + "/queue.txt"
        self.crawled_file = self.project_name + "/crawled.txt"
        self.number_of_threads = nr_threads

        self.queue_of_jobs = Queue()
        self.spider = Spider(self.project_name,
                             self.home_page,
                             self.domain)

    def run(self):
        queued_links = file_to_set(self.queue_file)
        if len(queued_links) > 0:
            print("Queue size \n" + str(len(queued_links)) + " links in the queue \n")
            self.create_jobs(queued_links)

    def create_jobs(self, queued_links=[]):
        for link in queued_links:
            self.queue_of_jobs.put(link)
        # Doesn't collide with the read and write
        self.queue_of_jobs.join()  # Done the creation of job (put link)
        self.run()

    def create_workers(self):
        for _ in range(self.number_of_threads):
            # What to do this worker; you specify a target work
            t = threading.Thread(target=self.work)
            t.daemon = True  # This thing dies when the main exits
            t.start()

    def work(self):
        while True:
            # Takes each link from the queue
            url = self.queue_of_jobs.get()
            Spider.crawl_page(threading.current_thread().name, url)
            self.queue_of_jobs.task_done()
