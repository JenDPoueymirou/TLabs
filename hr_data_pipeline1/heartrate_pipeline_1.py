import os                                              # import os to work with files and directories

DATA_FOLDER = "data/"                                  # folder containing raw heart-rate files


def load_raw_file(filepath):                           # define a function to load one raw file
    raw_lines = []                                     # list to store decoded lines

    with open(filepath, "rb") as f:                    # open the file in binary mode
        for line in f:                                 # loop through each raw line in the file
            decoded = line.decode("utf-8").strip()     # decode bytes to string and strip whitespace
            raw_lines.append(decoded)                  # add the cleaned line to the list

    return raw_lines                                   # return the list of raw decoded lines


def clean_records(raw_lines):                          # define a function to clean malformed records
    cleaned = []                                       # list to store valid integer heart-rate values

    for line in raw_lines:                             # loop through each raw line
        if "|" not in line:                            # skip lines missing the delimiter
            continue                                   # continue to next line

        parts = line.split("|")                        # split the line into index and value
        if len(parts) != 2:                            # skip lines with incorrect structure
            continue                                   # continue to next line

        value_str = parts[1].strip()                   # extract the value portion and strip whitespace

        if value_str == "":                            # skip missing values
            continue                                   # continue to next line

        if not value_str.isdigit():                    # skip non-numeric values
            continue                                   # continue to next line

        value = int(value_str)                         # convert the string to an integer

        if value < 30 or value > 250:                  # skip impossible heart-rate values
            continue                                   # continue to next line

        cleaned.append(value)                          # add the valid value to the cleaned list

    return cleaned                                     # return the list of cleaned integer values


def compute_stats(values):                             # define a function to compute descriptive statistics
    if len(values) == 0:                               # handle case where no valid values exist
        return {                                       # return empty statistics
            "count": 0,
            "mean": None,
            "min": None,
            "max": None
        }

    total = 0                                          # running total for computing mean
    minimum = values[0]                                # initialize minimum with first value
    maximum = values[0]                                # initialize maximum with first value

    for v in values:                                   # loop through each cleaned value
        total += v                                     # add value to running total

        if v < minimum:                                # update minimum if needed
            minimum = v                                # assign new minimum

        if v > maximum:                                # update maximum if needed
            maximum = v                                # assign new maximum

    mean = total / len(values)                         # compute mean manually

    return {                                           # return statistics as a dictionary
        "count": len(values),
        "mean": mean,
        "min": minimum,
        "max": maximum
    }


def process_all_files():                               # define main pipeline function
    for filename in os.listdir(DATA_FOLDER):           # loop through each file in the data folder
        filepath = os.path.join(DATA_FOLDER, filename) # build full file path

        raw = load_raw_file(filepath)                  # load raw lines from file
        cleaned = clean_records(raw)                   # clean malformed or invalid records
        stats = compute_stats(cleaned)                 # compute descriptive statistics

        print(f"\nResults for {filename}:")            # print file header
        print(f"  Count: {stats['count']}")            # print number of valid records
        print(f"  Mean:  {stats['mean']}")             # print mean heart rate
        print(f"  Min:   {stats['min']}")              # print minimum heart rate
        print(f"  Max:   {stats['max']}")              # print maximum heart rate


if __name__ == "__main__":                             # run the pipeline only when script is executed directly
    process_all_files()                                # call the main pipeline function
