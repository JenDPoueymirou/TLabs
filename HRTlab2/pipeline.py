from ingestion import load_raw_file, list_data_files   # import ingestion functions
from cleaning import clean_records                     # import cleaning function
from stats import compute_stats                        # import stats function


def process_all_files():                               # define main pipeline function
    filepaths = list_data_files()                      # get list of all data file paths

    for filepath in filepaths:                         # loop through each file
        raw = load_raw_file(filepath)                  # load raw lines
        cleaned = clean_records(raw)                   # clean malformed records
        stats = compute_stats(cleaned)                 # compute descriptive statistics

        print(f"\nResults for {filepath}:")            # print file header
        print(f"  Count: {stats['count']}")            # print count
        print(f"  Mean:  {stats['mean']}")             # print mean
        print(f"  Min:   {stats['min']}")              # print minimum
        print(f"  Max:   {stats['max']}")              # print maximum


if __name__ == "__main__":                             # run pipeline only when executed directly
    process_all_files()                                # call main pipeline function
