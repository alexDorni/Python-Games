import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


# Factory with jobs to do
# Each spider will have a queue with jobs to do
PROJECT_NAME = "how_to_be_pro_at_fortnite"
HOME_PAGE = "https://docs.python.org"
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
# TODO CHECK WHAT NUMBER OF THREADS OF PC
NUMBER_OF_THREADS = 8

queue_of_jobs = Queue()
# Test here
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)
# End test


# JOBS
# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print("Queue size \n" + str(len(queued_links)) + " links in the queue \n")
        create_jobs()


# Each link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue_of_jobs.put(link)
    # Doesn't colide with the read and write
    queue_of_jobs.join()  # Done the creation of job (put link)
    crawl()


# Threads (Spiders)
# Create worker threads when main exits
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        # What to do this worker; you specify a target work
        t = threading.Thread(target=work)
        t.daemon = True  # This thing dies when the main exits
        t.start()


# Do the next job in the queue
def work():
    while True:
        # Takes each link from the queue
        url = queue_of_jobs.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue_of_jobs.task_done()
