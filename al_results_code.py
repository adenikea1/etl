import csv
import pandas as pd

with open("al_results_2020 (1).csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
#need to chnage to dataframe
    exclude = ('Absent', '-', ' ', '')

    iter_csv = iter(csv_reader)
    for row in iter_csv:
        for row in csv_reader:
            if any(val in exclude for val in row):
                continue
            else:

                print(row)

row.to_csv('results.csv')













