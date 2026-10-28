# Statistics in Data Science

Welcome to the **Statistics** repository. This repository contains complete solutions, analytical writeups, code scripts, datasets, and interactive Jupyter Notebooks for all Statistics sessions in Data Science.

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
└── Session 3/
    ├── README.md            # Variance & Standard Deviation Hand Calculations
    ├── session_3.py         # Complete Python execution script (Tasks 1-4)
    └── session_3.ipynb      # Interactive Jupyter Notebook
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

---

## Quick Start

### Run All Session Scripts
```bash
# Session 1
python "Session 1/session_1.py"

# Session 2
python "Session 2/playlist_stats.py"
python "Session 2/session_2.py"

# Session 3
python "Session 3/session_3.py"
```

### Launch Interactive Notebooks
```bash
jupyter notebook "Session 1/session_1.ipynb"
jupyter notebook "Session 2/session_2.ipynb"
jupyter notebook "Session 3/session_3.ipynb"
```
