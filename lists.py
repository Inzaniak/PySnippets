def flatten_list(in_list):
    """
    flatten a list of lists
    Args:
    - in_list: The list to flatten

    Return:
    - flattened list of lists
    """
    return [item for sublist in in_list for item in sublist]