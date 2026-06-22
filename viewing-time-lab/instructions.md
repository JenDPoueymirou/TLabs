# Instructions

You are a data analyst at **NotGPT**, an educational company that creates workshops for professionals to learn data-focused skills.

Your team recently ran a training workshop and applied a treatment to one group of employees while leaving a second group unchanged. The treatment in this A/B test entails a redesign in slide format (the average word count per slide in the original presentation was 50 words, while the average word count per slide in the new presentations is 15 words).

Both groups' viewing times (in minutes) were recorded. Your job is to write a Python pipeline in explore.ipynb that cleans, explores, and reports on this data to determine whether the treatment had a meaningful effect on how long employees engaged with the workshop.

This project is organized into three parts, `cleaner.py` and `explore.ipynb`. For each step, You will write a reusable cleaning function, explore the data programmatically, and report your findings in plain language backed by one effective data visualization.

The skills that you will practice in this project include the following:
* file I/O  
* data cleaning  
* descriptive statistics  
* data visualizations  
* creating data reports  

## Background

### The Data

You've been given two plain text files for this project:
* `data/control.txt`: 500 viewing time recordings in minutes to employees who viewed the original slides
* `data/treatment.txt`: 500 viewing time recordings in minutes to employees who viewed the updated slides 

Each file has a single column with a header "minutes" followed by one numeric value per line. You will use the `cleaner.py` module to read these files into your notebook.

**Note** Remember, when you use the `readlines()` method, Python returns a list of strings! 

### Part 1: cleaner.py

Your first task is to implement the `clean_data()` function in `cleaner.py`. This function will be imported and used in your `explore.ipynb` notebook to clean your data before you begin calculating descriptive statistics.

This is a reimplementation of the data-cleaning logic you write in TLAB #1. You will apply the same idea: loop through each string value and typecast before appending to a new list. This logic is as follows:

1. Take in a list of strings in the parameter.
2. Skip the first element of the list. This is the header value and should not be included in your output.
3. For each string in this list, typecast your values and append to a new list that will contain "clean" values.
4. Return this cleaned list of floats

**Note**: Remember: You can test this function as you develop it using your jupyter notebook (just make sure to import the module before attempting to run the function).

### Part 2: explore.ipynb

In this notebook you will load both data files, apply your `clean_data()` function, compute descriptive statistics, and display a histplot on both datasets. 

You will compute descriptive statistics using the `statistics` module. Afterwards you will use the `matplotlib.pyplot` package to create a histogram on both datasets. Be sure to use the notes from class to find out more on how to create this histogram and add additional customizations (such as title or x-axis).

Be sure to import both packages at the top of your notebook! 

Afterwards, you will write up a brief observation on your findings: did the averages differ from one dataset to another? Which dataset had the highest viewing time? What about the dispersion? What this tell you about viewing behaviors of both datasets.

**Note**: Be sure to back up your findings with discrete numbers.

### Part 3 (Optional): challenge.ipynb

If you've completed this project and you're looking for a challenge, check out this notebook. We will challenge you to look ahead and use the `pandas` package to perform data analysis with minimal guidance in this notebook.

## Submission

The due date for this project is `4/12`.

To submit this project, you will push a completed version of this repository to your GitHub and post a link to your repo in Canvas.

**Note**: You must upload this to GitHub and submit a GitHub link to receive a grade for this project.
