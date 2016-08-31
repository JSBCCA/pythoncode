#   You should complete the provided functions so that they pass all the
#   provided tests. To complete a function, remove the "pass" (which
#   is a statement to do nothing) and implement the function.
#
#   To test your code, simply run this module. If your module runs
#   clean (without errors), then you are done, congrats! If it displays
#   errors, you have code to write/fix!


def kilometers_to_miles(kilometers):
    """
    >>> kilometers_to_miles(1)
    0.6214
    >>> kilometers_to_miles(.5)
    0.3107
    >>> kilometers_to_miles(0)
    0.0
    >>> kilometers_to_miles(40)
    24.855999999999998
    """
    return kilometers * 0.6214


# Problem 2 : Sales Tax
#   sales_tax should PRINT the appropriate information as
#   described in the docstring below.
#
#   important information:
#       state tax:      4% of purchase price
#       county tax:     2% of purchase price
def sales_tax(purchase_cost):
    """
    >>> sales_tax(1)
    Purchase Amount: 1
    State Sales Tax: 0.04
    County Sales Tax: 0.02
    Total Sales Tax: 0.06
    Total Cost: 1.06
    >>> sales_tax(99.99)
    Purchase Amount: 99.99
    State Sales Tax: 3.9996
    County Sales Tax: 1.9998
    Total Sales Tax: 5.9994
    Total Cost: 105.98939999999999
    >>> sales_tax(5.95)
    Purchase Amount: 5.95
    State Sales Tax: 0.23800000000000002
    County Sales Tax: 0.11900000000000001
    Total Sales Tax: 0.35700000000000004
    Total Cost: 6.307
    """
    print("Purchase Amount: " + str(purchase_cost))
    first = (purchase_cost * .04)
    print("State Sales Tax: " + str(first))
    second = (purchase_cost * .02)
    print("County Sales Tax: " + str(second))
    third = first + second
    print("Total Sales Tax: " + str(third))
    print("Total Cost: " + str(purchase_cost + third))


# Problem 3 : Minimum Insurance
#   min_insurance should RETURN the minimum amount of insurance a
#   person should buy for a given building.
#
#   important information:
#       minimum recommended insurance:      80% of replacement cost
def min_insurance(replacement_cost):
    """
    >>> min_insurance(100000)
    80000.0
    >>> min_insurance(123456789)
    98765431.2
    >>> min_insurance(0)
    0.0
    >>> min_insurance(-54317890)
    -43454312.0
    """
    return (replacement_cost * .8)


# Problem 4 : Automobile Costs
#   auto_cost should PRINT the appropriate information as described
#   in the docstring below. The provided arguments are the monthly
#   costs for loan payments, insurance payments, gas, oil, tires,
#   and maintanence.
#
#   important information:
#       the numbers should be formatted to be floating point representations
#           with 2 decimal points
def auto_cost(loan, insurance, gas, oil, tires, maintenance):
    """
    >>> auto_cost(1, 1, 1, 1, 1, 1)
    Monthly Automobile Cost: 6.0
    Annual Automobile Cost: 72.0
    >>> auto_cost(100, 75, 100, 30, 50, 100)
    Monthly Automobile Cost: 455.0
    Annual Automobile Cost: 5460.0
    >>> auto_cost(50.5, 70.39, 30.24, 50, 100, 40.76)
    Monthly Automobile Cost: 341.89
    Annual Automobile Cost: 4102.68
    >>> auto_cost(1.00000002, 1.1, 1.129, 2.29, 98, 7)
    Monthly Automobile Cost: 110.52
    Annual Automobile Cost: 1326.24
    """
    first = round(float(loan + insurance + gas + oil + tires + maintenance), 2)
    second = round(float(first * 12), 2)
    print("Monthly Automobile Cost: " + str(first))
    print("Annual Automobile Cost: " + str(second))


