import os

from crawler.general import file_to_set, set_to_file, CRAWLER_OUTPUT


class FileParser:
    DIR_CLEANER = "FILES_CLEANED/"

    def __init__(self, num_of_threads=8):
        self.number_of_threads = num_of_threads
        self.files_dict = {}
        self.data_statistics = set()

    def create_dict_files(self, folder_output):
        try:
            for root, sub_dirs, files in os.walk(folder_output):
                if not files:
                    continue
                sub_folder = root.split('/')
                self.files_dict[sub_folder[1]] = root + '/' + files[0]
        except Exception as e:
            print(e)

    def output_file(self, key_word):
        try:
            for key, val in self.files_dict.items():
                cleaned_folder = FileParser.DIR_CLEANER + key
                if not os.path.exists(cleaned_folder):
                    os.makedirs(cleaned_folder)
                lines = file_to_set(val)
                data_links = {link for link in lines if key_word.lower() in link.lower()}
                set_to_file(data_links, cleaned_folder + '/' + key_word + ".txt")
        except Exception as e:
            print(e)


f = FileParser()
f.create_dict_files(CRAWLER_OUTPUT)
f.output_file("fortnite")
