# this function cleans raw heart-rate data and returns values and skipped  count
def clean_heartrate_data(raw_lines):
    #list to store valid integer heart-rate values
    cleaned_values = []
    
    #counter to track how many rows were skipped
    skipped_rows = 0
    
    #loop through each raw line from the file
    for line in raw_lines:
        
        #remove whitespace and new line characters from the line
        value_str = line.strip()

        #skip empty lines (blank rows in the file)
        if value_str == "":
            skipped_rows += 1
            continue

        #skip values containing non-digit characters
        if not value_str.isdigit():
            skipped_rows += 1
            continue

        #convert the cleaned string into an integer
        value = int(value_str)

        #check if the value is within a realistic heart-rate range
        if 30 <= value <=220:
            #add valid values to the cleaned list
            cleaned_values.append(value)
        else:
            #count values outside the valid range as skipped
            skipped_rows += 1
    
    #return the cleaned list and the number of skipped rows
    return cleaned_values, skipped_rows

#function to calculate the average of a list of numbers
def average(values):
    #accumulator for total
    total = 0

    #loop through values and accumlate total
    for v in values:
        total += v

    #compute average
    avg = total / len(values)

    #return computed average
    return avg

# function to calculate the median of a list of numbers
def median(values):
    # sort values to prepare for median calculation
    sorted_values = sorted(values)
    # determine number of values
    n = len(sorted_values)
    # compute median for odd count
    if n % 2 == 1:
        return sorted_values[n // 2]
    #compute median for even count
    mid1 = sorted_values[n // 2 - 1]
    mid2 = sorted_values[n // 2]
    return (mid1 + mid2) / 2


#function loads the file, cleans it, and prints results
def run(filepath):
    # Open the file and read all lines into a list
    with open(filepath, "r") as f:
        raw_lines = f.readlines()

    # Clean the raw lines using cleaning function
    cleaned, skipped = clean_heartrate_data(raw_lines)

    # Print the cleaned values to verify the function works
    print("Cleaned values:", cleaned)

    # Print how many rows were skipped
    print("Skipped rows:", skipped)

    #compute the average using new function
    avg = average(cleaned)

    # print the cleaned values to verify the function
    print("Average:", avg)
        
    #Compute median
    med = median(cleaned)
    print("Median:", med)

    #Compute range
    rng = range_values(cleaned)
    print("Range:", rng)

    #Compute rolling average
    roll = rolling_average(cleaned, 5)
    print("Rolling average (window=5):", roll)

#function to calculate rolling averages using a fixed window size
def rolling_average(values, window_size):
    #List for storing rolling average results
    results = []

    #Loop through valid starting positions for the window
    for i in range(len(values) - window_size + 1):
        total = 0
    
        #Loop through window elements
        for j in range(window_size):
            total += values[i + j]

        #Compute average for current window
        avg = total / window_size
        #Store result
        results.append(avg)
    #Return list or rolling averages
    return results

#Function to calculate the range of a list of numbers
def range_values(values):
    #Initialize minimum and maximum trackers
    min_value = values[0]
    max_value = values[0]

    #Loop through values to dinf minimum and maximum
    for v in values:
        if v < min_value:
            min_value = v
        if v > max_value:
            max_value = v
    
    #return range as max minus min
    return max_value - min_value

# main execution block
if __name__ == "__main__":
    run("Data/phase0.txt")

