def get_students():
    """() -> list[String]
    """
    return ['james s', 'james h', 'keegan', 'onna', 'dustin', 'addey',
            'nicole', 'ricky', 'adam', 'jacob', 'martin', 'eddrick']


def is_in_BaseCamp(name):
    """(String) -> String
    """
    if name in get_students():
        print("Yes, " + (name.title()) + " is in Base Camp.")
        return None
    print("No, there is no " + (name.title()) + " in Base Camp.")


def sort_students_alpha():
    """() -> list[String]
    """
    return sorted(get_students())
