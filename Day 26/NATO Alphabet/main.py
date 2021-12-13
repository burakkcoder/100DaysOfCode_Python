import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = dict(zip(data['letter'], data ['code']))

word = input("Enter a word: ").upper()
output_list = []

for x in word:
    output_list.append(data_dict[x])

print(output_list)