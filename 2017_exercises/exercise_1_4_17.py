def text_reverse(x):  # The entire text is reversed
    return x[::-1]


def word_reverse(x):  # each word is reversed
    # somehow call text_reverse on each word, but keep spaces and newlines
    return rev


with open("alice_in.txt", 'r') as file:
    alice = file.read()

tr = text_reverse(alice)
with open("reversed_alice.txt", 'w') as file:
    file.write(tr)

wr = word_reverse(alice)
with open("alice_words_reversed.txt", 'w') as file:
    file.write(wr)
