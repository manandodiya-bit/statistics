"""
Session 5 - Task 2: Random User Survey Sampling
------------------------------------------------
Script name: random_sampling.py

Generates 1,000 fake user IDs (user1 to user1000) and draws
a random sample of 50 users using python's random.sample().
"""

import random


def simulate_random_sampling(total_users=1000, sample_size=50, seed=42):
    """
    Generates a population of user IDs and draws a random sample of specified size.
    """
    # Step 1: Create a population of fake user IDs
    population = [f"user{i}" for i in range(1, total_users + 1)]

    # Step 2: Set optional random seed for reproducibility
    if seed is not None:
        random.seed(seed)

    # Step 3: Draw random sample without replacement
    sample = random.sample(population, sample_size)
    return population, sample


def main():
    print("=" * 70)
    print("SESSION 5 - TASK 2: RANDOM USER SURVEY SAMPLING")
    print("=" * 70)

    total_users = 1000
    sample_size = 50

    population, selected_users = simulate_random_sampling(total_users, sample_size, seed=42)

    print(f"Total Population Size:  {len(population)} users ({population[0]} to {population[-1]})")
    print(f"Sample Size Selected:   {len(selected_users)} users")
    print("-" * 70)
    print("Selected User IDs for Survey Sample (50 Random Users):")
    print("-" * 70)

    # Print 5 IDs per line for clean readability
    for i in range(0, len(selected_users), 5):
        row = selected_users[i:i + 5]
        formatted_row = "  ".join(f"{uid:<10}" for uid in row)
        print(f"  [{i + 1:02d}-{i + len(row):02d}]  {formatted_row}")

    print("-" * 70)
    print(f"[+] Successfully drew {len(selected_users)} unique users from {len(population)} users.")
    print("=" * 70)


if __name__ == "__main__":
    main()
