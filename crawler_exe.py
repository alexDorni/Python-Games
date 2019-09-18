import argparse
from crawler.crawler import *


def main(args):
    try:
        with open(args.links_file, 'r') as f:
            lines = f.read().splitlines()

        for line in lines:
            crawler = Crawler(home_page=line,
                              nr_threads=args.nr_threads)
            crawler.create_workers()
            crawler.run()
    except Exception as e:
        print(e, "\nInvalid arguments see crawler_exe.py --help")


if __name__ == '__main__':
    """
    Making a console application
    """

    parser = argparse.ArgumentParser(description="Web crawler")
    parser.add_argument("--links_file", help="A .txt file wich contains links to be crawled", default='')
    parser.add_argument("--nr_threads", help="Number of threads your PC can handle", type=int, default=8)
    args = parser.parse_args()
    main(args)
