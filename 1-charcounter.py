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
sentence = input("Place your sentence here: ")
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
print(f"Number of Words: {word_count}")
print(f"Number of Vowels: {vow_count}")
print(f"Number of consonants: {cons_count}")