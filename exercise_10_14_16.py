import sys

# get people and numbers
with open('cust_info.txt', 'r') as file:
    customer_info = file.read().strip().split('\n')
cust_info = map(lambda c: c.split(' _ '), customer_info)

# get numbers and transactions
with open('receipts.txt', 'r') as file:
    customer_receipts = file.read().strip().split('\n')
cust_receipts = map(lambda c: c.split(), customer_receipts)

# loop over ID question
lock = True
while lock is True:
    ID = input("Please enter your customer ID. Type 'Q' to quit. ").upper()
    for person in cust_info:
        if ID == 'Q':
            sys.exit()
        elif ID == person[1]:
            lock = False
            print('\n' + person[0])
            spent_sum = 0
            for spent in cust_receipts:
                if ID == spent[0]:
                    print(spent[1])
                    spent_sum += float(spent[1])
            spent_sum = round(spent_sum, 2)
            print('Sum: ' + str(spent_sum))
