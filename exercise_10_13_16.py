with open('cust_info.txt', 'r') as file:
    customer_info = file.read().strip().split('\n')

# divider

cust_info = []
for c in customer_info:
    new = c.split(' _ ')
    if len(new) > 1:
        cust_info.append(new)

# divider

with open('receipts.txt', 'r') as file:
    customer_receipts = file.read().strip().split('\n')

# divider

cust_receipts = []
for c in customer_receipts:
    new = c.split(' ')
    if len(new) > 1:
        cust_receipts.append(new)

# divder

all_sum = 0
for spent in cust_receipts:
    all_sum += float(spent[1])
    all_sum = round(all_sum, 2)

# divider

all_cust_sums_list = []
for i in cust_info:
    cust_sums_list = []
    cust_sums_list.append(i[0])
    all_cust_sums_list.append(cust_sums_list)

# divider

for c in cust_info:
    amount = 0
    for n in cust_receipts:
        if n[0] == c[1]:
            amount += float(n[1])
    amount = round(float(amount), 2)
    all_cust_sums_list[cust_info.index(c)].append(amount)

# divider

with open('user_transactions_and_sum.txt', 'w') as file:
    for item in all_cust_sums_list:
        info = str(item[0]) + ": $" + str(item[1]) + '\n'
        file.write(info)
    final_sum = 'Sum: $' + str(all_sum)
    file.write(final_sum)
