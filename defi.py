from math import pi
import os
import time


# sum([n, n, n...]) adds any number of variables
def add(a, b):
    return a + b


def subtract(a, b):  # subtracts one number from another
    return a - b
# print (subtract(8, 3))


def multiply(a, b):  # multiplies two numbers
    return a * b
# print (multiply(5, 3))


def double(n):  # doubles a number
    return n * 2
# print (double(7))


def triple(n):  # triples a number
    return n * 3
# print (triple(5))


def divide(a, b):  # divides one number by another
    return a / b
# print (divide(8, 4))


def half(n):  # deduces half of a number
    return n / 2
# print (half(4))


def celsius_conv(f):  # takes a temperature in degF and converts to degC
    if f == 0:
        return -17.7778
    else:
        return (f - 32.0) * (5.0 / 9.0)
# print (celsius_conv(94))

c_c = celsius_conv


def fahrenheit_conv(c):  # takes a temp in degC and converts to degF
    if c == 0:
        return 32
    else:
        return c * (9.0 / 5.0) + 32
# print (fahrenheit_conv(49))


def p_t(a, b):  # uses the Pythag. theorem to deduce what C is
    return ((a * a + b * b)**(1 / 2))
# print (p_t(3, 4))


def p_t2(c, a):  # uses the Pythag. theorem to deduce what A or B is
    return ((c * c - a * a)**(1 / 2))
# print (p_t2(5, 3))


def square(c):  # squares a number
    return (c * c)
# print (square(5))


def square_root(n):  # gives the square root of a number
    return (n**(1 / 2))
# print (square_root(25))


def cube(c):  # cubes a number
    return (c**3)
# print (cube(4))


def feet_to_yards(n):  # converts feet into yards
    return (n * (1 / 3))
# print (f_y(1))

f_y = feet_to_yards


def inches_to_centi(n):  # converts inches to centimeters
    return (n * 2.54)
# print (i_c(10))

i_c = inches_to_centi


def inches_to_feet(n):  # converts inches to feet
    return (n / 12)
# print (i_f(11))

i_f = inches_to_feet


def feet_to_inches(n):  # converts feet to inches
    return (n * 12)
# print (f_i(30))

f_i = feet_to_inches


def miles_to_kilom(n):
    return n * 1.60934


def kilom_to_miles(n):
    return n * 0.621371


def blah(n):  # halves a number, then adds one
    return half(n) + 1
# print (blah(8))


def convert_mileage(mpg):  # converts mpg to liters per hundred km
    first = (100 * 3.785411784)
    second = (1.609344 * mpg)
    l_per_hundred_km = first / second
    return l_per_hundred_km
# print (convert_mileage(90))


def liters_needed(k, mpg):  # tells needed amount of liters
    first = convert_mileage(mpg)
    second = first / 100
    liters = second * k
    return liters
# print (liters_needed(50, 30))


def diff_from_10(x):
    return 10 - x


def add_5(x):
    return x + 5


def days_difference(day1, day2):  # gives number of days between 2 days
    return day2 - day1


def get_weekday(current_weekday, days_ahead):
    return (current_weekday + days_ahead - 1) % 7 + 1


def get_birthday_weekday(current_weekday, current_day, birthday_day):
    days_diff = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_diff)

    g_b_w = get_birthday_weekday


def pie_perc(n):
    """precondition: n > 0
    Assuming n people want to eat a pie,
    return the percentage each person gets to eat."""
    return int(100 / n)


def average_of_3(a, b, c):  # gives the average of 3 numbers
    return (a + b + c) / 3


def average_of_best_3(a, b, c, d):  # gives the average of the highest 3
    """Use numbers between 0 and 100"""
    first = min(a, b, c, d)
    second = (a + b + c + d - first)
    third = second / 3
    return third


def weeks_elapsed(day1, day2):  # deduces how many weeks are between 2 days
    first = abs(days_difference(day1, day2))
    second = first / 7
    third = int(second)
    return third


def circle_area(r):
    return pi * pow(r, 2)


def circumference(r):
    return (2 * (pi * r))


circum = circumference

# circum(r) = circumference(r)


def heart_disease(age, bmi):
    if age < 45:
        if bmi < 22.0:
            print("Low risk")
        else:
            print("Medium risk")
    else:
        if bmi < 22.0:
            print("Medium risk")
        else:
            print("High risk")


def different(a, b):
    print(a != b)
