import csv

import seaborn as sns
import matplotlib.pyplot as plt


class CsvCreator:

    # def clean_words(self, ):
    # TODO Put into a csv domain and word => plot it
    # TODO plot the shit
    # TODO think strategy for ML model | but first make the csv.

    def plot_statistics(self):
        sns.set(style="whitegrid")
        f, ax = plt.subplots(figsize=(6, 15))
        sns.load_dataset()

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
