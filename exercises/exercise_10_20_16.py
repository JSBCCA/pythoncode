# First Last _ custid _ username _ password _ rank


# change list of dictionaries into dictionary of dictionaries
def user_dict(user_l):
    """ list(dict) -> dict """
    id_user = {}
    for u in user_l:
        id_user[u['custID']] = u
    return id_user


# change string to dictionary of info
def read_user(str):
    """ str -> dict """
    pieces = str.split()
    return {
        'first': pieces[0],
        'last': pieces[1],
        'username': pieces[5],
        'custID': pieces[3],
        'password': pieces[7],
        'rank': 0,
        'total': 0
    }


# change strings to dictionary of info
def read_users(string):
    """ str -> list[dict] """
    user_strings = string.splitlines()
    return list(map(read_user, user_strings))


# sort totals
def sort_totals(cust):
    """ dict[dict] -> list[list] """
    trans_list = []
    for i in cust:
        trans_list.append([cust[i]['total'], i])
    trans_list = sorted(trans_list, reverse=True)
    return trans_list


def add_rank(customers, sorted_totals):
    """ list[list] -> dict[dict] """
    # get customer id
    cust_list = []
    for i in customers:
        cust_list.append(i)
    # add rank
    for i in range(len(customers)):
        for j in range(len(sorted_totals)):
            if cust_list[i] == sorted_totals[j][1]:
                customers[cust_list[i]]['rank'] = sorted_totals.index(
                    sorted_totals[j]) + 1
    return customers

# open cust_info_login.txt and make a dictionary
with open('cust_info_login.txt') as file:
    cust_list = read_users(file.read())
customers = user_dict(cust_list)

# open transactions.txt
with open('transactions.txt') as file:
    transactions = file.read().splitlines()

# map transactions and make a list
trans_info_s = list(map(lambda s: s.split(), transactions))
trans_info = list(map(lambda x: [x[0], float(x[1])], trans_info_s))

# change totals
for transaction in trans_info:
    customers[transaction[0]]['total'] += transaction[1]

# round totals
for i in customers:
    customers[i]['total'] = round(customers[i]['total'], 2)

# sort the totals in a separate list
sorted_totals = sort_totals(customers)

# make the final dictionary
final = add_rank(customers, sorted_totals)

# Write out everthing to cust_info_login.txt.
with open('cust_info_login.txt', 'w') as file:
    for item in final:
        file.write(final[item]['first'] + ' ' + final[item]['last'] + ' _ ' +
                   final[item]['custID'] + ' _ ' + final[item]['username'] +
                   ' _ ' + final[item]['password'] + ' _ ' + str(final[item][
                       'rank']) + '\n')
