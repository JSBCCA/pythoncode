# put all info into list of lists
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
for home in new_list:
    print("\n$" + home[9] + "\n" + home[0] + ", " + home[1] + ", " + home[2] +
          ", " + home[3])
