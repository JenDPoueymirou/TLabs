# shopping-behavior — American Consumer Shopping Analysis

## 📌 Overview
This project analyzes a dataset of 3,900 simulated shopping transactions for FlashFash, an online shopping company, to uncover seasonal purchasing patterns, the effect of promotional codes on spending, and customer review behavior.

## 📁 Project Structure
shopping-behavior/
│
├── data/
│   ├── raw/                    # Original shopping.csv
│   └── processed/
│       └── shopping_cleaned.csv
│
├── analysis.ipynb              # Full analysis, charts, and findings
├── README.md                   # Project documentation

## Required Analytical Questions
#### 1. What are the most popular colors by season?
Fall: Brown (97), Burnt Orange (93), Terra Cotta (91)
Spring: Baby Blue (69), White (63), Lavender (55)
Summer: Lavender (102), Lemon Yellow (98), Baby Blue (84)
Winter: Black (124), Burnt Orange (112), Aubergine (111)
#### 2. What is the most popular clothing item by season?
Fall: Backpack & Sweater tied (72), Socks (71)
Spring: Running Shoes (89), Sunglasses & T-shirt tied (80)
Summer: Shorts (152), Sunglasses (135), Running Shoes (134)
Winter: Leggings (118), Backpack & Sweater tied (113)
#### 3. What is the effect of promo codes on the dollar amount of purchases?
Customers who used a promo code spent an average of $50.07, compared to $30.16 for those who didn't — a $19.91 increase associated with promo code use.
#### 4. When do users leave a review?
Only 1,138 of 3,158 customers (36%) left a review; 2,020 (64%) did not. (Note: the dataset only records whether a review was left, not detailed timing data like days-after-purchase — so this answers "how often," not "when" in a time-based sense. Worth keeping in mind if the assignment expects a more literal time-based answer.)

## Findings
### Question 1: Most Popular Colors by Season
Fall favors warm earth tones: Brown (97), Burnt Orange (93), Terra Cotta (91)
Spring favors cool/light colors: Baby Blue (69), White (63), Lavender (55)
Summer favors bright colors: Lavender (102), Lemon Yellow (98), Baby Blue (84)
Winter favors dark/bold colors: Black (124), Burnt Orange (112), Aubergine (111)

### Question 2: Most Popular Clothing Items by Season
Fall: Backpack & Sweater tied (72), Socks (71)
Spring: Running Shoes (89), Sunglasses & T-shirt tied (80)
Summer: Shorts (152), Sunglasses (135), Running Shoes (134)
Winter: Leggings (118), Backpack & Sweater tied (113)

### Question 3: Effect of Promo Codes on Purchase Amount
Customers without promo codes spent an average of $30.16
Customers with promo codes spent an average of $50.07
Promo codes are associated with a $19.91 increase in average spending

### Question 4: When Do Users Leave a Review
Only 1,138 of 3,158 customers left a review (36%)
2,020 customers did not leave a review (64%)

## 🧠 Learning Objectives
This lab demonstrates:
Exploratory data analysis on real-world-style transactional data
Grouping and aggregation with pandas
Data visualization with matplotlib
Translating raw statistics into business-relevant findings

## My Analytical Questions
What are 6 analytical questions you can ask about this dataset?

### 1. How does the average purchase amount vary across different age groups?
Purchase amounts are remarkably consistent across age groups, all clustering tightly between $38.52–$39.76
50s spent the most on average ($39.76), <20 spent second-most ($38.88) — but the spread across all groups is under $1.25, suggesting age has little to no meaningful effect on spending amount

### 2. Which seasons show the highest total purchase volume, and how does this relate to item categories?
Winter drives the highest total revenue ($40,168), followed by Fall ($33,954), Summer ($29,643), and Spring ($18,806) — over double Spring's volume
Top-grossing item per season: Winter → Leggings ($4,615), Summer → Shorts ($5,888, the single highest of any season/item combo), Fall → Backpack ($2,851), Spring → Running Shoes ($3,576)

### 3. Do customers who use promo codes tend to spend more or less money than those who do not use promo codes?
Matches the required-questions finding: promo code users spent $50.07 on average vs. $30.16 for non-users — a $19.91 difference

### 4. Which demographic group has the highest frequency of purchases?
By gender: Non-binary customers had the highest average previous purchases (8.10), notably above Male (5.90) and Female (5.78)
By age group: customers under 20 had the highest average previous purchases (6.51), with a general downward trend as age increases (50s and 60+ lowest, ~5.37–5.38)

### 5. Are certain payment methods associated with higher-value transactions?
Bank Transfer users had the highest average purchase amount ($43.34), notably above all other methods
Cash transactions were lowest on average ($36.55); the remaining methods (Debit Card, PayPal, Venmo, Credit Card) clustered closely together (~$38.61–$39.03)

### 6. Which U.S. states generate the highest revenue, and how does this correlate with previous purchase history?
California led in total revenue ($3,115.70), followed by Nebraska, Delaware, and Montana
No clear correlation between a state's total revenue and its customers' average previous-purchase count — e.g., Illinois had the lowest revenue in the top 10 ($2,743) but the highest avg. previous purchases (7.10), while Delaware had strong revenue ($2,802) but the lowest avg. previous purchases (4.68) in the group


