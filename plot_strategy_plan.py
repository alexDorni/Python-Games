import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import ast


class StrategicalPlan:

    def __init__(self):
        self.file_csv = pd.read_csv("Links.csv")
        self.dict_file_words = {}

    def create_dict_file_words(self):
        for col_name in self.file_csv:
            col_dict = {}
            incrementer = 0
            for list_of_words in self.file_csv[col_name]:
                list_of_words = ast.literal_eval(list_of_words)  # Converts string of list into list
                for word in list_of_words:
                    if word == "NULL":
                        continue
                    if word not in col_dict:
                        col_dict[word] = incrementer
                    else:
                        col_dict[word] += 1
            self.dict_file_words[col_name] = col_dict
        # print(self.dict_file_words)

    # TODO plot the first 10 sorted values
    def visualize_strategy(self):
        index = 0
        fig, axes = plt.subplots(nrows=2, ncols=2)
        for key in self.dict_file_words:
            df = pd.DataFrame.from_dict(self.dict_file_words[key], orient="index")
            df.plot(kind="bar", ax=axes[0, index])
            index += 1
        plt.show()


plan = StrategicalPlan()
plan.create_dict_file_words()
plan.visualize_strategy()

