import json

# Load the words from the JSON file
with open('words_dictionary.json', 'r') as f:
    words = json.load(f)

# Filter and print 4-letter words consisting only of the letters a-f
for word in words:
    word = word.lower()
    if (len(word) == 4 or len(word) == 3) and all(c in 'abcdef' for c in word):
        print(word)
