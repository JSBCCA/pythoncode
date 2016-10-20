def read_user(string):
    """ str -> dict """
    parts = string.split()
    d = {'first': parts[0],
         'last': parts[1],
         'custId': parts[3],
         'username': parts[5],
         'password': parts[7]}
    return (d)


def read_users(string):
    """ str -> list[dict] """
    user_strings = string.splitlines()
    return list(map(read_user, user_strings))
