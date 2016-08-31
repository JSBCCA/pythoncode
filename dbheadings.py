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


def db_headings(dictionary):
    """dict -> set

    Returns a set of keys used in any of the dictionaries.

    >>>db_headings(x)
    {'author', 'forename', 'surname', 'notes', 'born', 'died'}
    """
    newset = set()
    for i in dictionary:
        for j in dictionary[i]:
            newset.add(j)
    return (newset)


print(db_headings(x))
