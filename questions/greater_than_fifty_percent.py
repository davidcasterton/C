import json
import pandas
import pdb


df = pandas.read_table('sample_data.txt')
df = df.iloc[:, range(3)]
col_name = 'Overarching Entity (Short Name)'
col_shares = 'Shares of A+B+C'
col_percent = '% of (A+B+C)'
df[col_percent] = df[col_percent].map(lambda x: x.rstrip('%'))
df[col_percent] = df[col_percent].astype(float)
df.sort_values(by=col_percent, ascending=False, inplace=True)


total = sum([float(x) for x in df[col_percent].values])
threshold = total / 2

results = {
    'sum of all percents': total,
    '50% of all percents' : threshold
}
for i in range(len(df)):
    for k in range(i, len(df)):
        percents = df[col_percent][i:k].values
        if sum(percents) >= threshold:
            result = {
                'sum': sum(percents), 
                'names': list(df[col_name][i:k].values),
                'shares': list(df[col_shares][i:k].values),
                'percents': list(percents)
            }
            try:
                results[len(percents)].append(result)
            except KeyError as e:
                results[len(percents)] = []
                results[len(percents)].append(result)

with open('cheers.json', 'w') as f:
    json.dump(results, f, indent=4)