HRTLab2 Writeup — Heart‑Rate Data Pipeline
1. Overview of the Pipeline

This lab implements a modular Python pipeline that processes raw heart‑rate data collected across four phases (phase0.txt–phase3.txt).
The raw files contain:

    Numeric heart‑rate values

    Blank lines

    "NO DATA" entries

    Occasional malformed records

The pipeline performs three major steps:

    Ingestion — reading raw text files from the data/ directory

    Cleaning — removing invalid or missing values

    Statistics — computing count, mean, min, and max

The project demonstrates modular design, separation of concerns, and reproducible data processing.
2. Data Cleaning Strategy

The cleaning logic was designed to match the actual structure of the Phase0–Phase3 files.
A valid heart‑rate record must:

    Contain only digits

    Not be blank

    Not equal "NO DATA"

    Fall within a realistic physiological range (30–250 bpm)

All other lines are discarded.

This ensures that the downstream statistics reflect only meaningful physiological data.
3. Statistical Results

After cleaning, the pipeline produced the following descriptive statistics:
Phase	Count	Mean (bpm)	Min	Max
phase0	63	64.59	54	93
phase1	54	87.30	56	110
phase2	60	85.18	54	117
phase3	86	60.65	50	99
4. Interpretation of Results
Phase 0 — Baseline / Rest

    Lower mean (≈64 bpm)

    Narrow range (54–93 bpm)

    Indicates resting or low‑activity conditions

Phase 1 — High Activity

    Highest mean (≈87 bpm)

    Max reaches 110 bpm

    Suggests moderate to vigorous activity

Phase 2 — Sustained Activity

    Mean remains high (≈85 bpm)

    Max reaches 117 bpm

    Indicates continued exertion

Phase 3 — Cooldown / Recovery

    Lowest mean (≈60 bpm)

    Lowest minimum (50 bpm)

    Suggests recovery or rest after activity

5. Reflection on the Pipeline Design

The modular structure made debugging and iteration straightforward:

    When cleaning logic was mismatched to the data format, only cleaning.py needed modification.

    The ingestion and statistics modules required no changes.

    The pipeline orchestrator (pipeline.py) remained stable throughout.

This mirrors real‑world data engineering workflows, where modularity reduces risk and accelerates iteration.
6. Possible Extensions

Future improvements could include:

    Variance and standard deviation

    Matplotlib line plots

    CSV export of cleaned data

    Automated anomaly detection

These additions would deepen the analysis and improve interpretability.
7. Conclusion

The completed pipeline successfully:

    Ingested raw heart‑rate data

    Cleaned malformed and missing records

    Computed meaningful descriptive statistics

    Revealed clear differences between rest, activity, and recovery phases

The project demonstrates practical data engineering skills and a clear understanding of modular pipeline design.