text = input("What text would you like to analyze? ")
letters = ''.join(c for c in text if c.isalpha())
vowels = ''.join(c for c in text if c.lower() in "aeiou")
print("-".join(letters), "\nTotal Text Length:", str(len(text)),
      "\nNumber of Letters:", str(len(letters)), "\nNumber of Vowels:",
      str(len(vowels)))

# t = input('What text would you like to analyze? ')
# l = (''.join(c for c in t if c.isalpha()))
# print('-'.join(l), '\nTotal Text Length:', str(len(t)), '\nNumber of Letters:',
#       str(len(l)), '\nNumber of Vowels:',
#       str(len(''.join(c for c in t if c.lower() in 'aeiou'))))
