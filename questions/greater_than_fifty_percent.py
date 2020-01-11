import csv
import datetime
import itertools
import json
import os
import pandas
import pdb
import pprint


THRESHOLD = 50
INPUT_FILE_PATH = '/home/dave/Downloads/list for dave.txt'
OUTPUT_FILE_PATH = os.path.abspath('%s.csv' % datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
COL_NAME = 'Overarching Entity (Short Name)'
COL_SHARES = 'Shares of A+B+C'
COL_PERCENT = '% of (A+B+C)'


df = pandas.read_table(INPUT_FILE_PATH)
df = df.iloc[:, range(3)]
df[COL_PERCENT] = df[COL_PERCENT].map(lambda x: x.rstrip('%'))
df[COL_PERCENT] = df[COL_PERCENT].astype(float)
df.sort_values(by=COL_PERCENT, ascending=False, inplace=True)

#unique_combinations = []
num_results = 0

with open(OUTPUT_FILE_PATH, 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')

    header = ['num', 'total percent']
    for i in range(len(df)):
        header.append("%s (%s)" % (df[COL_NAME][i], df[COL_PERCENT][i]))
    csv_writer.writerow(header)

    for sequence_length in range(1, 30):
        print(sequence_length)
        
        for indexes in itertools.combinations(range(len(df)), sequence_length):
            percents = df[COL_PERCENT][list(indexes)].values

            if sum(percents) >= THRESHOLD:
                num_results += 1

                row = [sequence_length, sum(percents)]
                funds = [""] * len(df)
                for index in indexes:
                    funds[index] = "x"
                row.extend(funds)

                csv_writer.writerow(row)

                print("%s : %s" % (sequence_length, num_results))

print(OUTPUT_FILE_PATH)
