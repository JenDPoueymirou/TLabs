# **HRTLab2 — Heart‑Rate Data Pipeline**

## 📌 Overview
This project implements a modular Python pipeline for ingesting, cleaning, analyzing, and reporting statistics on raw heart‑rate data collected across four phases (`phase0.txt`–`phase3.txt`).  
The raw files contain blank lines, `"NO DATA"` entries, and numeric values.  
The pipeline performs:

- Data ingestion  
- Data cleaning  
- Descriptive statistics  
- Modular, real‑world data engineering workflow  

---

## 📁 Project Structure

```
HRTLab2/
│
├── data/                 # Raw heart-rate files (phase0–phase3)
├── images/               # Optional: saved plots
│
├── ingestion.py          # File I/O functions
├── cleaning.py           # Data cleaning logic
├── stats.py              # Descriptive statistics
├── pipeline.py           # Orchestrates ingestion → cleaning → stats
├── hr_data_pipeline.py   # Entry point script
│
├── README.md             # Project documentation
└── writeup.md            # Lab writeup and analysis
```

---

## ⚙️ How the Pipeline Works

### **1. Ingestion (`ingestion.py`)**
- Lists `.txt` files in `data/`  
- Reads each file into memory  
- Returns raw lines for cleaning  

### **2. Cleaning (`cleaning.py`)**
Handles the actual format of the Phase0–Phase3 files:

- Strips whitespace  
- Skips blank lines  
- Skips `"NO DATA"`  
- Keeps only numeric values  
- Filters out unrealistic heart‑rate values (<30 or >250)  

### **3. Statistics (`stats.py`)**
Computes:

- Count  
- Mean  
- Minimum  
- Maximum  

### **4. Pipeline Orchestration (`pipeline.py`)**
For each file:

1. Load raw lines  
2. Clean the data  
3. Compute statistics  
4. Print results  

### **5. Entry Point (`hr_data_pipeline.py`)**
Run the entire pipeline with:

```
python hr_data_pipeline.py
```

---

## 📊 Example Output

```
Results for data/phase0.txt:
  Count: 63
  Mean:  64.5873
  Min:   54
  Max:   93

Results for data/phase1.txt:
  Count: 54
  Mean:  87.2963
  Min:   56
  Max:   110

Results for data/phase2.txt:
  Count: 60
  Mean:  85.1833
  Min:   54
  Max:   117

Results for data/phase3.txt:
  Count: 86
  Mean:  60.6512
  Min:   50
  Max:   99
```

---

## ▶️ How to Run

From the project root:

```
python hr_data_pipeline.py
```

Make sure the `data/` folder contains the four phase files.

---

## 🧠 Learning Objectives

This lab demonstrates:

- Modular Python design  
- File ingestion and directory traversal  
- Data cleaning and validation  
- Descriptive statistics  
- End‑to‑end pipeline orchestration  
- GitHub project structure and documentation  

---