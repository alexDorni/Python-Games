from itertools import islice

import pandas as pd
from matplotlib import pyplot as plt
import ast

from crawler.general import IMAGES


class StrategicalPlan:
    MAX_NR_WORDS = 10

    def __init__(self):
        self.file_csv = pd.read_csv("Links.csv")
        self.dict_file_words = {}

    def create_dict_file_words(self):
        for col_name in self.file_csv:
            col_dict = {}
            incrementer = 0
            for list_of_words in self.file_csv[col_name]:
                list_of_words = ast.literal_eval(list_of_words)  # Converts string of list into list of strings
                for word in list_of_words:
                    if word == "NULL":
                        continue
                    if word not in col_dict:
                        col_dict[word] = incrementer
                    else:
                        col_dict[word] += 1
            self.dict_file_words[col_name] = dict(
                                                  sorted(col_dict.items(),
                                                         key=lambda t: t[1],
                                                         reverse=True
                                                         )
                                                  )

    # TODO integrate it in the console app
    def visualize_strategy(self):

        for key in self.dict_file_words:
            key_word = list(islice(self.dict_file_words[key].keys(), StrategicalPlan.MAX_NR_WORDS))
            values = list(islice(self.dict_file_words[key].values(), StrategicalPlan.MAX_NR_WORDS))

            plt.barh(range(len(key_word)),
                     values,
                     tick_label=key_word)
            plt.xticks(rotation="vertical")
            plt.ylabel("Top words")
            plt.xlabel("Nr of words")
            plt.title(key)
            plt.gca().invert_yaxis()
            plt.savefig(IMAGES + "/{}_bar.png".format(key))


plan = StrategicalPlan()
plan.create_dict_file_words()
plan.visualize_strategy()

