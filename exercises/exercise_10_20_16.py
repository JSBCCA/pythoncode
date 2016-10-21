"""
Total the transaction costs for each person in cust_info_login.txt in the file transactions.txt.
Rank the customers at the end of the line in the file.
(1 = highest total of transactions).
First Last _ custid _ username _ password _ rank
"""


def user_dic(user_l):
    """ list(dict) -> dict """
    id_user = {}
    for u in user_l:
        id_user[u['custID']] = u
    return id_user


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


def read_users(string):
    """ str -> list[dict] """
    user_strings = string.splitlines()
    return list(map(read_user, user_strings))


with open('cust_info_login.txt') as file:
    cust_list = read_users(file.read())

customers = user_dic(cust_list)

with open('transactions.txt') as file:
    transactions = file.read().splitlines()

trans_info_s = list(map(lambda s: s.split(), transactions))
trans_info = list(map(lambda x: [x[0], float(x[1])], trans_info_s))

for transaction in trans_info:
    customers[transaction[0]]['total'] += transaction[1]

for i in customers:
    customers[i]['total'] = round(customers[i]['total'], 2)

print(customers)
"""
{'72925': {'username': 'todinson', 'rank': 0, 'password': '8tw4vm',
'total': 28710.69, 'custID': '72925', 'first': 'Thor', 'last': 'Odinson'},

 '96956': {'username': 'ppotts', 'rank': 0, 'password': 'pepper',
 'total': 30759.04, 'custID': '96956', 'first': 'Pepper', 'last': 'Potts'},

 '67935': {'username': 'wjohnson', 'rank': 0, 'password': 'b7kdwb',
 'total': 28472.96, 'custID': '67935', 'first': 'Will', 'last': 'Johnson'},

 '99115': {'username': 'jjackson', 'rank': 0, 'password': 'c2j402',
 'total': 32174.94, 'custID': '99115', 'first': 'Jackie', 'last': 'Jackson'},

 '63572': {'username': 'smcqueen', 'rank': 0, 'password': 'y5ze9w',
 'total': 32574.650000000005, 'custID': '63572', 'first': 'Steve', 'last': 'McQueen'},

 '18516': {'username': 'llane', 'rank': 0, 'password': '5h7820',
 'total': 33059.31, 'custID': '18516', 'first': 'Lois', 'last': 'Lane'},

 '47713': {'username': 'bbanner', 'rank': 0, 'password': '2luot3',
 'total': 32985.159999999996, 'custID': '47713', 'first': 'Bruce', 'last': 'Banner'},

 '92957': {'username': 'zstardust', 'rank': 0, 'password': '1337zs',
 'total': 28278.37, 'custID': '92957', 'first': 'Ziggy', 'last': 'Stardust'},

 '35423': {'username': 'mjackson', 'rank': 0, 'password': 'lonson',
 'total': 32317.04, 'custID': '35423', 'first': 'Marlon', 'last': 'Jackson'},

 '66469': {'username': 'mbrando', 'rank': 0, 'password': 'apples',
 'total': 30962.159999999996, 'custID': '66469', 'first': 'Marlon', 'last': 'Brando'},

 '83736': {'username': 'skyle', 'rank': 0, 'password': '7q9111',
 'total': 32781.780000000006, 'custID': '83736', 'first': 'Selina', 'last': 'Kyle'},

 '61884': {'username': 'swonder', 'rank': 0, 'password': 'abcdef',
 'total': 28818.020000000008, 'custID': '61884', 'first': 'Stevie', 'last': 'Wonder'},

 '87171': {'username': 'tjackson', 'rank': 0, 'password': 'f528i7',
 'total': 28166.409999999996, 'custID': '87171', 'first': 'Tito', 'last': 'Jackson'},

 '21627': {'username': 'rjackson', 'rank': 0, 'password': 'p03z32',
 'total': 35445.87999999999, 'custID': '21627', 'first': 'Randy', 'last': 'Jackson'},

 '42291': {'username': 'srogers', 'rank': 0, 'password': 'c26y5k',
 'total': 36976.600000000006, 'custID': '42291', 'first': 'Steven', 'last': 'Rogers'},

 '79476': {'username': 'ckent', 'rank': 0, 'password': 'u0hj1r',
 'total': 29245.699999999997, 'custID': '79476', 'first': 'Clark', 'last': 'Kent'},

 '89612': {'username': 'nprass', 'rank': 0, 'password': '9n94b8',
 'total': 28120.840000000015, 'custID': '89612', 'first': 'Natalie', 'last': 'Prass'},

 '46227': {'username': 'jjackson2', 'rank': 0, 'password': '0n9m7d',
 'total': 33893.03000000001, 'custID': '46227', 'first': 'Janet', 'last': 'Jackson'},

 '34565': {'username': 'maelius', 'rank': 0, 'password': '7lnimh',
 'total': 35100.75, 'custID': '34565', 'first': 'Marcus', 'last': 'Aelius'},

 '43726': {'username': 'mjackson1', 'rank': 0, 'password': '1at371',
 'total': 37185.56999999999, 'custID': '43726', 'first': 'Michael', 'last': 'Jackson'},

 '87151': {'username': 'nromanova', 'rank': 0, 'password': '7w5bzs',
 'total': 27688.059999999998, 'custID': '87151', 'first': 'Natalia', 'last': 'Romanova'},

 '59481': {'username': 'bwayne', 'rank': 0, 'password': 'batman',
 'total': 33467.62, 'custID': '59481', 'first': 'Bruce', 'last': 'Wayne'},

 '28621': {'username': 'tstark', 'rank': 0, 'password': 'irnman',
 'total': 29199.430000000008, 'custID': '28621', 'first': 'Tony', 'last': 'Stark'},

 '31779': {'username': 'jjackson1', 'rank': 0, 'password': '4mutfp',
 'total': 31573.65, 'custID': '31779', 'first': 'Jermaine', 'last': 'Jackson'}}
"""

