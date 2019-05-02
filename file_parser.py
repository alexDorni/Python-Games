import os

from numpy import unicode

from crawler.general import CRAWLER_OUTPUT, file_to_set


class FileParser:
    DIR_CLEANER = "FILES_CLEANED/"

    def __init__(self, num_of_threads=8):
        self.output = CRAWLER_OUTPUT
        self.number_of_threads = num_of_threads
        self.files_dict = {}
        self.data_statistics = set()

    def create_dict_files(self):
        try:
            for root, subdirs, files in os.walk(self.output):
                if not files:
                    continue
                sub_folder = root.split('/')
                self.files_dict[sub_folder[1]] = root + '/' + files[0]

        except Exception as e:
            print(e)

    def parse_file(self, key_word=None):
        try:
            for _, val in self.files_dict.items():
                lines = file_to_set(val)
                for data in lines:
                    if key_word.lower() in data.lower():
                        data_split = data.split('/')
                        for word in data_split:
                            self.data_statistics.add(word)
            # print(self.data_statistics)
            # for i in self.data_statistics:
            #     print(i)
        except Exception as e:
            print(e)


# f = FileParser()
# f.create_dict_files()
# f.parse_file("starcraft")