"""
SESSION 1 - Introduction to Statistics in Data Science
------------------------------------------------------
This script contains solutions, explanations, and Python demonstrations
for all tasks in Session 1.
"""

from collections import Counter
import statistics


def task_1():
    print("=" * 70)
    print("TASK 1: 5 Daily Actions on Apps & Data Classification")
    print("=" * 70)

    actions = [
        {
            "no": 1,
            "app": "Instagram",
            "action": "Double-tapping a post/reel to like it",
            "data_generated": "Like status (Liked: True / False)",
            "classification": "Categorical",
            "sub_type": "Nominal (Binary)",
            "explanation": "Generates a two-state label (Liked vs. Not Liked). Aggregated total likes is Discrete Numerical."
        },
        {
            "no": 2,
            "app": "Zomato",
            "action": "Submitting a star rating after an order",
            "data_generated": "Rating score (1 to 5 stars)",
            "classification": "Categorical / Numerical",
            "sub_type": "Ordinal / Discrete Numerical",
            "explanation": "Ratings possess a natural rank/order (5 > 4 > 3 > 2 > 1) and can be treated numerically for computing averages."
        },
        {
            "no": 3,
            "app": "Flipkart",
            "action": "Selecting a product category or brand filter",
            "data_generated": "Category Name (e.g., 'Electronics', 'Footwear')",
            "classification": "Categorical",
            "sub_type": "Nominal",
            "explanation": "Distinct qualitative categories with no inherent mathematical order or hierarchy."
        },
        {
            "no": 4,
            "app": "Zomato",
            "action": "Paying the final bill for food delivery",
            "data_generated": "Total order amount (e.g., INR 458.75)",
            "classification": "Numerical",
            "sub_type": "Continuous (Ratio Scale)",
            "explanation": "Measurable financial quantity with meaningful zero and fine gradations (decimals allowed)."
        },
        {
            "no": 5,
            "app": "Instagram",
            "action": "Watching a Reel in the feed",
            "data_generated": "Watch time duration (e.g., 18.4 seconds)",
            "classification": "Numerical",
            "sub_type": "Continuous (Ratio Scale)",
            "explanation": "A continuous time measurement on a ratio scale with an absolute zero point."
        }
    ]

    for item in actions:
        print(f"\n[{item['no']}] App: {item['app']}")
        print(f"    Action: {item['action']}")
        print(f"    Data Generated: {item['data_generated']}")
        print(f"    Classification: {item['classification']} ({item['sub_type']})")
        print(f"    Detail: {item['explanation']}")


