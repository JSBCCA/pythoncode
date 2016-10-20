from exercise_10_20_16.py import *


def test_add_rank():
    user_list = ['Tony Stark', '28621', 'tstark',
                 'irnman'], ['Bruce Banner', '47713', 'bbanner', '2luot3']

    ranks = add_rank(user_list)

    assert ranks == ['Tony Stark', '28621', 'tstark', 'irnman', '2'
                     ], ['Bruce Banner', '47713', 'bbanner', '2luot3', '1']
