"""
SESSION 8 - Probability Basics
-------------------------------
This script contains complete solutions, probability functions,
simulations, and practical e-commerce recommendation examples
for all 5 tasks in Session 8.
"""

from collections import Counter
import random


# -------------------------------------------------------------------------
# TASK 1: Basic Probability Function & Coin Toss
# -------------------------------------------------------------------------
def calculate_probability(event_count, total_outcomes):
    """
    Returns the probability of an event given the favorable event count
    and the total number of possible outcomes.
    """
    if total_outcomes <= 0:
        raise ValueError("Total outcomes must be greater than zero.")
    return event_count / total_outcomes


def task_1():
    print("=" * 70)
    print("TASK 1: Function calculate_probability() & Coin Toss")
    print("=" * 70)

    # For a fair coin toss:
    # Sample Space S = {'Heads', 'Tails'}, Total Outcomes = 2
    # Event E = {'Heads'}, Event Count = 1
    event_heads = 1
    total_coin_outcomes = 2

    prob_heads = calculate_probability(event_heads, total_coin_outcomes)

    print("Sample Space S:             {'Heads', 'Tails'}")
    print(f"Favorable Event Count (E):  {event_heads} ('Heads')")
    print(f"Total Outcomes (S):         {total_coin_outcomes}")
    print(f"Probability of 'Heads':     {prob_heads:.4f} ({prob_heads * 100:.1f}%)")


# -------------------------------------------------------------------------
# TASK 2: Dice Rolling Simulation (100 Rolls) & Experimental Probability
# -------------------------------------------------------------------------
def task_2():
    print("\n" + "=" * 70)
    print("TASK 2: Dice Rolling Simulation (100 Rolls - Count of '6')")
    print("=" * 70)

    num_rolls = 100
    random.seed(42)  # For reproducible simulation

    rolls = [random.randint(1, 6) for _ in range(num_rolls)]
    count_six = rolls.count(6)
    experimental_prob = count_six / num_rolls
    theoretical_prob = 1 / 6

    counts = Counter(rolls)
    print(f"Total Rolls Simulated:       {num_rolls}")
    print(f"Frequency of Each Outcome:   {dict(sorted(counts.items()))}")
    print(f"Count of '6' Appeared:       {count_six} times")
    print(f"Experimental Probability:    {count_six}/{num_rolls} = {experimental_prob:.4f} ({experimental_prob * 100:.1f}%)")
    print(f"Theoretical Probability:     1/6 = {theoretical_prob:.4f} ({theoretical_prob * 100:.2f}%)")
    print(f"Difference (Simulation Error): {abs(experimental_prob - theoretical_prob):.4f}")


# -------------------------------------------------------------------------
# TASK 3: Probability of 'Pop' Song in Last 20 Spotify Tracks
# -------------------------------------------------------------------------
def task_3():
    print("\n" + "=" * 70)
    print("TASK 3: Probability of Picking a 'Pop' Song from Spotify History")
    print("=" * 70)

    spotify_genres = [
        'pop', 'rock', 'pop', 'hiphop', 'pop', 'indie', 'rock', 'pop',
        'jazz', 'pop', 'edm', 'hiphop', 'pop', 'rock', 'pop', 'indie',
        'pop', 'hiphop', 'rock', 'pop'
    ]

    total_songs = len(spotify_genres)
    pop_count = spotify_genres.count('pop')
    prob_pop = pop_count / total_songs

    genre_breakdown = Counter(spotify_genres)

    print(f"Total Songs in Recent History: {total_songs}")
    print(f"Genre Breakdown:               {dict(genre_breakdown)}")
    print(f"Number of 'Pop' Songs:         {pop_count}")
    print(f"Probability of Picking 'Pop':  {pop_count}/{total_songs} = {prob_pop:.4f} ({prob_pop * 100:.1f}%)")


