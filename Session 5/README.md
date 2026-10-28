# Session 5 - Sampling

This directory contains the solutions, theoretical analyses, Python code simulations, and an interactive Jupyter Notebook for **Session 5: Sampling**.

---

## Overview of Tasks

| Task | Topic | Core Focus | Key Deliverables |
|---|---|---|---|
| **Task 1** | Population vs. Sample | App Context Definitions | 3 comprehensive real-world app examples (Instagram, Zomato, Flipkart). |
| **Task 2** | Random Sampling Simulation | Python `random.sample()` | `random_sampling.py` extracting 50 random users from 1,000 user IDs. |
| **Task 3** | Swiggy Delivery Time Analysis | Why Use Sampling? | 3 concise sentences on computational cost, timeliness, and CLT sufficiency. |
| **Task 4** | Spotify Music Survey Bias | Bias Identification | In-depth explanation of Selection Bias / Undercoverage Bias. |
| **Task 5** | BookMyShow Booking Habits | Sampling Methodologies | Stratified Sampling & Systematic Sampling design and code simulations. |

---

## Task Details & Solutions

### Task 1: 3 Examples of Population and Sample in Daily Apps

> **Prompt:** List 3 examples of 'population' and 'sample' in the context of apps you use daily (like Instagram followers, Zomato restaurants, or Flipkart products). For each, clearly define what would be considered the population and what would be a sample.

| # | Application | Practical Business Context | Population ($N$) | Sample ($n$) |
|:---:|:---:|:---:|---|---|
| **1** | **Instagram** | Influencer Follower Demographics & Feedback | **All 500,000 registered accounts** currently following an influencer. | **1,000 randomly selected followers** chosen to complete an engagement story poll. |
| **2** | **Zomato** | Restaurant Packaging Quality Audit | **All 25,000 restaurants** actively listed on Zomato in Mumbai. | **250 restaurants** selected randomly across zones and cuisines for surprise packaging checks. |
| **3** | **Flipkart** | Fake Review Detection on Electronics | **All 2,500,000 customer reviews** posted for electronics in 2026. | **5,000 randomly extracted reviews** processed by NLP models for anomaly detection. |

---

### Task 2: Random Sampling Simulation in Python

> **Prompt:** Write a Python script that simulates random sampling: given a list of 1000 fake user IDs (e.g., user1 to user1000), select 50 random users to simulate a survey sample. Print the selected user IDs.
>
> *Hint: Use the random.sample() function from Python's random module.*

- **Script Location:** [`random_sampling.py`](random_sampling.py)
- **Code:**
  ```python
  import random

  # Step 1: Generate population of 1,000 user IDs
  population = [f"user{i}" for i in range(1, 1001)]

  # Step 2: Draw random sample of 50 users
  random.seed(42)  # For reproducible output
  selected_users = random.sample(population, 50)

  print(f"Sampled {len(selected_users)} Users:")
  print(selected_users)
  ```

---

### Task 3: Swiggy Food Delivery Times — Why Use Sampling?

> **Prompt:** Imagine you are analyzing food delivery times on Swiggy. Explain in 2-3 sentences why you would use sampling instead of collecting data from every single order ever made.

#### Explanation (2-3 sentences):
1. **Computational & Cost Efficiency:** Swiggy processes hundreds of millions of historical orders; querying the entire database for operational metrics would consume immense computing power, incur high cloud data-transfer costs, and cause significant analysis latency.
2. **Current Relevance:** Historical orders from 3 years ago reflect obsolete road traffic patterns, older navigation algorithms, and discontinued restaurant partners that no longer mirror present delivery operations.
3. **Statistical Sufficiency:** Under the Central Limit Theorem, a representative sample of a few thousand recent orders provides statistically equivalent accuracy (tight confidence intervals) for estimating average delivery times in near real-time.

---

### Task 4: Spotify Bollywood Survey — Bias Identification

> **Prompt:** Given this scenario: A survey about music preferences is only sent to users who recently streamed Bollywood songs on Spotify. Identify and explain the type of bias this introduces in the sample.

#### Identified Bias:
**Selection Bias** (specifically **Sampling Bias / Undercoverage Bias**)

#### Explanation:
1. **Flawed Sampling Frame:** The target population is all general Spotify subscribers, but the sampling frame is artificially restricted to individuals who recently played Bollywood music.
2. **Systematic Exclusion:** Millions of users who exclusively listen to International Pop, Hip-Hop, Punjabi, Classical, EDM, K-Pop, or Indie genres are excluded from having any non-zero probability of being surveyed.
3. **Distorted Conclusion:** The survey results will heavily overestimate the overall platform-wide affinity and engagement with Bollywood music while severely underrepresenting other popular genres, producing flawed business decisions.

---

### Task 5: BookMyShow Movie Booking Habits — Two Sampling Types

> **Prompt:** Choose any two types of sampling (for example: random sampling, stratified sampling, systematic sampling, cluster sampling). For each, describe how you would use it to select a sample of users from BookMyShow to study movie booking habits.

#### Method 1: Stratified Sampling
- **How to apply:** Divide the BookMyShow user population into mutually exclusive subgroups (**strata**) based on **City Tier** (Tier 1 Metros: Mumbai/Delhi/Bengaluru; Tier 2 Cities: Pune/Jaipur; Tier 3 Towns) or **Booking Frequency** (Weekly, Monthly, Occasional).
- **Selection Process:** Randomly sample a proportionate number of users from each stratum (e.g., $500$ from Tier 1, $300$ from Tier 2, and $200$ from Tier 3).
- **Why it is suitable:** Guarantees that regional movie preferences, advance booking windows, and ticket price sensitivities across varying economic backgrounds are accurately represented without dominant metro hubs overshadowing smaller cities.

#### Method 2: Systematic Sampling
- **How to apply:** Arrange all movie ticket booking transactions completed over a weekend sequentially in chronological order by booking timestamp.
- **Selection Process:** Determine a fixed interval $k$ (e.g., $k = 100$). Pick a random starting index between $1$ and $100$ (e.g., transaction $37$), then select every $100^{\text{th}}$ transaction thereafter ($37^{\text{th}}, 137^{\text{th}}, 237^{\text{th}}, 337^{\text{th}}, \dots$).
- **Why it is suitable:** Extremely simple to implement in a real-time transactional stream, ensuring consistent, uniform representation across morning matinees, prime-time evening shows, and midnight screenings without time-clustering bias.

---

## How to Run

1. Run the dedicated Task 2 random sampling script:
   ```bash
   python random_sampling.py
   ```
2. Run the complete Session 5 suite:
   ```bash
   python session_5.py
   ```
3. Interactive Jupyter Notebook:
   ```bash
   jupyter notebook session_5.ipynb
   ```
