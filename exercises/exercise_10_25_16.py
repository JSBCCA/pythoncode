def pig_latin(text_input):
    final = ""  # create final string, couples, and split text_input
    couples = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl',
               'gr', 'ph', 'pl', 'pr', 'qu', 'sh', 'sk', 'sl', 'sm', 'sn',
               'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
    split_text = text_input.strip().lower().split()
    for i in range(len(split_text)):  # test for symbols and numbers
        if not split_text[i].isalpha():
            return "Invalid."
    for i in range(len(split_text)):  # test passed, convert to pig latin
        word = split_text[i]
        if word[0] in 'aeiou':  # vowel rule
            if i == 0:
                final += word.title()
            else:
                final += word
        elif word[0:2] in couples:  # first two letters rule
            if i == 0:
                final += word[2:].title()
            else:
                final += word[2:]
            final += word[0:2]
        else:  # regular rule
            if i == 0:
                final += word[1:].title()
            else:
                final += word[1:]
            final += word[0]
        final += 'ay '  # add 'ay'
    return final.strip()


if __name__ == '__main__':
    text = input("Give words: ")
    print(pig_latin(text))
