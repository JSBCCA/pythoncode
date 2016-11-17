list_of_list = []
with open("Sacramentorealestatetransactions.csv", 'r') as file:
    for line in file:
        list_of_list.append(line.split(","))
# take input
highest_price = int(input())
lowest_price = int(input())
# find info based on input
new_list = []
for item in list_of_list[1:]:
    if (int(item[9]) >= lowest_price) and (int(item[9]) <= highest_price):
        new_list.append(item)
# show homes
for h in new_list:
    print("\n${}\n{}, {}, {}, {}".format(h[9], h[0], h[1], h[2], h[3]))
