import os                                              # import os to work with file paths and directories

DATA_FOLDER = "data/"                                  # folder containing raw heart-rate files


def load_raw_file(filepath):                           # define a function to load one raw file
    raw_lines = []                                     # list to store decoded lines

    with open(filepath, "rb") as f:                    # open the file in binary mode
        for line in f:                                 # loop through each raw line
            decoded = line.decode("utf-8").strip()     # decode bytes to string and strip whitespace
            raw_lines.append(decoded)                  # add cleaned line to list

    return raw_lines                                   # return list of raw decoded lines


def list_data_files():                                 # define a function to list all files in data folder
    return [                                           # return a list of file paths
        os.path.join(DATA_FOLDER, f)                   # join folder and filename
        for f in os.listdir(DATA_FOLDER)
        if f.endswith(".txt")               # loop through files in data folder
    ]