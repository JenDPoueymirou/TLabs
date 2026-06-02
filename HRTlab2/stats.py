def compute_stats(values):                             # define a function to compute descriptive statistics
    if len(values) == 0:                               # handle empty list
        return {                                       # return empty stats
            "count": 0,
            "mean": None,
            "min": None,
            "max": None
        }

    total = 0                                          # running total for mean
    minimum = values[0]                                # initialize minimum
    maximum = values[0]                                # initialize maximum

    for v in values:                                   # loop through values
        total += v                                     # update total

        if v < minimum:                                # update minimum if needed
            minimum = v                                # assign new minimum

        if v > maximum:                                # update maximum if needed
            maximum = v                                # assign new maximum

    mean = total / len(values)                         # compute mean manually

    return {                                           # return stats dictionary
        "count": len(values),
        "mean": mean,
        "min": minimum,
        "max": maximum
    }
