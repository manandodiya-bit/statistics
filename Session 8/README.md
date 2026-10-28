# Session 8 - Probability Basics

This directory contains the solutions, probability formulas, simulations, and interactive Jupyter Notebook for **Session 8: Probability Basics**.

---

## Overview of Tasks

| Task | Topic | Key Focus | Mathematical Deliverables |
|---|---|---|---|
| **Task 1** | Probability Function & Coin Toss | Classical Probability | Function `calculate_probability(1, 2)` $\rightarrow P(\text{Heads}) = 0.50$ (50%). |
| **Task 2** | Dice Rolling Simulation | Experimental vs. Theoretical | 100 random rolls, counting 6s ($P_{\text{exp}} = 0.20$ vs $P_{\text{theo}} = 0.1667$). |
| **Task 3** | Spotify Playlist Probability | Empirical Probability | Last 20 songs, probability of picking a 'pop' song ($9/20 = 0.45$). |
| **Task 4** | Zomato Set Probability | Intersection over Union | Function computing $P(\text{Food } \cap \text{ Dessert}) = 3/10 = 0.30$. |
| **Task 5** | Conditional Probability in E-Commerce | Flipkart Recommendations | $P(\text{Headphones} \mid \text{Phone}) = 210/300 = 70.0\%$ for cross-selling. |

---

## Task Details & Solutions

### Task 1: Basic Probability Function & Coin Toss

> **Prompt:** Write a Python function `calculate_probability(event_count, total_outcomes)` that returns the probability of an event, and use it to find the probability of getting 'Heads' when tossing a coin.

#### Formula:
$$P(E) = \frac{\text{Number of favorable outcomes } (n(E))}{\text{Total number of possible outcomes } (n(S))}$$

```python
def calculate_probability(event_count, total_outcomes):
    """Returns probability of an event."""
    if total_outcomes <= 0:
        raise ValueError("Total outcomes must be greater than zero.")
    return event_count / total_outcomes

# Fair coin toss: Heads = 1, Total Outcomes = 2 (Heads, Tails)
prob_heads = calculate_probability(1, 2)
print(f"P(Heads) = {prob_heads:.2f}")  # 0.50 (50%)
```

---

### Task 2: Dice Rolling Simulation (100 Rolls)

> **Prompt:** Simulate rolling a six-sided dice 100 times using Python's random module, count how many times a '6' appears, and calculate the experimental probability of getting a '6'.
>
> *Hint: Use random.randint(1,6) in a loop and keep a counter for '6'.*

```python
import random

random.seed(42)
rolls = [random.randint(1, 6) for _ in range(100)]
count_six = rolls.count(6)

experimental_prob = count_six / 100
theoretical_prob = 1 / 6

print(f"Count of 6s: {count_six}")
print(f"Experimental Probability: {experimental_prob:.4f} (20.0%)")
print(f"Theoretical Probability:  {theoretical_prob:.4f} (16.67%)")
```

---

### Task 3: Probability of 'Pop' Song in Last 20 Spotify Tracks

> **Prompt:** Given an array of genres from your last 20 Spotify songs (like `['pop', 'rock', 'pop', 'hiphop', ...]`), write code to calculate the probability of randomly picking a 'pop' song from your recent history.

```python
spotify_genres = [
    'pop', 'rock', 'pop', 'hiphop', 'pop', 'indie', 'rock', 'pop',
    'jazz', 'pop', 'edm', 'hiphop', 'pop', 'rock', 'pop', 'indie',
    'pop', 'hiphop', 'rock', 'pop'
]

pop_count = spotify_genres.count('pop')
total_songs = len(spotify_genres)
prob_pop = pop_count / total_songs

print(f"Pop Songs: {pop_count} / {total_songs}")
print(f"P(Pop) = {prob_pop:.4f} (45.0%)")
```

---

### Task 4: Zomato Food & Dessert Orders (Intersection over Union)

> **Prompt:** Write a function that, given two arrays — one for users who ordered food on Zomato and one for users who ordered dessert — calculates the probability that a randomly selected user ordered both food and dessert (i.e., intersection over total unique users).

#### Formula:
$$P(\text{Food } \cap \text{ Dessert}) = \frac{|\text{Food} \cap \text{Dessert}|}{|\text{Food} \cup \text{Dessert}|}$$

```python
def probability_both_ordered(food_users, dessert_users):
    set_food = set(food_users)
    set_dessert = set(dessert_users)
    both = set_food.intersection(set_dessert)
    all_unique = set_food.union(set_dessert)
    return len(both) / len(all_unique) if all_unique else 0.0

food = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8']
dessert = ['user3', 'user4', 'user5', 'user9', 'user10']

prob = probability_both_ordered(food, dessert)
print(f"P(Both Food & Dessert) = 3 / 10 = {prob:.2f} (30%)")
```

---

### Task 5: Conditional Probability in Flipkart Recommendations

> **Prompt:** Explain with a short Python code example how conditional probability could be used to improve recommendations in an app like Flipkart (e.g., probability of buying headphones given user bought a phone).
>
> *Hint: Use counts of users who bought both items vs total who bought a phone.*

#### Principle:
$$P(\text{Headphones} \mid \text{Phone}) = \frac{P(\text{Headphones} \cap \text{Phone})}{P(\text{Phone})} = \frac{\text{Count}(\text{Bought Both Phone and Headphones})}{\text{Count}(\text{Bought Phone})}$$

#### Practical Application:
When a customer adds a smartphone to their cart on Flipkart, the recommender evaluates the conditional probability of complementary accessories. Since $P(\text{Headphones} \mid \text{Phone})$ is exceptionally high ($70\%$), the platform renders an automated cross-sell bundle card (*"Frequently Bought Together"*), significantly increasing average order value and checkout conversion.

```python
total_customers = 1000
phone_buyers = 300
bought_both = 210

p_headphones_given_phone = bought_both / phone_buyers
print(f"P(Headphones | Phone) = {bought_both}/{phone_buyers} = {p_headphones_given_phone:.2f} (70.0%)")
```

---

## How to Run

1. Run the Python script:
   ```bash
   python session_8.py
   ```
2. Open the Jupyter Notebook:
   ```bash
   jupyter notebook session_8.ipynb
   ```
