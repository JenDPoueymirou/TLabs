def clean_heartrate_data(raw_lines):
    #create an empty list to strore valid integer heart-rate values
    cleaned_values = []
    
    #create counter to track how many rows were skipped
    skipped_rows = 0
    
    #loop through each raw line from the file
    for line in raw_lines:
        
        #remove whitespace and new line characters from the line
        value_str = line.strip()

        #skip empty lines (blank rows in the file)
        if value_str == "":
            skipped_rows += 1
            continue

        # any value that contains non-digit character (e.g., "NO DATA")
        if not value_str.isdigit():
            skipped_rows += 1
            continue

        #convert the cleaned string into an integer
        value = int(value_str)

        #Check if the value is within a realistic heart-rate range
        if 30 <= value <=220:
            #Add valid values to the cleaned list
            cleaned_values.append(value)
        else:
            #Count values outside the valid range as skipped
            skipped_rows += 1
    
    #Return the cleaned list and the number of skipped rows
    return cleaned_values, skipped_rows

if __name__ == "__main__":
    run("Data/phase0.txt")

