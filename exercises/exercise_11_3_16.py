def secondhighest_thirdlowest(txt_file):
    # opens file and saves as a set
    with open(txt_file, 'r') as file:
        data_set = set(file.read().splitlines())
    # removes first highest and first/second lowest
    data_set.remove(max(data_set))
    data_set.remove(min(data_set))
    data_set.remove(min(data_set))
    # returns second highest and third lowest
    return str(txt_file) + " third lowest: " + str(min(data_set)) + '\n' + str(
        txt_file) + " second highest: " + str(max(data_set))


# py.test exercise_11_3_16.py --cov=exercise_11_3_16.py --cov-report=html
def test_secondhighest_thirdlowest():
    assert secondhighest_thirdlowest(
        "data_1.txt") == """data_1.txt third lowest: 13.2
data_1.txt second highest: 84.9"""
    assert secondhighest_thirdlowest(
        "data_2.txt") == """data_2.txt third lowest: 12.5
data_2.txt second highest: 88.9"""
    assert secondhighest_thirdlowest(
        "data_3.txt") == """data_3.txt third lowest: 10.9
data_3.txt second highest: 89.6"""


if __name__ == "__main__":
    print(secondhighest_thirdlowest('data_1.txt'))
    print(secondhighest_thirdlowest('data_2.txt'))
    print(secondhighest_thirdlowest('data_3.txt'))
