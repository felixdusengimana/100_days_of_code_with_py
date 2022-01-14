import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

keyword = input("What the word: ").upper()
output_list = [phonetic_dictionary[alph] for alph in keyword]
print(output_list)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
