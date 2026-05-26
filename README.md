# Mobile User Behavior Analysis

---

## Project Snapshot

- Dataset Size: 700 mobile users
- Analysis Type: EDA + Statistical Inference
- Tools: Python, Pandas, Seaborn, SciPy
- Focus Areas:
  - Screen time
  - Battery drain
  - App usage
  - Data consumption
  - Operating system comparisons

---

## Key Visualizations

### User Behavior Class

![User Behavior Class](images/user_behavior_class.png)


This visualization shows that mobile user behavior classes are strongly associated with the amount of time users spend
on their mobile devices. Higher behavior classes exhibit greater overall app usage activity.

---

### Correlation Heatmap

![Correlation Heatmap](images/correlation_heatmap.png)

The heatmap highlights strong positive relationships between app usage time, screen-on time, battery drain, and data usage, suggesting that increased device activity contributes to higher resource consumption.

---

## Exploratory Data Analysis & Statistical Inference

This project analyzes behavioral data from 700 mobile users to explore relationships between app usage, screen time, battery drain, and data consumption across different device models and operating systems.

Using exploratory data analysis and hypothesis testing, the project identifies usage patterns and evaluates whether operating systems or device models significantly influence user behavior metrics.

---

## Project Objectives

This project aims to answer the following questions:
  - How do mobile phone users behave in terms of application usage, screen activity, battery consumption, and data utilization?
  - Do users behave differently across mobile device models?
  - Is there a statistically significant difference in battery drain between Android and iOS operating systems?
  - Does data usage significantly differ across mobile device models?

---

## Key Findings

- Android and iOS users showed no statistically significant difference in battery drain.
- Device model did not strongly predict data consumption behavior.
- Screen time and app usage were positively correlated.
- User behavior patterns were more influential than device type alone.

---

## Business Relevance

Insights from this analysis could help:
- mobile manufacturers optimize battery performance
- app developers understand engagement behavior
- telecom providers analyze data consumption trends
- UX teams improve mobile usage experiences

## Dataset Information

The dataset contains behavioral information from 700 mobile phone users and includes:
- Device model
- Operating system
- App usage time
- Screen-on time
- Number of installed applications
- Data usage
- Age
- Gender
- User behavior classification

---

## Analytical Workflow

1. Data Understanding
2. Data Cleaning and Preparation
3. Distribution Analysis of Individual Features
4. Descriptive Statistics
5. Correlation Analysis
6. Hypothesis Testing
7. Conclusion

---

## Technologies Used

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Jupyter Notebook
- Git & GitHub

---

## Statistical Methods

### Independent Two-Sample t-test

Used to compare average battery drain between Android and iOS operating systems.

### One-Way ANOVA

Used to evaluate differences in mean data usage across the five mobile device models.

### Assumption Checks
- Histogram inspection
- Q-Q plots
- Shapiro-Wilk normality test
- Levene's test for homogeneity of variance

---

## Visualizations

The project includes several visualizations such as:
 - Battery drain distribution histogram
 - Battery drain by device model
 - Battery drain by gender
 - Mobile device market share pie chart
 - Correlation heatmap
 - Pairplot analysis

---

## Reproducibility

To run this project locally:
```
git clone https://github.com/TontonGit/mobile-user-behavior-analysis.git
```

Install required libraries:
```
pip install pandas numpy matplotlib seaborn scipy
```

Run the notebook from the **notebooks/** directory.

---

## Project Structure

```text
mobile-user-behavior-analysis/
│
├── data/
├── images/
├── notebooks/
├── src/
└── README.md
```
---

## Author


Akowe Atty













