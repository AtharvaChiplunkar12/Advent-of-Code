import pandas as pd

file_path = 'day6_input.txt'

df = pd.read_csv(file_path, sep=':', header=None,  index_col=0, skipinitialspace=True)

df = df.transpose()
df['Time'] = df['Time'].str.replace(' ', '')
df['Distance'] = df['Distance'].str.replace(' ', '')



startWays = 0
last = int(df['Time'][1])
for initial in range(int(df['Time'][1])):
    if (int(df['Time'][1]) - initial)*initial > int(df['Distance'][1]):
        StartWays=initial
        break

print((last-initial)-initial + 1)