# Problem 5 : Property Tax
#   property_tax should PRINT the appropriate information as described
#   in the docstring below.
#
#   important information:
#       assessment value:   60% of actual value
#       property tax:       $.64 for each $100 of the assessment value
def property_tax(actual_value):
    """
    >>> property_tax(10000)
    Assessment Value: 6000.0
    Property Tax: 38.4
    >>> property_tax(99999.95)
    Assessment Value: 59999.969999999994
    Property Tax: 383.999808
    """
    first = actual_value * .6
    print("Assessment Value: " + str(first))
    second = ((first / 100) * .64)  # jjksjkc
    print("Property Tax: " + str(second))


# Problem 6 : Body Mass Index
#   bmi should RETURN the body mass index from the provided weight (pounds)
# and height (inches).
#
#   important information:
#       bmi:    weight * 703 / height**2
def bmi(weight, height):
    """
    >>> bmi(160, 67)
    25.056805524615726
    >>> bmi(200, 72)
    27.121913580246915
    >>> bmi(120, 60)
    23.433333333333334
    """
    return (weight * 703) / (height**2)


# Problem 7 : Calories from Fat and Carbohydrates
#   calories should RETURN the amount of calories in a provided number of
#   fat grams and carbohydrate grams.
#
#   important information:
#       calories from fat:      9 * fat grams
#       calories from carbs:    4 * carb grams
def calories(fat, carbs):
    """
    >>> calories(5,20)
    125
    >>> calories(1,1)
    13
    """
    return (fat * 9) + (4 * carbs)


# Problem 8 : Stadium Seating
#   earnings should RETURN the total earnings provided the number of A, B,
#   and C class seats sold.
#
#   important information:
#       Class A seats cost $15.
#       Class B seats cost $12.
#       Class C seats cost $9.
def earnings(a, b, c):
    """
    >>> earnings(100, 100, 100)
    3600
    >>> earnings(50, 75, 100)
    2550
    >>> earnings(0, 1000, 79)
    12711
    """
    return (15 * a) + (12 * b) + (9 * c)


# Problem 9 : Paint Job Estimator
#   paint_job_estimator should PRINT the appropriate information as described
#   in the docstring below.
#
#   important information:
#       For every 115 square feet of wall space, 1 gallon of paint and 8 hours
#           of labor will be required.
#       Each hour of labor costs $20.
def paint_job_estimator(wall_space, paint_price):
    """
    >>> paint_job_estimator(50, 10)
    Gallons of paint required: 0.43478260869565216
    Hours of labor required: 3.4782608695652173
    Cost of paint: 4.3478260869565215
    Cost of labor: 69.56521739130434
    Total Cost: 73.91304347826086
    >>> paint_job_estimator(750, 15.95)
    Gallons of paint required: 6.521739130434782
    Hours of labor required: 52.17391304347826
    Cost of paint: 104.02173913043477
    Cost of labor: 1043.4782608695652
    Total Cost: 1147.5
    """
    first = (wall_space / 115)
    second = first * 8
    third = first * (8 * 20)
    fourth = first * paint_price
    print("Gallons of paint required: " + str(first))
    print("Hours of labor required: " + str(second))
    print("Cost of paint: " + str(fourth))
    print("Cost of labor: " + str(third))
    print("Total Cost: " + str(third + fourth))


# Problem 10 : Monthly Sales Tax
#   monthly_sales_tax should PRINT the appropriate information as described
#   in the docstring below.
#
#   important information:
#       State sales tax:    4% of sales
#       County sales tax:   2% of sales
def monthly_sales_tax(total_sales):
    """
    >>> monthly_sales_tax(123456.79)
    Monthly sales: 123456.79
    State sales tax: 4938.2716
    County sales tax: 2469.1358
    Total sales tax: 7407.4074
    >>> monthly_sales_tax(4321567.21)
    Monthly sales: 4321567.21
    State sales tax: 172862.6884
    County sales tax: 86431.3442
    Total sales tax: 259294.03260000004
    """
    first = total_sales * .04
    second = total_sales * .02
    third = first + second
    print("Monthly sales: " + str(total_sales))
    print("State sales tax: " + str(first))
    print("County sales tax: " + str(second))
    print("Total sales tax: " + str(third))

# DO NOT TOUCH #
# This is causes your code to be tested. If you edit this, you might
# cause your code to run
if __name__ == "__main__":
    import doctest
    doctest.testmod()
