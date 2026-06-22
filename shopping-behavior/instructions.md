# FlashFash: American Consumer Shopping Analysis

You are a junior data analyst at **FlashFash**, a fast-growing online shopping company headquartered in Bengaluru, India, that recently went public at a **$90 Billion USD IPO valuation**. To establish a foothold in the global market, your team has been tasked with analyzing the shopping behavior of American consumers.

Your job will entail analyzing a sample dataset for aggregate descriptive statistics and visualizations. We are interested in discovering the "seasonality" of shoppers, which demographics buy the most, and which market outreach strategies we can apply to maximize purchases.

Utilize documentation, your peers, readings, and classroom notes to complete this project. There is one difficulty level. The complete directions are embedded in the project itself.

**Due date: 4/30. Submit a link to your GitHub repository.**

Fun fact: fashion is not immune to the promises of data science. Check out these links to find out more:
* [data, but make it fashion](https://databutmakeitfashion.com/)
* [SHEIN data practices](https://news.sophos.com/en-us/2023/03/10/shein-shopping-app-goes-rogue-grabs-price-and-url-data-from-your-clipboard/)

---

## Background

This dataset contains **3,900 samples & 15 columns** of simulated shopping data. Before writing any code, open `data/raw/shopping.csv` in a spreadsheet tool (Excel or Google Sheets) to get a feel for its structure.

### Columns

| Column | Description |
|---|---|
| **Customer ID** | Unique identifier per customer |
| **Age** | Customer age for demographic segmentation |
| **Gender** | Gender identification of the customer |
| **Item Purchased** | The specific product selected |
| **Purchase Amount (USD)** | Transaction value in US dollars |
| **Location** | State from which the order was placed |
| **Size** | Size specification of the purchased item |
| **Color** | Color variant of the purchased item |
| **Season** | Seasonal relevance of the purchase (Spring, Summer, Fall, Winter) |
| **Review Rating** | Numerical customer satisfaction rating |
| **Shipping Type** | Delivery method (standard, express, etc.) |
| **Promo Code Used** | Whether a promotional code was applied |
| **Previous Purchases** | Number of prior purchases by the customer |
| **Payment Method** | Mode of payment (credit card, cash, etc.) |
| **Frequency of Purchases** | How often the customer makes purchases |

---

## Part 0: Initial Exploration & Question Formulation

> **Complete this part before writing any analysis code.**

Every good data analysis starts with curiosity. Before you can answer questions, you need to know which questions are worth asking.

### Step 1: Explore the Raw Data

Open `data/raw/shopping.csv` in **Google Sheets or Excel** (or load it with `pandas` and call `.head()`, `.describe()`, and `.info()`). Spend at least 10–15 minutes scrolling through the data. Ask yourself:

* What does each row represent?
* Which columns are numeric? Which are categorical?
* Are there any columns that surprise you or that you don't immediately understand?
* What would a FlashFash executive care about most: sales volume, demographics, timing, marketing ROI?

### Step 2: Write Your Questions

In `README.md`, write a section titled **"My Analytical Questions"** containing **at least 6 original questions** you want to investigate. These should be your own questions based on your initial data exploration.

A strong question is:
* **Specific**: names a column or relationship (e.g., "Does purchase amount differ by payment method?" not "What affects spending?")
* **Answerable**: can be investigated with this dataset's columns
* **Interesting**: would matter to a real business decision

**Example question to inspire you (do not use this):**
* Which shipping types are most common among high-spend customers?

## Required Analytical Questions

In addition to your own questions, your analysis **must** address these four:

1. What are the most popular colors by season?
2. What is the most popular clothing item by season?
3. What is the effect of promo codes on the dollar amount of purchases?
4. When do users leave a review?

## Submission Checklist

Before submitting, confirm:

- [ ] `README.md` includes your **My Analytical Questions** section (6+ questions, 3 starred)
- [ ] All files are pushed to GitHub

**Submit your GitHub repository link in Canvas by 4/30.**
