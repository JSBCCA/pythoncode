from practice import *


def test_read_user():
    user_string = "Nate Clark _ 1337 _ natec425 _ notMyPass"

    user = read_user(user_string)

    assert user["first"] == "Nate"
    assert user["last"] == "Clark"
    assert user["custId"] == "1337"
    assert user["username"] == "natec425"
    assert user["password"] == "notMyPass"


def test_read_user2():
    user_string = "Gandalf Grey _ 1 _ ggm8 _ shallNotPass"

    user = read_user(user_string)

    assert user["first"] == "Gandalf"
    assert user["last"] == "Grey"
    assert user["custId"] == "1"
    assert user["username"] == "ggm8"
    assert user["password"] == "shallNotPass"


def test_read_users():
    user_string = "Nate Clark _ 1337 _ natec425 _ notMyPass\nGandalf Grey _ 1 _ ggm8 _ shallNotPass"

    users = read_users(user_string)

    assert len(users) == 2
    assert users[0]['first'] != users[1]['first']
    assert users[0]["first"] == "Nate"
    assert users[1]["first"] == "Gandalf"
