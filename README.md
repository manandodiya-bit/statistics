# Statistics in Data Science

Welcome to the **Statistics** repository. This repository contains complete solutions, analytical writeups, code scripts, datasets, high-resolution plots, and interactive Jupyter Notebooks for all Statistics sessions in Data Science.

---

## Repository Structure

```
statistics/
├── .gitignore
├── README.md
├── Session 1/
│   ├── README.md            # App Data Classification & Feature Improvement
│   ├── session_1.py         # Complete Python execution script
│   └── session_1.ipynb      # Interactive Jupyter Notebook
├── Session 2/
│   ├── README.md            # Mean, Median, Mode & Outlier Analysis
│   ├── playlist_stats.py    # Dedicated Task 1 script (Spotify play counts)
│   ├── session_2.py         # Complete Python execution script (Tasks 1-5)
│   ├── session_2.ipynb      # Interactive Jupyter Notebook
│   └── data/
│       └── ipl_player_runs.csv # Real Kaggle dataset for Task 5
├── Session 3/
│   ├── README.md            # Variance & Standard Deviation Hand Calculations
│   ├── session_3.py         # Complete Python execution script (Tasks 1-4)
│   └── session_3.ipynb      # Interactive Jupyter Notebook
├── Session 4/
│   ├── README.md            # Skewness (Basic), Distributions & Real-World Apps
│   ├── session_4.py         # Python script & plot generator (Tasks 1-4)
│   ├── session_4.ipynb      # Interactive Jupyter Notebook
│   └── plots/
│       ├── swiggy_orders_distribution.png     # Right-skewed distribution
│       └── flipkart_ratings_distribution.png  # Left-skewed distribution
├── Session 5/
│   ├── README.md            # Sampling Theory, Bias Analysis & Methodologies
│   ├── random_sampling.py   # Dedicated Task 2 script (random.sample)
│   ├── session_5.py         # Complete Python execution script (Tasks 1-5)
│   └── session_5.ipynb      # Interactive Jupyter Notebook
└── Session 6/
    ├── README.md            # Hypothesis Testing, t-Tests, p-Values & A/B Testing
    ├── session_6.py         # Complete Python execution script (Tasks 1-4)
    └── session_6.ipynb      # Interactive Jupyter Notebook
```

---

## Session Summaries

### [Session 1: Introduction to Statistics in Data Science](Session%201/README.md)
- **Task 1:** 5 daily actions on Instagram, Zomato, and Flipkart classified into Categorical vs. Numerical data.
- **Task 2:** Music genre sample data `['Pop', 'Rock', 'Jazz', ...]` classified as Nominal Categorical data with reasoning.
- **Task 3:** Improving Zomato's restaurant rating system using Bayesian Weighted Averages, Outlier Detection, and Time-Decay Weighting.
- **Task 4:** Utilizing **Mode**, **Mean**, and **Variance** in Spotify-like playlist recommendations with one-line examples.

### [Session 2: Mean, Median & Mode](Session%202/README.md)
- **Task 1:** Created `playlist_stats.py` calculating mean daily Spotify song plays ($145.00$ plays/day).
- **Task 2:** Computed median delivery time for Zomato orders ($30$ minutes).
- **Task 3:** Implemented `most_common_rating(ratings)` returning the mode for Flipkart product ratings ($4$ stars).
- **Task 4:** Compared YouTube video views across 3 channels to prove Channel C is most affected by viral outliers (Mean inflated to $924.17$ while Median remains $110.00$).
- **Task 5:** Loaded real Kaggle IPL Player Runs dataset using `pandas`, computing Mean ($449.44$), Median ($413.00$), and Mode.

### [Session 3: Variance & Standard Deviation](Session%203/README.md)
- **Task 1:** Step-by-step hand calculation of weekly step counts variance ($s^2 \approx 3,488,095.24$, $s \approx 1,867.64$).
- **Task 2:** Implemented `calculate_standard_deviation(scores)` returning sample standard deviation rounded to 2 decimal places.
- **Task 3:** Compared Zomato daily spending of Friend A ($\sigma = 0.00$) vs Friend B ($s = 145.77$), proving Friend A is significantly more consistent.
- **Task 4:** Analyzed startup monthly salaries, calculating high spread ($s = 13,255.19$) driven by a ₹60,000 outlier and showing that median better represents typical pay.

### [Session 4: Skewness (Basic)](Session%204/README.md)
- **Task 1:** Swiggy delivery partner orders plotted and classified as **Right-Skewed** due to a 200-order outlier ($\text{Mean } 33.40 > \text{Median } 15.00$).
- **Task 2:** Instagram influencer followers analyzed ($\text{Mean } 18.78\text{k} > \text{Median } 9.00\text{k}$), demonstrating positive (right) skewness.
- **Task 3:** Real-world right-skewed app analysis of Zomato order basket amounts (bounded lower end vs. unbounded upper catering orders).
- **Task 4:** Flipkart product ratings graphed and classified as **Left-Skewed** ($\text{Mean } 4.30 < \text{Median } 4.50 < \text{Mode } 5.00$) with one-line justification.

### [Session 5: Sampling](Session%205/README.md)
- **Task 1:** Defined population and sample with 3 app examples (Instagram followers, Zomato restaurants, Flipkart reviews).
- **Task 2:** Created `random_sampling.py` simulating selection of 50 random users from 1,000 user IDs via `random.sample()`.
- **Task 3:** Explained why Swiggy analyzes delivery times via sampling rather than querying all historical orders.
- **Task 4:** Identified and analyzed Selection Bias / Undercoverage Bias in Spotify's Bollywood-only music survey.
- **Task 5:** Designed Stratified Sampling and Systematic Sampling frameworks for studying BookMyShow movie booking habits.

### [Session 6: Hypothesis Testing (Basic)](Session%206/README.md)
- **Task 1:** Formulated $H_0$ and $H_1$ for daily time spent on Instagram vs. YouTube.
- **Task 2:** Executed two-sample t-test for Zomato home page redesign ($t = 2.3238$, $p = 0.0237 < 0.05 \implies \text{Reject } H_0$).
- **Task 3:** Designed complete A/B test for Paytm's redesigned sticky "Pay Now" payment button.
- **Task 4:** Evaluated Flipkart's wishlist button A/B test (520 vs 480 clicks), explaining why the result ($p = 0.0736$) is due to chance.

---

## Quick Start

### Run All Session Scripts
```bash
python "Session 1/session_1.py"
python "Session 2/playlist_stats.py"
python "Session 2/session_2.py"
python "Session 3/session_3.py"
python "Session 4/session_4.py"
python "Session 5/random_sampling.py"
python "Session 5/session_5.py"
python "Session 6/session_6.py"
```

### Launch Interactive Notebooks
```bash
jupyter notebook "Session 1/session_1.ipynb"
jupyter notebook "Session 2/session_2.ipynb"
jupyter notebook "Session 3/session_3.ipynb"
jupyter notebook "Session 4/session_4.ipynb"
jupyter notebook "Session 5/session_5.ipynb"
jupyter notebook "Session 6/session_6.ipynb"
```
