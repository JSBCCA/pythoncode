text = input("What text would you like to analyze? ")
letters = ''.join(c for c in (text.replace(" ", "")) if c.isalpha())
vowels = ''.join(c for c in text if c.lower() in "aeiou")
print(("-".join(letters)), "\nTotal Text Length:", str(len(text)),
      "\nNumber of Letters:", str(len(letters)), "\nNumber of Vowels:",
      str(len(vowels)))
