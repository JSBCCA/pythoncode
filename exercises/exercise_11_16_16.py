list_of_list = []
with open("Sacramentorealestatetransactions.csv", 'r') as file:
    for line in file:
        list_of_list.append(line.split(","))
# make list of sell prices
sales_list = []
for sale in list_of_list[1:]:
    sales_list.append(int(sale[9]))
# print
print("Highest: $" + str(max(sales_list)))
print("Lowest: $" + str(min(sales_list)))
av = round(sum(sales_list) / len(sales_list), 2)
print("Average: $" + str(av))
