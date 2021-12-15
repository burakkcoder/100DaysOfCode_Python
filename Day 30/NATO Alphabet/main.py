import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = dict(zip(data['letter'], data ['code']))

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [data_dict[letter] for letter in word]
    except:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()