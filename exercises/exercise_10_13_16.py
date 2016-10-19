# Read cust_info.txt.

with open('cust_info.txt', 'r') as file:
    customer_info = file.read().strip().split('\n')

# Make a list of lists, containing a person and their corresponding number.

cust_info = []
for c in customer_info:
    new = c.split(' _ ')
    if len(new) > 1:
        cust_info.append(new)

# read receipts.txt

with open('receipts.txt', 'r') as file:
    customer_receipts = file.read().strip().split('\n')

# Make a list of lists, containing a number and the amount spent on a transaction.

cust_receipts = []
for c in customer_receipts:
    new = c.split(' ')
    if len(new) > 1:
        cust_receipts.append(new)

# Find the sum of all transactions by every person.

all_sum = 0
for spent in cust_receipts:
    all_sum += float(spent[1])
    all_sum = round(all_sum, 2)

# Make a list of lists containing only every person, for now.

all_cust_sums_list = []
for i in cust_info:
    cust_sums_list = []
    cust_sums_list.append(i[0])
    all_cust_sums_list.append(cust_sums_list)

# Match the numbers from both .txts, and add the transaction sums of each person
# to the list of lists from the last step. We have now matched each person with
# the amount of money they have spent.

for c in cust_info:
    amount = 0
    for n in cust_receipts:
        if n[0] == c[1]:
            amount += float(n[1])
    amount = round(float(amount), 2)
    all_cust_sums_list[cust_info.index(c)].append(amount)

# Write out every person and amount spent to user_transactions_and_sum.txt.
# Write the total sum of all transactions at the bottom.

with open('user_transactions_and_sum.txt', 'w') as file:
    for item in all_cust_sums_list:
        info = str(item[0]) + ": $" + str(item[1]) + '\n'
        file.write(info)
    final_sum = 'Sum: $' + str(all_sum)
    file.write(final_sum)
