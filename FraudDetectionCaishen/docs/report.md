# Fraud Detection - Report
**1. Which insights did you gain from your EDA?**
Fraud is heavily concentrated: it only occurs in TRANSFER and CASH_OUT transaction types (0% in CASH_IN, DEBIT, PAYMENT). Fraud transactions also involve much larger amounts on average (~$1.47M vs ~$178K legit) and tend to drain the origin account to $0. The naive isFlaggedFraud rule (amount > 200,000) catches only 16 of 8,213 fraud cases, confirming a simple threshold is far too weak. A correlation heatmap showed oldbalanceOrg/newbalanceOrig and oldbalanceDest/newbalanceDest are near-perfectly correlated with each other but not with isFraud individually - the real signal comes from the difference between them, not the raw values.

**2. How did you determine which columns to drop or keep?**
Dropped nameOrig and nameDest (unique identifiers, no predictive value) and isFlaggedFraud (EDA showed it misses 99.8% of fraud, so including it as a feature risked misleading the model rather than helping it). Kept all other columns and engineered balance_diff_orig (oldbalanceOrg - newbalanceOrig) directly from the EDA finding that fraud drains accounts.

**3. Which hyperparameter tuning strategy did you use? Why?**
RandomizedSearchCV over GridSearchCV, given the large dataset size and time constraints - RandomizedSearch explores a wide hyperparameter space in far fewer iterations (10 vs. an exhaustive grid), which was necessary to keep training time practical.

**4. How did your model's performance change after tuning?**
Baseline RandomForestClassifier already performed strongly (F1 0.97 for the fraud class). After tuning (n_estimators=200, max_depth=20, min_samples_split=2, min_samples_leaf=1), F1 was 0.966 - essentially unchanged. This suggests the engineered features (particularly balance_diff_orig) provided most of the predictive power, making the model relatively insensitive to hyperparameter choices.

**5. What was your final F1 score? Precision vs. recall interpretation?**
Final F1: 0.966 (precision 0.97, recall 0.96 for the fraud class). Precision means 97% of transactions flagged as fraud were actually fraud - few false alarms. Recall means the model caught 96% of all actual fraud cases - few missed frauds. For a bank, both matter: high precision avoids annoying customers with false fraud alerts, while high recall minimizes actual fraud losses. This model balances both well.
