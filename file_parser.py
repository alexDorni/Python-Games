import csv
import os

from crawler.general import file_to_set, set_to_file, CRAWLER_OUTPUT


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
        try:
            flag = True
            nr_iter = 0
            while flag:
                dict_data = {}
                flag = False
                for key in self.files_dict.keys():
                    link_set = file_to_set(self.files_dict[key], nr_iter)
                    dict_data[key] = list(link_set)[0].replace("\n", '')
                    if dict_data[key] != "NULL":
                        flag = True
                        self.sub_links_split.append(dict_data)
                print(self.sub_links_split)
                if flag:
                    nr_iter += 1
            print(self.sub_links_split)

        except Exception as e:
            print(e)

    def create_csv_file(self):
        with open('Links.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, self.files_dict.keys())
            writer.writeheader()
            print(self.sub_links_split)

            try:
                writer.writerows(self.sub_links_split)

            except Exception as e:
                print(e)


f = FileParser()
# f.create_dict_files(CRAWLER_OUTPUT)
f.create_csv_file()
