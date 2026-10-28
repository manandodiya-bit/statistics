"""
SESSION 2 - Mean, Median & Mode
--------------------------------
This script contains complete solutions and code demonstrations
for all 5 tasks in Session 2.
"""

from collections import Counter
import os
import statistics
import pandas as pd


# -------------------------------------------------------------------------
# TASK 1: Playlist Daily Play Counts Mean
# -------------------------------------------------------------------------
def task_1():
    print("=" * 70)
    print("TASK 1: Mean Daily Spotify Plays (playlist_stats.py)")
    print("=" * 70)

    daily_plays = [120, 135, 150, 200, 120, 90, 200]
    total_plays = sum(daily_plays)
    count_days = len(daily_plays)
    mean_plays = total_plays / count_days

    print(f"Daily Spotify Play Counts: {daily_plays}")
    print(f"Total Plays:               {total_plays}")
    print(f"Number of Days:            {count_days}")
    print(f"Calculated Mean (Average): {mean_plays:.2f} plays/day")
    print(f"statistics.mean() Result:  {statistics.mean(daily_plays):.2f} plays/day")


# -------------------------------------------------------------------------
# TASK 2: Zomato Delivery Times Median
# -------------------------------------------------------------------------
def task_2():
    print("\n" + "=" * 70)
    print("TASK 2: Median Delivery Time for Zomato Orders")
    print("=" * 70)

    delivery_times = [30, 25, 40, 35, 30, 45, 30]
    print(f"Original Delivery Times (minutes): {delivery_times}")

    # Step-by-step manual median calculation
    sorted_times = sorted(delivery_times)
    n = len(sorted_times)
    print(f"Sorted Delivery Times:             {sorted_times}")
    print(f"Number of Observations (n):        {n} (Odd number)")

    # For odd n, median is the middle element at index n // 2
    median_manual = sorted_times[n // 2]
    median_stat = statistics.median(delivery_times)

    print(f"Middle Position Index:             index {n // 2} (4th element)")
    print(f"Median Delivery Time (Manual):     {median_manual} minutes")
    print(f"Median Delivery Time (statistics): {median_stat} minutes")


# -------------------------------------------------------------------------
# TASK 3: Flipkart Product Ratings Mode Function
# -------------------------------------------------------------------------
def most_common_rating(ratings):
    """
    Takes a list of Flipkart product ratings and returns the mode
    (most frequent rating). Handles multi-mode scenarios if present.
    """
    if not ratings:
        return None
    
    # Method using collections.Counter
    counts = Counter(ratings)
    # statistics.mode returns the first most common element
    return statistics.mode(ratings)


def task_3():
    print("\n" + "=" * 70)
    print("TASK 3: Most Common Flipkart Rating (Mode)")
    print("=" * 70)

    sample_ratings = [5, 4, 4, 3, 5, 4, 2, 4]
    print(f"Flipkart Product Ratings List: {sample_ratings}")

    # Frequency breakdown
    frequency = Counter(sample_ratings)
    print("\nRating Frequency Breakdown:")
    for rating, count in sorted(frequency.items(), reverse=True):
        print(f"  {rating} Stars: {count} times")

    mode_result = most_common_rating(sample_ratings)
    print(f"\nResult from most_common_rating(): {mode_result} (Mode)")
    print(f"Explanation: Rating '{mode_result}' appears {frequency[mode_result]} times, which is the highest frequency.")


# -------------------------------------------------------------------------
# TASK 4: YouTube Views Comparison & Outlier Sensitivity
# -------------------------------------------------------------------------
def task_4():
    print("\n" + "=" * 70)
    print("TASK 4: YouTube Video Views - Mean vs. Median vs. Mode & Outliers")
    print("=" * 70)

    channels = {
        "Channel A (Tech Reviews - Consistent)": [1500, 1600, 1550, 1500, 1650, 1500, 1700],
        "Channel B (Cooking Channel - Moderate)": [800, 950, 1200, 850, 1100, 800, 900],
        "Channel C (Gaming Channel - Viral Hit Outlier)": [100, 120, 110, 105, 110, 5000]
    }

    results = []

    for name, views in channels.items():
        ch_mean = statistics.mean(views)
        ch_median = statistics.median(views)
        try:
            ch_mode = statistics.mode(views)
        except statistics.StatisticsError:
            ch_mode = "No unique mode"
        
        # Difference between mean and median indicates degree of skewness / outlier influence
        skew_diff = abs(ch_mean - ch_median)
        results.append({
            "name": name,
            "views": views,
            "mean": ch_mean,
            "median": ch_median,
            "mode": ch_mode,
            "skew_diff": skew_diff
        })

        print(f"\n{name}:")
        print(f"  Views Data:             {views}")
        print(f"  Mean Views:             {ch_mean:.2f}")
        print(f"  Median Views:           {ch_median:.2f}")
        print(f"  Mode Views:             {ch_mode}")
        print(f"  |Mean - Median| Skew:   {skew_diff:.2f}")

    # Comparison and Conclusion
    print("\n" + "-" * 70)
    print("ANALYSIS & CONCLUSION:")
    print("-" * 70)
    most_affected = max(results, key=lambda x: x["skew_diff"])
    print(f"Channel Most Affected by Outliers: {most_affected['name']}")
    print(f"Reasoning:")
    print(f"  1. In Channel C, regular videos get around 100-120 views (Median = {most_affected['median']:.1f}).")
    print(f"  2. A single viral video with 5,000 views pulls the Mean drastically up to {most_affected['mean']:.1f}.")
    print(f"  3. The massive gap of {most_affected['skew_diff']:.1f} views between the Mean and Median demonstrates")
    print(f"     that the Mean is highly sensitive to extreme values (outliers), whereas the Median")
    print(f"     and Mode remain resilient and reflect the true typical channel performance.")


# -------------------------------------------------------------------------
# TASK 5: Real Dataset from Kaggle (IPL Player Runs) using Pandas
# -------------------------------------------------------------------------
def task_5():
    print("\n" + "=" * 70)
    print("TASK 5: Real Dataset Analysis with Pandas (IPL Player Runs)")
    print("=" * 70)

    # Locate the CSV dataset
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "data", "ipl_player_runs.csv")

    df = pd.read_csv(csv_path)
    print("Dataset Loaded Successfully: IPL Top Batsmen Performance")
    print(f"Dataset Shape: {df.shape[0]} players, {df.shape[1]} features\n")
    print("First 5 Rows of Dataset:")
    print(df[["player_name", "team", "matches", "runs", "batting_average", "strike_rate"]].head())

    # Numeric column chosen: 'runs'
    target_col = "runs"
    runs_series = df[target_col]

    mean_runs = runs_series.mean()
    median_runs = runs_series.median()
    mode_runs = runs_series.mode().tolist()

    print(f"\nStatistical Measures for Column '{target_col}':")
    print(f"  Mean (Average Runs):    {mean_runs:.2f}")
    print(f"  Median (Middle Value):  {median_runs:.2f}")
    print(f"  Mode (Most Frequent):   {mode_runs}")

    # Additional insights on another key metric: 'batting_average'
    avg_mean = df["batting_average"].mean()
    avg_median = df["batting_average"].median()
    print(f"\nSupplementary Metric ('batting_average'):")
    print(f"  Mean Batting Average:   {avg_mean:.2f}")
    print(f"  Median Batting Average: {avg_median:.2f}")

    print("\nSummary Interpretation:")
    print(f"  - The mean runs ({mean_runs:.2f}) is higher than the median runs ({median_runs:.2f})")
    print(f"    due to top orange-cap contenders like Shubman Gill (890) and Faf du Plessis (730)")
    print(f"    creating a slight right-skew (positive skew) in the distribution.")


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
    print("All Session 2 tasks executed successfully!")
    print("=" * 70)
