def get_num_words(string):
    """
    Returns the number of words in the string.
    """

    words = string.split()

    return len(words)

def get_freq_dict(string):
    """
    Returns a dictionary with the frequency of each character in the string.
    """

    freq_dict = {}

    for char in string:
        char = char.lower()
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1

    return freq_dict


def sort_by_count(dict):
    """
    Helper function to extract the 'count' value from a dictionary.
    Used for sorting the list of dictionaries by the 'count' key.
    """

    return dict['count']

def sort_freq_dict(freq_dict):
    """
    Sorts the frequency dictionary by the 'count' value in descending order.
    Returns a list of dictionaries with 'char' and 'count' keys.
    """
    
    if not freq_dict:  # Handle the edge case of an empty dictionary
        return []

    # Convert dictionary to list of dictionaries with 'char' and 'count' keys
    sorted_list_of_dict = [{'char': key, 'count': value} for key, value in freq_dict.items()]


    # Sort the list of dictionaries based on the 'count' key in descending order
    sorted_list_of_dict.sort(key=sort_by_count, reverse=True)

    return sorted_list_of_dict