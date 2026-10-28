"""
SESSION 4 - Skewness (Basic)
----------------------------
This script contains complete solutions, statistical analysis,
and visualization scripts for all 4 tasks in Session 4.
"""

from collections import Counter
import os
import statistics
import matplotlib.pyplot as plt
import numpy as np


# -------------------------------------------------------------------------
# TASK 1: Swiggy Daily Order Counts Skewness & Plot
# -------------------------------------------------------------------------
def task_1():
    print("=" * 70)
    print("TASK 1: Swiggy Delivery Partner Orders - Skewness Analysis & Plot")
    print("=" * 70)

    orders = [12, 15, 17, 14, 13, 16, 200, 18, 14, 15]
    sorted_orders = sorted(orders)
    n = len(orders)
    mean_orders = statistics.mean(orders)
    median_orders = statistics.median(orders)
    modes_orders = statistics.multimode(orders)

    print(f"Daily Order Counts: {orders}")
    print(f"Sorted Orders:      {sorted_orders}")
    print(f"Number of Days (n): {n}")
    print(f"Mean Orders:        {mean_orders:.2f}")
    print(f"Median Orders:      {median_orders:.2f}")
    print(f"Mode Orders:        {modes_orders}\n")

    print("Distribution Shape & Reasoning:")
    print("  Classification: RIGHT-SKEWED (Positively Skewed)")
    print("  Reasoning:")
    print("  1. The vast majority of daily orders (9 out of 10 days) cluster tightly between")
    print("     12 and 18 orders, forming a tall peak on the left side of the scale.")
    print("  2. An extreme single-day outlier of 200 orders (likely a festival catering drive)")
    print("     creates a long, stretched tail extending far to the right.")
    print("  3. As a result, the Mean (33.40) is pulled far to the right, significantly exceeding")
    print("     the Median (15.00), which is the classic signature of a right-skewed distribution.")

    # Generate Plot
    current_dir = os.path.dirname(os.path.abspath(__file__))
    plots_dir = os.path.join(current_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    plot_path = os.path.join(plots_dir, "swiggy_orders_distribution.png")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(orders, bins=[10, 20, 40, 80, 120, 160, 210], color="#fc8019", edgecolor="black", alpha=0.75, rwidth=0.85)
    ax.axvline(mean_orders, color="red", linestyle="--", linewidth=2.5, label=f"Mean = {mean_orders:.2f}")
    ax.axvline(median_orders, color="blue", linestyle="-", linewidth=2.5, label=f"Median = {median_orders:.2f}")

    ax.set_title("Session 4 Task 1: Swiggy Daily Orders Distribution (Right-Skewed)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Number of Orders Delivered", fontsize=11)
    ax.set_ylabel("Frequency (Days)", fontsize=11)
    ax.legend(fontsize=11)
    ax.grid(axis="y", linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"\n[+] Plot saved to: {plot_path}")


# -------------------------------------------------------------------------
# TASK 2: Instagram Influencer Followers Mean vs. Median & Skewness
# -------------------------------------------------------------------------
def task_2():
    print("\n" + "=" * 70)
    print("TASK 2: Instagram Influencer Followers - Mean vs. Median & Skewness")
    print("=" * 70)

    followers = [5, 7, 8, 8, 9, 10, 12, 15, 95]
    n = len(followers)
    mean_f = statistics.mean(followers)
    median_f = statistics.median(followers)

    print(f"Follower Counts (in thousands): {followers}")
    print(f"Number of Influencers (n):       {n}")
    print(f"Total Followers Sum:             {sum(followers)}k")
    print(f"Calculated Mean:                 {mean_f:.2f}k followers ({round(mean_f * 1000):,} followers)")
    print(f"Calculated Median:               {median_f:.2f}k followers ({round(median_f * 1000):,} followers)\n")

    print("Comparison & Conclusion:")
    print(f"  - Which is higher? The Mean ({mean_f:.2f}k) is substantially HIGHER than the Median ({median_f:.2f}k).")
    print(f"  - Difference:      Mean - Median = +{mean_f - median_f:.2f}k followers.")
    print("  - What this tells us about skewness:")
    print("    Because the Mean is pulled far above the Median by the extreme mega-influencer outlier (95k),")
    print("    the data is RIGHT-SKEWED (Positively Skewed).")
    print("    This confirms that the vast majority (8 out of 9 creators) have modest follower counts (5k-15k),")
    print("    while a rare exceptional account stretches the distribution's tail out to the right.")


# -------------------------------------------------------------------------
# TASK 3: Real-World Example of Right-Skewed App Data
# -------------------------------------------------------------------------
def task_3():
    print("\n" + "=" * 70)
    print("TASK 3: Real-World Example of Right-Skewed App Data")
    print("=" * 70)

    print("Selected Real-World App Example: Zomato Customer Order Amounts (Basket Size in INR)\n")
    print("1. Dataset Description:")
    print("   A dataset consisting of final invoice amounts (in INR) across thousands of daily customer")
    print("   orders placed on the Zomato food delivery app in an urban metropolitan area.\n")

    print("2. Why It Is Right-Skewed (Reasoning):")
    print("   - Hard Natural Lower Bound: Order values cannot be negative and rarely drop below INR 120-150")
    print("     due to minimum basket charges and restaurant price minimums.")
    print("   - High Peak (Mode): The vast majority of daily orders are single meals or couples dining,")
    print("     clustering heavily between INR 250 and INR 500.")
    print("   - Unbounded Long Right Tail: Occasionally, users place huge party orders, corporate catering,")
    print("     or order from fine-dining luxury restaurants totaling INR 4,000, INR 12,000, or INR 30,000+.")
    print("   - Result: These infrequent massive orders pull the arithmetic Mean significantly higher than")
    print("     the Median, producing an elongated tail on the right side.")


# -------------------------------------------------------------------------
# TASK 4: Flipkart Product Ratings Skewness & Plot
# -------------------------------------------------------------------------
def task_4():
    print("\n" + "=" * 70)
    print("TASK 4: Flipkart Product Ratings - Graph & Skewness Classification")
    print("=" * 70)

    ratings = [3, 3, 4, 4, 4, 5, 5, 5, 5, 5]
    freq = Counter(ratings)
    mean_r = statistics.mean(ratings)
    median_r = statistics.median(ratings)
    mode_r = statistics.mode(ratings)

    print(f"Flipkart Ratings Dataset: {ratings}")
    print(f"Frequency Distribution:   {dict(freq)}")
    print(f"Mean Rating:              {mean_r:.2f}")
    print(f"Median Rating:            {median_r:.2f}")
    print(f"Mode Rating:              {mode_r:.2f}\n")

    print("ASCII Frequency Histogram:")
    for star in [1, 2, 3, 4, 5]:
        count = freq.get(star, 0)
        bar = "#" * (count * 4)
        print(f"  {star} Star | {bar:<22} ({count})")

    print("\nClassification:")
    print("  -> LEFT-SKEWED (Negatively Skewed)")
    print("\nOne-Line Justification:")
    print("  The distribution is left-skewed because ratings concentrate heavily at the high end (5 stars),")
    print("  stretching a tail towards lower ratings on the left, resulting in Mean (4.30) < Median (4.50) < Mode (5.00).")

    # Generate Plot
    current_dir = os.path.dirname(os.path.abspath(__file__))
    plots_dir = os.path.join(current_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    plot_path = os.path.join(plots_dir, "flipkart_ratings_distribution.png")

    fig, ax = plt.subplots(figsize=(8, 4.5))
    stars = [1, 2, 3, 4, 5]
    counts = [freq.get(s, 0) for s in stars]

    bars = ax.bar(stars, counts, color="#2874f0", edgecolor="black", alpha=0.8, width=0.55)
    ax.axvline(mean_r, color="red", linestyle="--", linewidth=2.5, label=f"Mean = {mean_r:.2f}")
    ax.axvline(median_r, color="green", linestyle="-", linewidth=2.5, label=f"Median = {median_r:.2f}")
    ax.axvline(mode_r, color="purple", linestyle=":", linewidth=2.5, label=f"Mode = {mode_r:.2f}")

    # Add count labels on bars
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, h + 0.15, str(h), ha="center", va="bottom", fontweight="bold")

    ax.set_title("Session 4 Task 4: Flipkart Product Ratings Distribution (Left-Skewed)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Star Rating", fontsize=11)
    ax.set_ylabel("Review Count", fontsize=11)
    ax.set_xticks(stars)
    ax.set_ylim(0, 6.2)
    ax.legend(fontsize=10)
    ax.grid(axis="y", linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"\n[+] Plot saved to: {plot_path}")


# -------------------------------------------------------------------------
# MAIN RUNNER
# -------------------------------------------------------------------------
if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    print("\n" + "=" * 70)
    print("All Session 4 tasks executed successfully!")
    print("=" * 70)
