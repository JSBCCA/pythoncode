from random import choice


def generate_chars(n):
    """ int -> string """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # new_string = ''
    # for l in range(n):
    #     new_string += choice(letters)
    # print(new_string)
    x = ''.join(map(lambda _: choice(letters), range(n)))
    print(x)


if __name__ == '__main__':
    generate_chars(3)
