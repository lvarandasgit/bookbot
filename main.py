# print("hello world")
#
# ----
# Ex. 1
def print_book_content(path_to_file):
    #
    with open(path_to_file) as f: # the "with" command ensures that the file is actually closed when the block is finished
        file_contents = f.read()
        print(file_contents)
# ----
# Ex. 2
def count_book_words(path_to_file):
    #
    with open(path_to_file) as f: # the "with" command ensures that the file is actually closed when the block is finished
        file_contents = f.read()
        words = file_contents.split()
        number_words = len(words)
        print(number_words)
# ----
# Ex. 3
def diction(path_to_file):
    #
    word_dictionary = {}
    unique = set() # set to track the presence of a letter to feed in the dictionary
    #
    with open(path_to_file) as f: # the "with" command ensures that the file is actually closed when the block is finished
        file_contents = f.read()
        words = file_contents.split()
        #
        for word in words:
            for character in word:
                character_small = character.lower()
                #
                if character_small not in unique: # this verifies if the character has been spotted before
                    unique.add(character_small) # this adds the character in the set
                    word_dictionary[character_small] = 1 # initiation of the key for the dictionary
                else:
                    word_dictionary[character_small] += 1
    #
    space_count = file_contents.count(' ') # counts the total number os spaces, since this is not retrieved with the "split" method
    word_dictionary[' '] = space_count
    # print(word_dictionary)
    return word_dictionary
# ----
# Ex. 4
def report(dicionario):
    # print(dicionario)
    #
    count_total = 0
    string_count = ''
    for letra in dicionario:
        if letra.isalpha():
            count_total += dicionario[letra]
            string_count += 'The \'' + str(letra) + '\' character was found ' + str(dicionario[letra]) + ' times'
            string_count += "\n"
    #
    string_final = '--- Begin report of books/frankenstein.txt ---'
    string_final += "\n"
    string_final += str(count_total) + ' words found in the document'
    string_final += "\n"; string_count += "\n"
    string_final += string_count
    string_final += '--- End report ---'
    #
    print(string_final)
        
    

path_to_file = 'books/frankenstein.txt'
# print_book_content(path_to_file)
# count_book_words(path_to_file)
dicionario = diction(path_to_file)
#
report(dicionario)