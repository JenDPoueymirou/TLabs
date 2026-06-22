def clean_data(data):
    """
    Takes a list of strings read from a text file.
    skips the header, and returns a list of floats.
    """
    clean_data = []
    for value in data[1:]:   # skip header at index 0
        clean_data.append(float(value.strip()))
    return clean_data