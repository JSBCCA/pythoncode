# don't go above 20,000,000

# version for level up
x = int(input())
y = x / 2
while x > 1:
    x -= 1
    y += x
print(y)

# version for adding
# x = int(input())
# y = x
# while x > 1:
#     x -= 1
#     y += x
# print(y)
