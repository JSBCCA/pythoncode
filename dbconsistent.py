x = {
    'jgoodall': {'surname': 'goodall',
                 'forename': 'jane',
                 'born': 1934,
                 'died': None,
                 'notes': 'primate researcher',
                 'author': ['in the shadow of man',
                            'the chimpanzees of gombe']},
    'rfranklin': {'surname': 'franklin',
                  'forename': 'rosalind',
                  'born': 1920,
                  'died': 1957,
                  'notes': 'contributed to discovery of DNA'},
    'rcarson': {'surname': 'carson',
                'forename': 'rachel',
                'born': 1907,
                'died': 1964,
                'notes': 'raised awareness of effects of ddt',
                'author': ['silent spring']}
}


def db_consistent(dict_in_dict):
    """

    Returns True iff every inner dictionary has the same keys.

    >>>db_consistent(x)
    False
    """

    listofsets = []
    for k in dict_in_dict:
        for d in dict_in_dict[k]:
            setofk = set()
            for dk in d:
                setofk.add(dk)
            listofsets.append(setofk)
    for i in range(1, len(listofsets)):
        if listofsets[i] != listofsets[i - 1]:
            return False
    return True


print(db_consistent(x))
