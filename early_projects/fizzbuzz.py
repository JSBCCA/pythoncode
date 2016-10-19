def fizzbuzz(i):
    ''' int -> str
    If i is divisible by 3, return "Fizz".
    If i is divisible by 5, return "Buzz".
    If i is divisible by 3 and 5, return "FizzBuzz".'''

    if i % 3 == 0 and i % 5 == 0:
        return ("FizzBuzz")
    elif i % 3 == 0:
        return ("Fizz")
    elif i % 5 == 0:
        return ("Buzz")
    else:
        return (str(i))


numlist = range(1, 101)
for i in numlist:
    print(fizzbuzz(i))
