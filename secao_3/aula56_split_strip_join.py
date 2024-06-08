sentence = '     Look,     what a interesting thing'

split_sentence = sentence.split(',')
# print(split_sentence)

white_space_remove = []
for i in split_sentence:
    white_space_remove.append(i.strip())

restaured_sentence = ', '.join(white_space_remove)
print(restaured_sentence)