# Session 3 - Variance & Standard Deviation

This directory contains the solutions, step-by-step hand calculations, Python implementations, and an interactive Jupyter Notebook for **Session 3: Variance & Standard Deviation**.

---

## Overview of Tasks

| Task | Topic | Deliverables |
|---|---|---|
| **Task 1** | Fitness App Step Counts | Full step-by-step hand calculation of variance ($s^2 \approx 3,488,095.24$). |
| **Task 2** | Exam Scores Standard Deviation | Python function `calculate_standard_deviation(scores)` rounded to 2 decimal places. |
| **Task 3** | Zomato Daily Spending | Comparing Friend A ($\sigma = 0.00$) vs Friend B ($s = 145.77$) to determine spending consistency. |
| **Task 4** | Startup Salary Spread Analysis | Variance and Standard Deviation on 6 salaries, interpreting the high spread due to a 60k outlier. |

---

## Task Details & Solutions

### Task 1: Step Counts Variance Hand Calculation

> **Prompt:** Given an array of daily step counts from your fitness app for one week (e.g., `[4500, 7000, 5000, 8000, 4000, 9000, 6000]`), calculate the variance by hand using the variance formula and show each calculation step.

#### Step 1: Compute the Mean ($\bar{x}$)
$$\sum x_i = 4500 + 7000 + 5000 + 8000 + 4000 + 9000 + 6000 = 43,500$$
$$\bar{x} = \frac{\sum x_i}{n} = \frac{43,500}{7} \approx 6,214.2857\text{ steps}$$

#### Step 2: Tabulate Deviations and Squared Deviations

| Day | Steps ($x_i$) | Deviation $(x_i - \bar{x})$ | Squared Deviation $(x_i - \bar{x})^2$ |
|:---:|:---:|:---:|:---:|
| **1** | $4,500$ | $4500 - 6214.2857 = -1714.2857$ | $2,938,775.51$ |
| **2** | $7,000$ | $7000 - 6214.2857 = +785.7143$ | $617,346.94$ |
| **3** | $5,000$ | $5000 - 6214.2857 = -1214.2857$ | $1,474,489.80$ |
| **4** | $8,000$ | $8000 - 6214.2857 = +1785.7143$ | $3,188,775.51$ |
| **5** | $4,000$ | $4000 - 6214.2857 = -2214.2857$ | $4,903,061.22$ |
| **6** | $9,000$ | $9000 - 6214.2857 = +2785.7143$ | $7,760,204.08$ |
| **7** | $6,000$ | $6000 - 6214.2857 = -214.2857$ | $45,918.37$ |
| **Total** | **$43,500$** | **$0.00$** | **$\sum (x_i - \bar{x})^2 = 20,928,571.43$** |

#### Step 3: Compute Variance
- **Sample Variance ($s^2$):**
  $$s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1} = \frac{20,928,571.43}{6} \approx \mathbf{3,488,095.24}$$
  $$s = \sqrt{3,488,095.24} \approx \mathbf{1,867.64\text{ steps}}$$

- **Population Variance ($\sigma^2$):**
  $$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N} = \frac{20,928,571.43}{7} \approx \mathbf{2,989,795.92}$$
  $$\sigma = \sqrt{2,989,795.92} \approx \mathbf{1,729.10\text{ steps}}$$

---

### Task 2: Standard Deviation Python Function

> **Prompt:** Write a Python function called `calculate_standard_deviation(scores)` that takes a list of exam scores and returns the standard deviation rounded to two decimal places.

```python
import math

def calculate_standard_deviation(scores):
    """
    Takes a list of exam scores and returns the sample standard deviation
    rounded to two decimal places.
    """
    if len(scores) < 2:
        return 0.0
    
    mean_score = sum(scores) / len(scores)
    sum_squared_diff = sum((x - mean_score) ** 2 for x in scores)
    variance = sum_squared_diff / (len(scores) - 1)
    return round(math.sqrt(variance), 2)
```

**Test Example:**
- Input: `[78, 85, 92, 60, 88, 75, 95]`
- Output: `11.99`

---

### Task 3: Spending Consistency Comparison on Zomato

> **Prompt:** Imagine two friends track their daily spending on Zomato over 5 days. Friend A spends `[200, 200, 200, 200, 200]` and Friend B spends `[100, 300, 150, 400, 50]`. Calculate the standard deviation for both and explain in 2-3 lines who has more consistent spending and why.

#### Statistical Metrics:
- **Friend A:**
  - Mean: $\text{INR } 200.00$
  - Standard Deviation: $\mathbf{0.00}$
- **Friend B:**
  - Mean: $\text{INR } 200.00$
  - Sum of squared deviations: $(100-200)^2 + (300-200)^2 + (150-200)^2 + (400-200)^2 + (50-200)^2 = 85,000$
  - Sample Standard Deviation: $\sqrt{\frac{85,000}{4}} = \mathbf{145.77}$ *(or Population SD: $\sqrt{\frac{85,000}{5}} = 130.38$)*

#### Decision & Reasoning (2-3 lines):
1. **Friend A has significantly more consistent spending than Friend B.**
2. Friend A's standard deviation is **$0.00$**, which indicates zero dispersion or variation around the mean (spending is completely predictable at exactly ₹200 every day).
3. In contrast, Friend B's standard deviation is **$145.77$**, revealing erratic swings between ₹50 and ₹400 despite sharing the same average.

---

### Task 4: Startup Monthly Salary Spread & Interpretation

> **Prompt:** You are given the monthly salary data of 6 employees in a startup: `[28000, 29000, 27000, 60000, 26500, 27500]`. Calculate the variance and standard deviation, then interpret in 2-3 lines what the high or low spread means for this team.

#### Calculations:
- Salaries: `[28000, 29000, 27000, 60000, 26500, 27500]`
- Total Sum: $198,000$
- Mean Salary: $\frac{198000}{6} = \mathbf{33,000.00}$
- Median Salary: $\mathbf{27,750.00}$
- Sum of Squared Deviations: $878,500,000.00$
- **Sample Variance ($s^2$):** $\frac{878,500,000}{5} = \mathbf{175,700,000.00}$
- **Sample Standard Deviation ($s$):** $\sqrt{175,700,000} \approx \mathbf{13,255.19}$
- *(Population Variance $\sigma^2 = 146,416,666.67$, Population SD $\sigma = 12,100.28$)*

#### Interpretation (2-3 lines):
1. Five out of the six startup employees earn closely between ₹26,500 and ₹29,000, but the team's standard deviation is very high (exceeding ₹13,000).
2. This large spread is driven by a single high-earning outlier (₹60,000, likely a founder or tech lead), which inflates the mean (₹33,000) significantly above what 83% of the team actually earns.
3. This indicates severe internal pay disparity, showing that the median (₹27,750) provides a much more honest measure of typical employee compensation than the mean.

---

## How to Run

1. Run the Python script:
   ```bash
   python session_3.py
   ```
2. Open the Jupyter Notebook:
   ```bash
   jupyter notebook session_3.ipynb
   ```
