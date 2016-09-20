txt = input("Enter your space separated entries:\n").strip().lower()
sym = "1234567890)(*&^%$#@!-=_+][}{\\|;:\'\"/?>.<,"
print(sorted(set((''.join(c for c in txt if c not in sym)).split()) - set("")))
