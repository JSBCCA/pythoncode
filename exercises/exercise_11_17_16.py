with open("Sacramentorealestatetransactions.csv", 'r') as file:
    sret_list = file.read().splitlines()  # open file
highest_price = int(input("Highest price: "))  # take input
lowest_price = int(input("Lowest price: "))  # take info
new_list = []  # create list to append info to
for item in sret_list[1:]:  # find info based on input
    info = item.split(",")  # split lines by commas
    if (int(info[9]) >= lowest_price) and (int(info[9]) <= highest_price):
        new_list.append(info)  # add info to list created earlier
for h in new_list:  # show homes
    print("\n${}\n{}, {}, {}, {}".format(h[9], h[0], h[1], h[2], h[3]))
