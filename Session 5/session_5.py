"""
SESSION 5 - Sampling
--------------------
This script contains complete solutions, code simulations,
and theoretical analysis for all 5 tasks in Session 5.
"""

import random


# -------------------------------------------------------------------------
# TASK 1: Population vs. Sample in Daily Apps (3 Examples)
# -------------------------------------------------------------------------
def task_1():
    print("=" * 70)
    print("TASK 1: Population vs. Sample in Daily Apps (3 Real-World Examples)")
    print("=" * 70)

    examples = [
        {
            "app": "Instagram",
            "context": "Influencer Audience Demographics & Engagement Study",
            "population": "All 500,000 registered accounts currently following the creator.",
            "sample": "A randomly selected group of 1,000 followers surveyed for story engagement and feedback."
        },
        {
            "app": "Zomato",
            "context": "Food Packaging Quality & Hygiene Standards Audit in Mumbai",
            "population": "Every single restaurant listed on Zomato in Mumbai (e.g., all 25,000 registered eateries).",
            "sample": "250 restaurants selected randomly across different cuisines and neighborhoods for physical packaging audit."
        },
        {
            "app": "Flipkart",
            "context": "Sentiment Analysis of Customer Reviews for Electronics",
            "population": "All 2,500,000 verified product reviews submitted for electronics in 2026.",
            "sample": "5,000 randomly extracted reviews parsed by an NLP model to detect fake reviews."
        }
    ]

    for idx, ex in enumerate(examples, 1):
        print(f"\n[Example {idx}] Application: {ex['app']}")
        print(f"  Context:    {ex['context']}")
        print(f"  POPULATION: {ex['population']}")
        print(f"  SAMPLE:     {ex['sample']}")


# -------------------------------------------------------------------------
# TASK 2: Random Sampling Simulation in Python
# -------------------------------------------------------------------------
def task_2():
    print("\n" + "=" * 70)
    print("TASK 2: Random Sampling Simulation (random.sample)")
    print("=" * 70)

    # Generate population of 1000 fake user IDs
    population = [f"user{i}" for i in range(1, 1001)]
    random.seed(42)  # For reproducible results
    sample_users = random.sample(population, 50)

    print(f"Total Population Size:  {len(population)} (user1 to user1000)")
    print(f"Survey Sample Size:     {len(sample_users)} users")
    print("\nSelected 50 User IDs:")

    for i in range(0, len(sample_users), 5):
        chunk = sample_users[i:i + 5]
        print("  " + "  ".join(f"{uid:<10}" for uid in chunk))


# -------------------------------------------------------------------------
# TASK 3: Swiggy Food Delivery Times - Why Use Sampling?
# -------------------------------------------------------------------------
def task_3():
    print("\n" + "=" * 70)
    print("TASK 3: Analyzing Swiggy Delivery Times - Why Use Sampling?")
    print("=" * 70)

    print("Explanation (2-3 sentences):")
    print("  1. Computational & Financial Efficiency: Swiggy processes hundreds of millions of")
    print("     historical orders; querying the entire database for every metric would consume massive")
    print("     compute power, incur high cloud costs, and create excessive processing delays.")
    print("  2. Relevance of Current Conditions: Historical delivery times from years ago under outdated")
    print("     traffic patterns or discontinued delivery routes no longer reflect current logistics.")
    print("  3. Statistical Sufficiency: By the Central Limit Theorem, a representative sample of a few")
    print("     thousand recent orders provides statistically indistinguishable accuracy for calculating")
    print("     mean delivery times and confidence intervals in near real-time.")


# -------------------------------------------------------------------------
# TASK 4: Spotify Bollywood Survey Bias Identification
# -------------------------------------------------------------------------
def task_4():
    print("\n" + "=" * 70)
    print("TASK 4: Spotify Bollywood Survey - Bias Identification & Explanation")
    print("=" * 70)

    print("Scenario: A survey about music preferences is sent ONLY to users who recently streamed Bollywood songs.\n")
    print("Identified Bias:")
    print("  -> SELECTION BIAS (specifically Sampling Bias / Undercoverage Bias)\n")

    print("Explanation:")
    print("  1. The target population is all Spotify users, but the sampling frame is artificially restricted")
    print("     only to individuals who already listen to Bollywood tracks.")
    print("  2. This systematically excludes millions of users who exclusively listen to International Pop,")
    print("     Hip-Hop, Punjabi, Classical, EDM, K-Pop, or Indie genres.")
    print("  3. As a consequence, the survey results will heavily overestimate the general popularity and")
    print("     affinity for Bollywood music, yielding invalid, skewed conclusions about platform-wide preferences.")


# -------------------------------------------------------------------------
# TASK 5: BookMyShow Movie Booking Habits (Two Sampling Types)
# -------------------------------------------------------------------------
def task_5():
    print("\n" + "=" * 70)
    print("TASK 5: BookMyShow Movie Booking Habits - Two Types of Sampling")
    print("=" * 70)

    print("Method 1: STRATIFIED SAMPLING")
    print("  - How to apply:")
    print("    Divide all registered BookMyShow users into distinct, non-overlapping strata based on their")
    print("    city tier (Tier 1 metros like Mumbai/Bengaluru, Tier 2 cities like Jaipur/Pune, and Tier 3 towns).")
    print("  - Sampling process:")
    print("    Randomly sample a proportionate number of users from each stratum (e.g., 500 from Tier 1,")
    print("    300 from Tier 2, and 200 from Tier 3).")
    print("  - Why it is suitable:")
    print("    Guarantees that ticket purchasing habits, advance booking windows, and price sensitivities across")
    print("    different economic demographics are fairly represented without metro cities dominating the data.\n")

    print("Method 2: SYSTEMATIC SAMPLING")
    print("  - How to apply:")
    print("    Order all movie ticket transactions chronologically throughout a weekend based on booking timestamp.")
    print("  - Sampling process:")
    print("    Select every k-th transaction (e.g., every 100th booking: 37th, 137th, 237th, 337th...) after")
    print("    picking a random starting integer between 1 and 100.")
    print("  - Why it is suitable:")
    print("    Extremely simple to automate in a production data stream, ensuring even sampling across all time")
    print("    slots (morning matinees, evening peak shows, and late-night screenings) without time-clustering bias.")

    # Python demonstration of Systematic and Stratified Sampling
    print("\n--- Python Demonstration of the Two Sampling Methods on BookMyShow Data ---")
    
    # 1. Stratified Demo
    users_by_city = {
        "Tier_1_Metros": [f"user_T1_{i}" for i in range(1, 101)],
        "Tier_2_Cities": [f"user_T2_{i}" for i in range(1, 101)],
        "Tier_3_Towns":  [f"user_T3_{i}" for i in range(1, 101)]
    }
    stratified_sample = []
    for tier, users in users_by_city.items():
        sampled = random.sample(users, 3)
        stratified_sample.extend(sampled)
        print(f"  Stratified from {tier:<15}: {sampled}")

    # 2. Systematic Demo
    bookings = [f"booking_{i:04d}" for i in range(1, 51)]
    k_step = 10
    start = 4
    systematic_sample = bookings[start::k_step]
    print(f"\n  Systematic Bookings (every 10th starting at index {start}): {systematic_sample}")


# -------------------------------------------------------------------------
# MAIN RUNNER
# -------------------------------------------------------------------------
if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    print("\n" + "=" * 70)
    print("All Session 5 tasks executed successfully!")
    print("=" * 70)
