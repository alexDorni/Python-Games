import csv
import os

from crawler.general import file_to_set, CRAWLER_OUTPUT


class FileParser:
    DIR_CLEANER = "FILES_CLEANED/"

    def __init__(self, num_of_threads=8):
        self.number_of_threads = num_of_threads
        self.files_dict = {}
        self.sub_links_split = []

        self.__create_dict_files()
        self.__create_list_of_dict()

    def __create_dict_files(self):
        try:
            for root, sub_dirs, files in os.walk(CRAWLER_OUTPUT):
                if not files:
                    continue
                sub_folder = root.split('/')
                self.files_dict[sub_folder[1]] = root + '/' + files[0]
        except Exception as e:
            print(e)

    def __create_list_of_dict(self):
        """
        Algorithm -> convert data from .txt files into csv

        Takes all the .txt files from a directory root (CRAWLER_OUTPUT) variable.

        Makes a list of dict with
                                [
                                    {
                                        key1 (folder_name_1/crawled.txt): value(line_1_of_folder_1),
                                        key2 (folder_name_2/crawled.txt): value(line_2_of_folder_2),
                                        ...,
                                    },
                                    ...
                                ]

        If the value is None for a line of a .txt file it will be NULL
        """
        try:
            flag = True
            nr_iter = 0
            while flag:
                dict_data = {}
                flag = False
                for key in self.files_dict.keys():
                    link_set = file_to_set(self.files_dict[key], nr_iter)
                    elem_link = list(link_set)[0].replace("\n", '').split(key)[1]
                    dict_data[key] = elem_link if elem_link != '/' else "NULL"
                    if dict_data[key] != "NULL":
                        flag = True
                        self.sub_links_split.append(dict_data)
                if flag:
                    nr_iter += 1

        except Exception as e:
            print(e)

    def create_csv_file(self):
        try:
            with open('Links.csv', 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, self.files_dict.keys())
                writer.writeheader()
                writer.writerows(self.sub_links_split)

        except Exception as e:
            print(e)