def task_2():
    print("\n" + "=" * 70)
    print("TASK 2: Music App Sample Data Classification & Reasoning")
    print("=" * 70)

    sample_data = ['Pop', 'Rock', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Jazz', 'Pop']
    print(f"Sample Data: {sample_data}\n")

    print("Classification:")
    print("  -> Categorical Data (Qualitative - Nominal)\n")

    print("Reasoning (2-3 lines):")
    print("  1. The elements represent qualitative genre labels describing musical style, not numerical measurements.")
    print("  2. The categories have no mathematical order, ranking, or distance (e.g., 'Pop' is not mathematically greater than 'Rock').")
    print("  3. Arithmetic operations (addition/average) are not meaningful, though frequency counts and the Mode can be calculated.\n")

    # Statistical demonstration using Python
    counts = Counter(sample_data)
    mode_genre = statistics.mode(sample_data)
    print(f"Frequency Distribution: {dict(counts)}")
    print(f"Calculated Mode (Most Frequent Genre): '{mode_genre}' (count: {counts[mode_genre]})")


def task_3():
    print("\n" + "=" * 70)
    print("TASK 3: Improving an App Feature with Statistics")
    print("=" * 70)

    print("Feature Chosen: Restaurant Rating & Recommendation System on Zomato\n")
    print("Problem with naive approach:")
    print("  A simple arithmetic mean of ratings can be misleading. A new restaurant with 1 review of")
    print("  5.0 stars will rank above an established restaurant with 2,500 reviews averaging 4.8 stars.")
    print("  Additionally, unweighted averages are vulnerable to sudden outlier attacks (1-star review-bombing).\n")

    print("How Statistics Improves This Feature:")
    print("  1. Bayesian Weighted Average (Empirical Bayes):")
    print("     Pulls restaurants with few reviews toward the platform average until a credible sample size")
    print("     is reached, preventing one-off 5-star spots from falsely topping search lists.")
    print("  2. Outlier Detection & Robust Estimators (Trimmed Mean / IQR):")
    print("     Uses statistical dispersion and z-scores to detect and filter out bot spikes or spam campaigns.")
    print("  3. Time-Decay Exponential Weighting:")
    print("     Assigns exponentially higher statistical weight to reviews from the past 30-90 days, accurately")
    print("     reflecting current food quality and service consistency.")

    # Demonstration of Simple Mean vs Bayesian Weighted Mean
    print("\n--- Numerical Demonstration ---")
    global_avg = 3.8
    m_min_reviews = 50

    restaurants = [
        {"name": "Restaurant A (Brand New)", "reviews": 1, "avg_rating": 5.0},
        {"name": "Restaurant B (Popular Classic)", "reviews": 1200, "avg_rating": 4.8},
    ]

    for r in restaurants:
        v = r["reviews"]
        R = r["avg_rating"]
        # Bayesian weighted average formula: WR = (v * R + m * C) / (v + m)
        bayesian_rating = (v * R + m_min_reviews * global_avg) / (v + m_min_reviews)
        print(f"{r['name']}:")
        print(f"   Simple Average:   {R:.2f} stars ({v} reviews)")
        print(f"   Bayesian Score:   {bayesian_rating:.2f} stars (Statistically Adjusted)")


def task_4():
    print("\n" + "=" * 70)
    print("TASK 4: Spotify-like Playlist Recommendation - 3 Statistical Terms")
    print("=" * 70)

    terms = [
        {
            "term": "Mode",
            "definition": "The most frequently occurring value in a dataset.",
            "example": "Finding the most played artist in a user's weekly listening history to anchor their 'Daily Mix' playlist (e.g., Mode = 'Arijit Singh')."
        },
        {
            "term": "Mean (Average)",
            "definition": "The sum of all values divided by the count, representing central tendency.",
            "example": "Calculating the user's average track tempo (e.g., Mean = 126 BPM) during morning hours to generate an energized workout playlist."
        },
        {
            "term": "Variance (or Standard Deviation)",
            "definition": "A measure of how spread out or diverse data points are from the mean.",
            "example": "Analyzing tempo or acoustic variance to decide whether to suggest a focused single-genre mix (low variance) or an eclectic 'Discover Weekly' playlist (high variance)."
        }
    ]

    for t in terms:
        print(f"\n* {t['term']}:")
        print(f"  - Definition: {t['definition']}")
        print(f"  - One-Line Example: {t['example']}")

    # Python simulation of Spotify user audio features
    print("\n--- Python Demonstration on Simulated User Track Tempos (BPM) ---")
    tempos_workout = [124, 128, 126, 130, 125, 128, 127]
    genres_played = ["Pop", "EDM", "Pop", "Hip-Hop", "Pop", "Rock", "Pop"]

    print(f"Track Tempos (BPM): {tempos_workout}")
    print(f"Mean BPM:     {statistics.mean(tempos_workout):.1f} BPM")
    print(f"Median BPM:   {statistics.median(tempos_workout):.1f} BPM")
    print(f"Variance:     {statistics.variance(tempos_workout):.2f}")
    print(f"Std Dev:      {statistics.stdev(tempos_workout):.2f}")
    print(f"Genres:       {genres_played}")
    print(f"Mode Genre:   '{statistics.mode(genres_played)}'")


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    print("\n" + "=" * 70)
    print("All Session 1 tasks completed successfully!")
    print("=" * 70)
