"""
Use additional letters for duplicates:
Hank Pym ## hpym@basecampcodingacademy.org
Henry Pym ## hepym@basecampcodingacademy.org

Write the email addresses to a new txt file in alphabetical order:

Anthony, Sean ## santhony@basecampcodingacademy.org
Pym, Hank ## hpym@basecampcodingacademy.org
Pym, Henry ## hepym@basecampcodingacademy.org
"""

with open('enrollment.txt', 'r') as file:
    users = file.read().strip().lower().split('\n')

full_list = []
for i in users:
    names = i.split(' ')
    full_list.append(names)

final_list = []
test_list = []
for i in full_list:
    x = i[1].title() + ', ' + i[0].title() + ' ## '
    y = i[0][0] + i[1][:] + '@basecampcodingacademy.org'
    if y in test_list:
        y = i[0][0] + i[0][1] + i[1][:] + '@basecampcodingacademy.org'
        if y in test_list:
            y = i[0][0] + i[0][1] + i[0][2] + i[
                1][:] + '@basecampcodingacademy.org'
        else:
            test_list.append(y)
    else:
        test_list.append(y)
    z = x + y
    final_list.append(z)

with open('e_addresses.txt', 'w') as file:
    for i in sorted(final_list):
        file.write(i + '\n')
