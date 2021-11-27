# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

# steps:
# 1. ask for a sentence
sentence = input("\33[1m\33[3m\33[31mPlace your sentence here:\33[0m ")
# 2. count the number of words, vowels, and consonants
vow_count = 0
cons_count = 0
space_count = 0
word_count = len(sentence.split())

for count in sentence:
    if count == "a" or count == "e" or count == "i" or count == "o" or count == "u" or \
        count == "A" or count == "E" or count == "I" or count == "O" or count == "U":
        vow_count = vow_count + 1 # added to vowel count
    elif count == " ":
        space_count = space_count + 1
    else:
        cons_count = cons_count + 1 # added to consonant count


# 3. display
print(f"\33[1m\33[3m\33[32mNumber of Words:\33[0m \33[1m\33[33m{word_count}\33[0m")
print(f"\33[1m\33[3m\33[32mNumber of Vowels:\33[0m \33[1m\33[35m{vow_count}\33[0m")
print(f"\33[1m\33[3m\33[32mNumber of consonants:\33[0m \33[1m\33[34m{cons_count}\33[0m")