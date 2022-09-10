def find_lastname(firstname, names):

    for name in names:
        split_name = name.split(" ")
        if split_name[0] == firstname:
            if len(split_name) > 1:
                return split_name[-1]
            else:
                return '' # function returns empty string if there's no last name
    
    return None # function returns None if firstname is not found in the names list