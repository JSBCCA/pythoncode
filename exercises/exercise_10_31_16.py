with open('phone_data.txt', 'r') as file:
    phone_numbers = file.read().strip().split('\n')


# change phone numbers to (555) 555-5555 format and add them to new_phone_data.txt
def change_format(phonelist):
    with open('new_phone_data.txt', 'w') as file:
        for p in phonelist:
            if len(p) == 10:
                file.write('(' + str(p[:3]) + ') ' + str(p[3:6]) + '-' + str(p[
                    6:]) + '\n')
            elif len(p) == 11:
                file.write('(' + str(p[1:4]) + ') ' + str(p[4:7]) + '-' + str(
                    p[7:]) + '\n')
            elif len(p) == 12:
                file.write('(' + str(p[:3]) + ') ' + str(p[4:7]) + '-' + str(p[
                    8:]) + '\n')
            elif len(p) == 14:
                file.write('(' + str(p[2:5]) + ') ' + str(p[6:9]) + '-' + str(
                    p[10:]) + '\n')
            else:
                file.write("???????????\n")


if __name__ == '__main__':
    change_format(phone_numbers)
