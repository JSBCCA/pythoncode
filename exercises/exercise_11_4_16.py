# converts a string into a string of word lengths
def words_to_count(words):
    """str -> str"""
    result = ""
    words = words.strip().split()
    for word in range(len(words)):
        if words[word] == words[-1]:
            result += str(len(words[word]))
        else:
            result += str(len(words[word])) + " "
    return result


# py.test exercise_11_4_16.py --cov=exercise_11_4_16.py --cov-report=html
def test_words_to_count():
    assert words_to_count("I am a goofy goober!") == "1 2 1 5 7"
    assert words_to_count("") == ""


if __name__ == "__main__":
    with open("bacon.txt", 'r') as bacon:
        bacon_words = bacon.read()
    counted_words = words_to_count(bacon_words)
    with open("bacon_count.txt", 'w') as bacon_count:
        bacon_count.write(counted_words)
