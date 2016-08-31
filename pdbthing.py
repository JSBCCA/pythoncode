def find_authors(filename_list):
    """list -> set

    Returns a set of authors found in a list of filenames for PDB formatted
    files.

    >>> find_authors(['pdb0.txt', 'pdb1.txt', pdb2.txt])
    {'Bob bobberson', 'Adam yargg'}
    """
    authors_set = set()
    for filename in filename_list:
        with open(filename, 'r') as file:
            for line in file:
                line.strip().lower()
                if line.startswith('author'):
                    author = line[6:].strip()
                    authors_set.add[author]
                elif line == '':
                    continue
                else:
                    break
    return authors_set