# Read cust_info_login.txt.
# Make a list of lists, containing a person and their corresponding number.
# with open('cust_info_login.txt', 'r') as file:
#     customer_info_login = file.read().strip().split('\n')
# cust_info_log = list(map(lambda c: c.split(' _ '), customer_info_login))
#
# # read transactions.txt
# # Make a list of lists, containing a number and the amount spent on a transaction.
# with open('transactions.txt', 'r') as file:
#     customer_receipts = file.read().strip().split('\n')
# receipts = list(map(lambda c: c.split(' '), customer_receipts))
#
# # def sort_transactions(user_list):
# #     num_list = []
# #     for i in user_list:
# #         num_list.append(int(user_list[i][1]))
# #     sort(num_list)
# #     return (num_list)
# #
# #
# # def add_rank(user_list):
# #     ...
#
# # add transactions together
# amounts = []
# for person in cust_info_log:
#     amount = 0
#     for money in receipts:
#         if money[0] == person[1]:
#             amount += float(money[1])
#     amount = round(amount, 2)
#     amounts.append([amount, person[1]])
#
# # rank each amount
# sorted_amounts = sorted(amounts)
# for i in range(len(amounts)):
#     for si in range(len(sorted_amounts)):
#         if sorted_amounts[si][1] == amounts[i][1]:
#             amounts[i].append(sorted_amounts.index([si]))
#
# # add ranks to cust_info_log
# for i in range(len(cust_info_log)):
#     cust_info_log[i].append(amounts[i][2])
#
# # Write out everthing to cust_info_login.txt.
# with open('cust_info_login.txt', 'w') as file:
#     for i in range(len(cust_info_log)):
#         file.write(cust_info_log[i][0] + ' _ ' + cust_info_log[i][1] + ' _ ' +
#                    cust_info_log[i][2] + ' _ ' + cust_info_log[i][3] + ' _ ' +
#                    cust_info_log[i][4] + '\n')
