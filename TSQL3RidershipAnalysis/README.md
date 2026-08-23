## Citibike Ridership Model

A daily ridership dataset for New York City's Citi Bike program, built by joining 50M+ individual trip records with LaGuardia Airport weather observations, to explore what drives daily demand.

### Repo structure

- `code/` — notebooks for EDA, preprocessing, and modeling (Part 2)
- `data/` — the exported, analysis-ready CSV (`citibike_weather_daily.csv`)
- `queries/` — the final SQL used to build the dataset (`build_dataset.sql`)
- `docs/` — data dictionary and supporting notes


## Part 2: Predicting Daily Ridership

**Data quality issues found & fixed:**
- `ride_date` loaded as string, not date — converted with `pd.to_datetime()`
- `precip_in` had 1 row coded as 99.99 (NOAA's missing-value sentinel) — converted to NaN, imputed as 0
- 186 days missing from the dataset (Oct 2016-Mar 2017 gap) — traced to the INNER JOIN in Part 1 dropping days where LaGuardia weather data was unavailable

**Features engineered:**
- One-hot encoded `day_of_week` (captures weekday/weekend commuter pattern)
- `days_since_launch` — trend feature capturing system growth over time (ridership roughly doubled 2013-2017)
- `temp_f_sq` — squared temperature term, capturing a "comfort ceiling" where extreme heat suppresses ridership rather than boosting it further
- Used only `temp_f` (not max/min) to avoid stacking near-collinear temperature columns

**Model performance:**
- Linear Regression, test R² = 0.752 (up from 0.744 baseline after adding temp²)
- MAE ≈ 6,950 rides — typical prediction is off by about that many rides per day
- Strongest effects: Sunday (-7,291 rides), Saturday (-5,650), precipitation (-3,874/inch), temperature (+567/°F)

**Biggest weakness & next steps:**
- Residuals drift over time — model under-predicts more in later years, suggesting the trend feature doesn't fully capture system growth (e.g., station count changes, membership growth)
- Would want: actual station/bike count by date, holiday calendar flag, and more granular weather (hourly, not just daily means) to improve accuracy further