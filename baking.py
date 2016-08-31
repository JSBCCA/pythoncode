import temp_program


def get_preheat_instructions(f):
    cels = str(temp_program.c_c(f))
    fahr = str(f)
    return "Preheat oven to " + fahr + " degrees F (" + cels + " degrees C)."


fahr = float(input("Enter the baking temperature in degrees Fahrenheit: "))
print(get_preheat_instructions(fahr))
