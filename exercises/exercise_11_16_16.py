# put info into list of lists
list_of_list = []
with open("Sacramentorealestatetransactions.csv", 'r') as sret:
    for line in sret:
        sret_list = line.split(",")
        list_of_list.append(sret_list)
# get list of sell prices
sales_list = []
for sale in list_of_list[1:]:
    sales_list.append(int(sale[9]))
# find average
av = 0
for sell in sales_list:
    av += sell
av = av / len(sales_list)
# print
print("Highest: $" + str(max(sales_list)))
print("Lowest: $" + str(min(sales_list)))
print("Average: $" + str(round(av, 2)))
