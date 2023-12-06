import pandas as pd

file_path = 'day6_input.txt'

df = pd.read_csv(file_path, sep=' ', header=None,  index_col=0, skipinitialspace=True)

df = df.transpose()

total = 1
for ixd, row in df.iterrows():
    start = 0
    last = int(row['Time:'])
    for initial in range(int(row['Time:'])):
        if (int(row['Time:']) - initial)*initial > int(row['Distance:']):
            start = initial
            break

    total *= ((last-start)-start + 1)
print(total)