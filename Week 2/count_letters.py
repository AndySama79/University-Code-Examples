def count_letters(str):
    # using isalpha() fails in case there are accented characters
    # therefore, had to use regEx to do the task
    import re
    count = (re.findall("[a-zA-Z]", str))
    return count