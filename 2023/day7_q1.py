import pandas as pd

card_values = {'K': 13, 'Q': 12, 'J': 11, 'T': 10, 'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def custom_sort(item):
    return (item[1][0], item[1][1], card_values.get(item[0][0]), card_values.get(item[0][1]), card_values.get(item[0][2]), card_values.get(item[0][3]), card_values.get(item[0][4]))

file_path = 'day7_input.txt'

df = pd.read_csv(file_path, sep=' ', header=None,  index_col=0, skipinitialspace=True)



sorting_list = []
#print(df)
for index, row in df.iterrows():
    check = dict()
    for character in index:
        if character in check:
            check[character] += 1
        else:
            check[character] = 1
    sorted_values = sorted(check.values())
    if len(sorted_values) == 1:
        sorted_values.append(5)
    sorting_list.append((index,(sorted_values[-1],sorted_values[-2]), row[1]))

sorting_list = sorted(sorting_list, key=custom_sort)
sum = 0
for i in range(len(sorting_list)):
    sum += (sorting_list[i][2]*(i+1))

print(sum)



