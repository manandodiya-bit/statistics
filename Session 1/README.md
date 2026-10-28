# Session 1 - Introduction to Statistics in Data Science

This directory contains the solutions, explanations, and Python implementations for **Session 1 Tasks**.

---

## Task 1: Daily App Actions & Data Type Classification

> **Prompt:** List 5 daily actions you perform on apps like Instagram, Zomato, or Flipkart, and for each, identify whether the data generated is numerical or categorical.

| S.No | Application | User Action Performed | Data Generated | High-Level Classification | Sub-Type & Scale | Explanation |
|---|---|---|---|---|---|---|
| **1** | **Instagram** | Liking a post or reel | Like Status (Liked: `True` / `False`) | **Categorical** | Nominal (Binary) | Represents a qualitative two-state binary event. *(Note: The platform's aggregated like count is Discrete Numerical).* |
| **2** | **Zomato** | Submitting a restaurant star review | Rating score ($1, 2, 3, 4, 5$ stars) | **Categorical / Numerical** | Ordinal / Discrete Numerical | Values possess a natural ordering ($5 > 4 > 3 > 2 > 1$) and can be aggregated to calculate continuous average ratings. |
| **3** | **Flipkart** | Filtering products by department/category | Category label (e.g., `"Electronics"`, `"Footwear"`) | **Categorical** | Nominal | Distinct qualitative labels without any inherent mathematical order or ranking. |
| **4** | **Zomato** | Paying the final bill amount | Total order amount in INR (e.g., `INR 458.75`) | **Numerical** | Continuous (Ratio Scale) | Measurable monetary amount on a continuous ratio scale with a true zero point. |
| **5** | **Instagram** | Watching a video / Reel | Watch duration (e.g., `18.4 seconds`) | **Numerical** | Continuous (Ratio Scale) | Continuous measurement of elapsed time with an absolute zero origin. |

---

## Task 2: Music App Sample Data Classification

> **Prompt:** Given this sample data from a music app: `['Pop', 'Rock', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Jazz', 'Pop']`, classify the type of data and explain your reasoning in 2-3 lines.

### Classification:
**Categorical Data (Qualitative — Nominal)**

### Reasoning:
1. **Qualitative Labels:** The elements represent names/labels of musical genres describing characteristics rather than numerical measurements or quantities.
2. **No Mathematical Ordering:** There is no intrinsic ranking, hierarchy, or mathematical distance between genres (e.g., `'Pop'` is not numerically greater or smaller than `'Rock'`).
3. **Non-Arithmetic:** Arithmetic operations (such as addition, subtraction, or calculating a mean) are meaningless on this data, though descriptive frequency counts and the **Mode** (`'Pop'`) can be computed.

---

## Task 3: Improving an App Feature with Statistics

> **Prompt:** Pick any one feature from an app you use (such as the number of likes on an Instagram post, or the rating of a restaurant on Zomato) and describe how statistics could help improve that feature for users.

### Selected Feature: **Restaurant Rating & Recommendation Ranking on Zomato**

#### The Problem with Simple Averages:
In naive implementations, restaurant rankings rely on a basic arithmetic mean of user star ratings. This creates significant issues:
- **Small Sample Bias:** A brand-new restaurant with only **$1$ review of $5.0$ stars** ranks higher than a legendary local restaurant with **$3,000$ reviews averaging $4.8$ stars**.
- **Vulnerability to Outliers / Review-Bombing:** A sudden coordinated wave of malicious $1$-star reviews or paid $5$-star bot reviews distorts the true diner experience.

#### Statistical Solutions to Improve the Feature:
1. **Bayesian Weighted Average (Empirical Bayes / IMDB Weighted Rating):**
   $$\text{Weighted Rating} = \frac{v \cdot R + m \cdot C}{v + m}$$
   - $v$: Number of reviews for the specific restaurant.
   - $R$: Average rating of the restaurant.
   - $m$: Minimum reviews threshold needed for ranking credibility.
   - $C$: Platform-wide global mean rating across all restaurants.
   *Impact:* New listings with few reviews are shrunk towards the platform mean, requiring substantial positive evidence before outranking established top performers.

2. **Outlier Filtering & Robust Estimators (Trimmed Mean / IQR):**
   - Applies Interquartile Range (IQR) and $z$-score thresholds to detect anomalous spikes in rating distributions.
   - Trims the top and bottom $5\%$ of extreme ratings or computes a trimmed mean / median to mitigate the effect of malicious review bombing.

3. **Time-Decayed Exponential Weighting:**
   - Incorporates half-life statistical decay weights $\lambda$ so that reviews submitted within the last $30$–$60$ days contribute more heavily than reviews submitted $3$ years ago, accurately capturing recent changes in chef, menu, or hygiene.

---

## Task 4: Spotify Playlist Recommendation — 3 Statistical Terms

> **Prompt:** Suppose you are building a new playlist recommendation feature for a Spotify-like app. List 3 basic statistical terms (such as mean, median, mode, variance, etc.) that would be useful in analyzing user listening data, and explain each with a one-line example.

### 1. Mode
- **Definition:** The value that occurs with the highest frequency in a dataset.
- **One-Line Example:** *Identifying a user's most frequently streamed artist in the past 7 days (e.g., Mode = "Arijit Singh") to anchor the primary recommendation in their daily personalized mix.*

### 2. Mean (Average)
- **Definition:** The arithmetic average calculated by summing all values and dividing by the total count.
- **One-Line Example:** *Calculating the user's average track tempo (e.g., Mean = 126 BPM) during morning workout hours to automatically curate playlists with matching cadence and energy.*

### 3. Variance (or Standard Deviation)
- **Definition:** A measure of statistical dispersion representing how widely data values deviate from the mean.
- **One-Line Example:** *Measuring the variance of acoustic features or genres in a user's listening history to decide whether to suggest a specialized single-genre playlist (low variance) or an eclectic Discover Weekly playlist (high variance).*

---

## How to Run the Code

Execute the standalone Python script:
```bash
python session_1.py
```

Or open the interactive Jupyter Notebook in VS Code or JupyterLab:
```bash
jupyter notebook session_1.ipynb
```
