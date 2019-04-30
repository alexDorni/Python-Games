import argparse
from crawler.crawler import *


def main(args):
    try:
        crawler = Crawler(project_name=args.proj_name,
                          home_page=args.url_page,
                          nr_threads=args.nr_threads)
        crawler.create_workers()
        crawler.run()
    except Exception as e:
        print(e, "\nInvalid arguments see crawler_exe.py --help")


if __name__ == '__main__':
    """
    Making a console application
    """
    # TODO put into a txt multiple links, take automate all the links in different folders
    # TODO make data processing using keywords/ make a another folder for each of them
    # TODO check what words are the most use in links ( plot them )
    # TODO try to build a strategy to be more efficient

    parser = argparse.ArgumentParser(description="Web crawler")
    parser.add_argument("--proj_name", help="Project name for the folder", default='')
    parser.add_argument("--url_page", help="Home page url you want to crawl", default='')
    parser.add_argument("--nr_threads", help="Number of threads your PC can handle", type=int, default=8)
    args = parser.parse_args()
    main(args)
