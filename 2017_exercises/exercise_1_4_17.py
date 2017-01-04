with open("alice_in.txt", 'r') as alice:
    x = alice.read()

with open("reversed_alice.txt", 'w') as file:
    file.write(x[::-1])

rev = " ".join(w[::-1] for w in x.split())
with open("alice_words_reversed.txt", 'w') as file:
    file.write(rev)

# def text_reverse(x):  # The entire text is reversed
#     return x[::-1]
#
#
# def word_reverse(x):  # each word is reversed
#     rev = " ".join(w[::-1] for w in x.split())
#     return rev
#
#
# with open("alice_in.txt", 'r') as file:
#     alice = file.read()
#
# tr = text_reverse(alice)
# with open("reversed_alice.txt", 'w') as file:
#     file.write(tr)
#
# wr = word_reverse(alice)
# with open("alice_words_reversed.txt", 'w') as file:
#     file.write(wr)
