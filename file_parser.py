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

    def create_tsv_file(self):
        try:
            words_list = self.__split_data()
            with open("Links.tsv", 'w', newline='') as tsv_file:
                tsv_writer = csv.writer(tsv_file, delimiter=' ')
                for words in words_list:
                    tsv_writer.writerow(words)

        except Exception as e:
            print(e)

    def create_csv_file(self):
        try:
            self.__create_list_of_dict()
            with open("Links.csv", 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, self.files_dict.keys())
                writer.writeheader()
                writer.writerows(self.sub_links_split)

        except Exception as e:
            print(e)

    def __create_dict_files(self):
        try:
            for root, sub_dirs, files in os.walk(CRAWLER_OUTPUT):
                if not files:
                    continue
                sub_folder = root.split('/')
                self.files_dict[sub_folder[1]] = root + '/' + files[0]
            print(self.files_dict)
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
            # TODO Optimize the code
            flag = True
            nr_iter = 0
            while flag:
                dict_data = {}
                flag = False
                for key in self.files_dict.keys():
                    words_list = []
                    link_set = file_to_set(self.files_dict[key], nr_iter)

                    if next(iter(link_set)) != "NULL":
                        flag = True
                    else:
                        words_list.append("NULL")
                        dict_data[key] = words_list
                        continue

                    elem_link = list(link_set)[0].replace("\n", '')
                    if elem_link == '':
                        words_list.append("NULL")
                        dict_data[key] = words_list
                        continue

                    if elem_link.find(key) == -1:
                        words_list.append("NULL")
                        dict_data[key] = words_list
                        continue

                    elem_link = elem_link.split(key)[1]
                    elem_link = elem_link.split('/')  # Split the links
                    for var_list in elem_link:
                        if var_list != '':
                            elem_link = var_list.split('-')  # Split the words from the links
                            for word in elem_link:
                                words_list.append(word.replace(".html", ''))
                            dict_data[key] = words_list
                        else:
                            words_list.append("NULL")
                            dict_data[key] = words_list

                self.sub_links_split.append(dict_data)

                if flag:
                    nr_iter += 1
        except Exception as e:
            print(e)

    def __split_data(self):
        spliced_data = []
        for key, val in self.files_dict.items():
            links_list = list(file_to_set(val))
            for link in links_list:
                link = link.replace("\n", '')
                link = link.replace(".html", '').split(key)[1].split('/')
                for words in link:
                    if not words == '':
                        words = words.split('-')
                        spliced_data.append(words)
        return spliced_data


FileParser().create_tsv_file()