# -------------------------------------------------------------------------
# TASK 4: Zomato Food & Dessert Orders (Intersection over Union)
# -------------------------------------------------------------------------
def probability_both_ordered(food_users, dessert_users):
    """
    Calculates the probability that a randomly selected user ordered both
    food and dessert: |Food AND Dessert| / |Total Unique Users|.
    """
    set_food = set(food_users)
    set_dessert = set(dessert_users)

    # Intersection: users who ordered both
    both = set_food.intersection(set_dessert)
    # Total unique users (Union)
    all_users = set_food.union(set_dessert)

    if not all_users:
        return 0.0

    return len(both) / len(all_users)


def task_4():
    print("\n" + "=" * 70)
    print("TASK 4: Probability of Ordering Both Food & Dessert on Zomato")
    print("=" * 70)

    food_users = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8"]
    dessert_users = ["user3", "user4", "user5", "user9", "user10"]

    set_food = set(food_users)
    set_dessert = set(dessert_users)
    both_users = set_food.intersection(set_dessert)
    all_unique = set_food.union(set_dessert)

    prob = probability_both_ordered(food_users, dessert_users)

    print(f"Users Who Ordered Food:          {sorted(list(set_food))} (Count: {len(set_food)})")
    print(f"Users Who Ordered Dessert:       {sorted(list(set_dessert))} (Count: {len(set_dessert)})")
    print(f"Users Who Ordered BOTH (A n B):  {sorted(list(both_users))} (Count: {len(both_users)})")
    print(f"Total Unique Users (A u B):      {sorted(list(all_unique))} (Count: {len(all_unique)})\n")

    print(f"Formula: P(Food AND Dessert) = |Food n Dessert| / |Total Unique Users|")
    print(f"Result:  {len(both_users)} / {len(all_unique)} = {prob:.4f} ({prob * 100:.2f}%)")


# -------------------------------------------------------------------------
# TASK 5: Conditional Probability in Flipkart Recommendations
# -------------------------------------------------------------------------
def task_5():
    print("\n" + "=" * 70)
    print("TASK 5: Conditional Probability for Flipkart Product Recommendations")
    print("=" * 70)

    print("Explanation:")
    print("  Conditional Probability P(B | A) represents the likelihood of an event B occurring,")
    print("  given that event A has already occurred.\n")
    print("  In E-Commerce (Flipkart):")
    print("    P(Headphones | Phone) = P(Bought Both Phone and Headphones) / P(Bought Phone)")
    print("                          = Count(Bought Both) / Count(Bought Phone)\n")
    print("  Recommendation Use Case:")
    print("  If P(Headphones | Phone) is high (e.g., 68%), Flipkart's recommendation engine triggers")
    print("  a real-time 'Frequently Bought Together' bundle card or cart pop-up as soon as a customer")
    print("  adds a smartphone to their shopping cart.\n")

    # Python Code Example Simulation
    print("--- Python Code Example Simulation ---")
    total_customers = 1000
    phone_buyers = 300
    both_buyers = 210  # Customers who bought both phone and headphones

    # P(Phone)
    p_phone = phone_buyers / total_customers
    # P(Phone and Headphones)
    p_both = both_buyers / total_customers
    # Conditional Probability: P(Headphones | Phone)
    p_headphones_given_phone = both_buyers / phone_buyers

    print(f"Total Flipkart Customers Analyzed:       {total_customers}")
    print(f"Customers Who Bought a Phone:            {phone_buyers}")
    print(f"Customers Who Bought Both Phone & Audio: {both_buyers}\n")

    print(f"P(Phone):                                {phone_buyers}/{total_customers} = {p_phone:.2f}")
    print(f"P(Phone AND Headphones):                 {both_buyers}/{total_customers} = {p_both:.2f}")
    print(f"P(Headphones | Phone) = {both_buyers}/{phone_buyers} = {p_headphones_given_phone:.4f} ({p_headphones_given_phone * 100:.1f}%)")
    print("\nConclusion: With a 70% conditional purchase probability, recommending headphones")
    print("to phone shoppers will dramatically boost cross-sell conversion and average basket size.")


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
    print("All Session 8 tasks executed successfully!")
    print("=" * 70)
