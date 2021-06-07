# Mad Libs Program


# Read in text from file
file = open('MadLibsText.txt', 'r')
sentence = file.read()
# Split the text into a list of words
split_sentence = sentence.split()
print(split_sentence)
# Prompt the user for a word for each occurrence of ADJECTIVE, NOUN, VERB
# in the text
[]
words_to_replace = ['adjective', 'noun', 'verb.']
for index, word in enumerate(split_sentence):
    if word.lower() in words_to_replace:
        if word.lower() == 'verb.':
            userInput = input(f"Enter an {word.lower()}\n")
            split_sentence[index] = userInput + '.'
        # Replace the word in the list with the user input
        else:
            userInput = input(f"Enter an {word.lower()}.\n")
            split_sentence[index] = userInput

# Join the list into a string
new_sentence = ' '.join(split_sentence)

print(new_sentence)
new_file = open('Result.txt', 'w')
new_file.write(new_sentence)

