# Session 2 - Mean, Median & Mode

This directory contains the solutions, explanations, Python scripts, and Jupyter Notebook for **Session 2: Mean, Median & Mode**.

---

## Overview of Tasks

| Task | Topic | Deliverables |
|---|---|---|
| **Task 1** | Spotify Playlist Play Counts | `playlist_stats.py` calculating mean daily plays ($145.00$ plays/day). |
| **Task 2** | Zomato Delivery Times | Array sorting and middle element extraction for median ($30$ minutes). |
| **Task 3** | Flipkart Product Ratings | Function `most_common_rating(ratings)` computing mode ($4$ stars). |
| **Task 4** | YouTube Video Views & Outliers | Comparing 3 channels, demonstrating that viral video outliers skew Mean while Median remains robust. |
| **Task 5** | Real Kaggle Dataset (IPL Runs) | Loading `ipl_player_runs.csv` using pandas and computing Mean, Median, and Mode. |

---

## Task Details & Solutions

### Task 1: Mean Daily Spotify Plays (`playlist_stats.py`)
> **Prompt:** Create a Python script called `playlist_stats.py` that takes a list of daily Spotify song play counts (e.g., `[120, 135, 150, 200, 120, 90, 200]`) and calculates the mean (average) number of plays.

- **Data:** `[120, 135, 150, 200, 120, 90, 200]`
- **Calculation:**
  $$\text{Mean } (\bar{x}) = \frac{\sum x_i}{n} = \frac{120 + 135 + 150 + 200 + 120 + 90 + 200}{7} = \frac{1015}{7} = 145.00\text{ plays/day}$$
- **Script Location:** [`playlist_stats.py`](playlist_stats.py)

---

### Task 2: Median Delivery Time for Zomato Orders
> **Prompt:** Given the following array of delivery times (in minutes) for Zomato orders: `[30, 25, 40, 35, 30, 45, 30]`, write code to find the median delivery time and print it.

- **Original Array:** `[30, 25, 40, 35, 30, 45, 30]`
- **Step 1: Sort in ascending order:**
  $$\text{Sorted} = [25, 30, 30, \mathbf{30}, 35, 40, 45]$$
- **Step 2: Sample size:** $n = 7$ (odd).
- **Step 3: Position of median:**
  $$\text{Median Position} = \frac{n + 1}{2} = \frac{7 + 1}{2} = 4^{\text{th}}\text{ element}$$
- **Result:** **$30\text{ minutes}$**

---

### Task 3: Most Common Flipkart Rating (Mode Function)
> **Prompt:** Write a function `most_common_rating(ratings)` that takes a list of Flipkart product ratings (e.g., `[5, 4, 4, 3, 5, 4, 2, 4]`) and returns the mode (most frequent rating).

```python
from collections import Counter
import statistics

def most_common_rating(ratings):
    """Takes a list of Flipkart ratings and returns the mode."""
    if not ratings:
        return None
    return statistics.mode(ratings)
```
- **Given Ratings:** `[5, 4, 4, 3, 5, 4, 2, 4]`
- **Frequency Distribution:**
  - $4$ Stars: $4$ times (Highest frequency)
  - $5$ Stars: $2$ times
  - $3$ Stars: $1$ time
  - $2$ Stars: $1$ time
- **Output:** **$4$ stars**

---

### Task 4: YouTube Views Comparison & Outlier Sensitivity
> **Prompt:** Given three lists representing YouTube video views for three different channels, compare the mean, median, and mode for each channel, and decide which channel's data is most affected by outliers.
>
> *Hint: Try using one list with a very high value (e.g., [100, 120, 110, 105, 5000]) to see the effect on mean vs median.*

#### Comparison Table:
| Channel | Views Data | Mean Views | Median Views | Mode Views | $\lvert\text{Mean} - \text{Median}\rvert$ |
|---|---|---|---|---|---|
| **Channel A** *(Consistent)* | `[1500, 1600, 1550, 1500, 1650, 1500, 1700]` | $1571.43$ | $1550.00$ | $1500$ | $21.43$ |
| **Channel B** *(Moderate)* | `[800, 950, 1200, 850, 1100, 800, 900]` | $942.86$ | $900.00$ | $800$ | $42.86$ |
| **Channel C** *(Viral Outlier)* | `[100, 120, 110, 105, 110, 5000]` | $\mathbf{924.17}$ | $\mathbf{110.00}$ | $110$ | $\mathbf{814.17}$ |

#### Conclusion & Reasoning:
- **Channel C is most affected by outliers.**
- In Channel C, ordinary uploads receive around $100$–$120$ views, reflected accurately by the **Median ($110.00$)**.
- The single viral video ($5,000$ views) heavily inflates the **Mean to $924.17$**.
- This demonstrates that **Mean is sensitive to outliers**, whereas **Median and Mode are robust resistant estimators** of central tendency.

---

### Task 5: Real Dataset from Kaggle (IPL Player Runs) using Pandas
> **Prompt:** Pick any real dataset from Kaggle or UCI (e.g., IPL player runs, Swiggy restaurant ratings, or movie box office collections), load it using pandas, and display the mean, median, and mode for one numeric column of your choice.

- **Dataset:** IPL Top Batsmen Season Performance (`data/ipl_player_runs.csv`)
- **Selected Numeric Column:** `runs`

```python
import pandas as pd

df = pd.read_csv('data/ipl_player_runs.csv')
runs_col = df['runs']

print(f"Mean:   {runs_col.mean():.2f}")
print(f"Median: {runs_col.median():.2f}")
print(f"Mode:   {runs_col.mode().tolist()}")
```

#### Results:
- **Mean (Average Runs):** **$449.44$ runs**
- **Median (Middle Value):** **$413.00$ runs**
- **Mode:** Unique values across the top 25 batsmen.
- **Statistical Interpretation:** The Mean ($449.44$) exceeds the Median ($413.00$) due to high-scoring outlier seasons (e.g., Shubman Gill's $890$ runs and Faf du Plessis's $730$ runs), causing positive (right) skewness in the distribution.

---

## How to Run

1. Run Task 1 Spotify script:
   ```bash
   python playlist_stats.py
   ```
2. Run all Session 2 tasks:
   ```bash
   python session_2.py
   ```
3. Interactive Jupyter Notebook:
   ```bash
   jupyter notebook session_2.ipynb
   ```
