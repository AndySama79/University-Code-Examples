def split_names(names):
    first_names = []
    last_names = []
    for name in names:
        split_name = name.split(" ")
        first_names.append(split_name[0])

        # handling more than two string literals in the string: treating the first literal as first names and the last literal as last name, hence 0, -1, respectively

        if split_name[-1] != split_name[0]: last_names.append(split_name[-1]) # checks if there's only one string literal in the name
        else: last_names.append('') # append empty string if only a single component

    return first_names, last_names