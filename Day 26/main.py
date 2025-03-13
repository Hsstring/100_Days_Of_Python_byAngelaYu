# TODO 1. Create a dictionary in this format:

import pandas

data_file = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data_file.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato = [data_dict[alphabet] for alphabet in word]
print(nato)
