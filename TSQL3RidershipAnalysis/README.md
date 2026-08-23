## Citibike Ridership Model

A daily ridership dataset for New York City's Citi Bike program, built by joining 50M+ individual trip records with LaGuardia Airport weather observations, to explore what drives daily demand.

### Repo structure

- `code/` — notebooks for EDA, preprocessing, and modeling (Part 2)
- `data/` — the exported, analysis-ready CSV (`citibike_weather_daily.csv`)
- `queries/` — the final SQL used to build the dataset (`build_dataset.sql`)
- `docs/` — data dictionary and supporting notes


## Part 2: Predicting Daily Ridership

**Data quality issues found & fixed:**
- `ride_date` loaded as string, rather than a date, so pandas couldn't  fo any date-based operations on it until converted with `pd.to_datetime()'
- `precip_in` had 1 row coded as 99.99, matching NOAA's documented missing-value sentinel for precipitation. This was converted to NaN, then imputed as 0 - a conservative choice given only 1 of 1,610 rows was affected and most days genuinely have 0 precipitation.
- 186 calendar days were missing from the dataset entirely, clustered mainly between October 2016 and March 2017. Tracing this back to Part 1's SQL, the gap came from the weather side: the LaQuardia station's records were incomplete for this period, and the INNER JOIN in Part 1 dropped any ride day that had no matching weather observation from LaGuardia weather data.

**Features engineered:**
- One-hot encoded `day_of_week` to capture weekday/weekend commuter pattern found in EDA.
- Added `days_since_launch` as a trend feature, since ridership grew substantially over the six-year window (roughly doubling from 2013 to 2017) - without this, the model has no way to know "what year it is."
- Added `temp_f_sq` — squared temperature term, after EDA showed ridership doesn't keep climbing indefinitely with heat - it plateaus and slightly dips on the hottest days. This lets a linear model capture that curve.
- Used only `temp_f` as the temperature feature (not 'max_temp_f' or 'min_temp_f'), since the three move almost perfectly together and including all three would produce unstable, misleading coefficients

**Model performance:**
- Linear Regression, test R² = 0.752 (up from 0.744 baseline after adding temp²)
- MAE ≈ 6,950 rides — typical prediction is off by about that many rides per day
- Strongest effects: Sunday (-7,291 rides), Saturday (-5,650), precipitation (-3,874/inch), temperature (+567/°F)

**Biggest weakness & next steps:**
- Residuals drift over time — model under-predicts more in later years, suggesting the trend feature doesn't fully capture system growth (e.g., station count changes, membership growth)
- Would want: actual station/bike count by date, holiday calendar flag, and more granular weather (hourly, not just daily means) to improve accuracy further
- Residual plots against date reveal drift over time: the model under-predicts more in later years than earlier ones, suggesting the trend feature doesn't fully capture the system's real growth (more stations, more bikes, more members over time.) To improve this, it would help to have the actual station count and bike fleet size by date, a holiday calendar flag ( since holidays likeley break normal weekday/weekend patterns), and more granular weather date - hourly rather than daily averages - to better capture how conditions change throughout a single day.