import os
from ingestion import load_file
from cleaning import clean_values
from stats import compute_stats

DATA_FOLDER = "data/"

def run_pipeline():
    for filename in os.listdir(DATA_FOLDER):
        filepath = os.path.join(DATA_FOLDER, filename)

        raw = load_file(filepath)
        cleaned = clean_values(raw)
        stats = compute_stats(cleaned)

        print(f"\nResults for {filename}:")
        print(f"  Count: {stats['count']}")
        print(f"  Mean:  {stats['mean']}")
        print(f"  Min:   {stats['min']}")
        print(f"  Max:   {stats['max']}")
