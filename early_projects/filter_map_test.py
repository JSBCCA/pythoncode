"""map() and filter():

('list' only a literal list if you call list over it)

map(func, list) -> Returns 'list' with func applied to items.

strings = map(str, [hello, world])
strings == ['hello', 'world']

filter(func, list) -> Returns 'list' of items that func already applies to.

even = filter(lambda n: n % 2, [3, 4, 5, 6])
even == [4, 6]
"""


def circle_area(r):
    return 3.14 * (r * r)


nums = input(
    "Please type each of the radii values. Separate with spaces. Ex: '5 3 86 11 4'\n").split(
        " ")
# nums = map(int, nums)
# radii = list(map(circle_area, nums))
# list(map(print, radii))
#  # for i in radii:
#  #     print(i)

for i in nums:
    x = circle_area(int(i))
    print(x)
