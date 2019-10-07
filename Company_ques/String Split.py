# The program will recieve 3 English words inputs from STDIN
#
# These three words will be read one at a time, in three separate line
# The first word should be changed like all vowels should be replaced by $
# The second word should be changed like all consonants should be replaced by #
# The third word should be changed like all char should be converted to upper case
# Then concatenate the three words and print them
# Other than these concatenated word, no other characters/string should or message should be written to STDOUT
#
# For example if you print how are you then output should be h$wa#eYOU.
#
# You can assume that input of each word will not exceed more than 5 chars



three_wrd_input = input()

list_of_words = ''.join(three_wrd_input).split()
print(list_of_words)


if len(list_of_words) == 3:

    first_word = list_of_words[0]
    first_word = ' '.join(first_word).split()

    for i in first_word:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            first_word[first_word.index(i)] = '$'

    list_of_words[0] = "".join(first_word)


    second_word = list_of_words[1]
    second_word = ' '.join(second_word).split()

    for j in second_word:
        if j != 'a' and j != 'e' and j != 'i' and j != 'o' and j != 'u':
            second_word[second_word.index(j)] = '#'
    list_of_words[1] = ''.join(second_word)



    list_of_words[2] = list_of_words[2].upper()


else:
    print("only 3")

print(*list_of_words)