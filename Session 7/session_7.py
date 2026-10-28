"""
SESSION 7 - Correlation
-----------------------
This script contains complete solutions, numpy correlation calculations,
and matplotlib scatter plots for all 4 tasks in Session 7.
"""

import os
import matplotlib.pyplot as plt
import numpy as np


# -------------------------------------------------------------------------
# TASK 1: Instagram Hours vs. Posts Created (Scatter Plot & Relationship)
# -------------------------------------------------------------------------
def task_1():
    print("=" * 70)
    print("TASK 1: Instagram Hours vs. Posts Made (Scatter Plot & Visual Analysis)")
    print("=" * 70)

    # 7 days of tracking: Daily hours on Instagram vs. Number of posts created
    instagram_hours = [1.5, 2.0, 3.5, 2.5, 4.0, 5.0, 4.5]
    posts_created = [1, 1, 2, 2, 3, 4, 3]

    print(f"Instagram Hours (X): {instagram_hours}")
    print(f"Posts Made (Y):      {posts_created}")

    # Compute correlation coefficient using numpy
    r_matrix = np.corrcoef(instagram_hours, posts_created)
    r = r_matrix[0, 1]
    print(f"\nPearson Correlation Coefficient (r): {r:.4f}")

    print("\nVisual & Statistical Description:")
    print("  Relationship: STRONG POSITIVE CORRELATION")
    print("  Reasoning:")
    print("  1. The scatter plot displays an upward-sloping pattern moving from bottom-left to top-right.")
    print("  2. Days with higher app usage (e.g., 4.0 to 5.0 hours) coincide with a greater number")
    print("     of posts created (3 to 4 posts), while low-usage days (1.5 to 2.0 hours) show only 1 post.")
    print(f"  3. The correlation coefficient r = {r:.2f} (close to +1.0) confirms a strong positive linear relationship.")

    # Generate and save scatter plot
    current_dir = os.path.dirname(os.path.abspath(__file__))
    plots_dir = os.path.join(current_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    plot_path = os.path.join(plots_dir, "task_1_instagram_scatter.png")

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.scatter(instagram_hours, posts_created, color="#E1306C", s=90, edgecolors="black", linewidth=1.2, zorder=3)

    # Add linear trend line
    m, c = np.polyfit(instagram_hours, posts_created, 1)
    x_line = np.linspace(min(instagram_hours) - 0.5, max(instagram_hours) + 0.5, 100)
    ax.plot(x_line, m * x_line + c, color="#833AB4", linestyle="--", linewidth=2, label=f"Trend Line (r = {r:.2f})")

    ax.set_title("Session 7 Task 1: Instagram Daily Hours vs. Posts Made", fontsize=12, fontweight="bold")
    ax.set_xlabel("Hours Spent on Instagram Daily", fontsize=10)
    ax.set_ylabel("Number of Posts Made", fontsize=10)
    ax.legend()
    ax.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"[+] Plot saved to: {plot_path}")


# -------------------------------------------------------------------------
# TASK 2: Zomato vs. Swiggy Order Count Correlation (numpy corrcoef)
# -------------------------------------------------------------------------
def task_2():
    print("\n" + "=" * 70)
    print("TASK 2: Zomato vs. Swiggy Orders Correlation for 6 Friends")
    print("=" * 70)

    # Monthly orders placed by 6 friends on both food delivery platforms
    friends = ["Friend 1", "Friend 2", "Friend 3", "Friend 4", "Friend 5", "Friend 6"]
    zomato_orders = [18, 12, 25, 8, 15, 22]
    swiggy_orders = [16, 10, 24, 7, 14, 20]

    print("Friend-by-Friend Monthly Orders:")
    for f, z, s in zip(friends, zomato_orders, swiggy_orders):
        print(f"  {f:<10}: Zomato = {z:<3} | Swiggy = {s:<3}")

    # Calculate correlation matrix using numpy's corrcoef()
    corr_matrix = np.corrcoef(zomato_orders, swiggy_orders)
    r = corr_matrix[0, 1]

    print("\nNumPy Correlation Matrix (np.corrcoef):")
    print(corr_matrix)
    print(f"\nCorrelation Coefficient (r): {r:.4f}")

    print("\nExplanation of Correlation:")
    print("  Direction: POSITIVE CORRELATION (Strong, r > +0.95)")
    print("  Interpretation:")
    print("  1. The coefficient r is approximately +0.99, indicating a near-perfect positive linear relationship.")
    print("  2. Friends who order frequently on Zomato (high takeout propensity) also order frequently on Swiggy.")
    print("  3. Conversely, friends who rarely order food from restaurants order minimally on both platforms.")
    print("  4. Both variables increase together, reflecting overall food-delivery adoption rather than substitution.")


# -------------------------------------------------------------------------
# TASK 3: Real-Life Variables Correlation (Study Time vs. Screen Time)
# -------------------------------------------------------------------------
def task_3():
    print("\n" + "=" * 70)
    print("TASK 3: Two Real-Life Variables - Expected Correlation & Why")
    print("=" * 70)

    print("Selected Variables from Daily Life:")
    print("  Variable X: Daily Hours Spent on YouTube / Entertainment Screen Time")
    print("  Variable Y: Daily Hours Spent on Focused Study & Coding Practice\n")

    print("Paragraph Description & Justification:")
    print("  I expect a STRONG NEGATIVE CORRELATION between daily YouTube entertainment hours and")
    print("  daily focused study hours. Every individual has a finite allocation of approximately 16 waking")
    print("  hours per day. When non-academic screen time expands (e.g., spending 5-7 hours binge-watching")
    print("  YouTube videos), it directly cannibalizes time and mental bandwidth that could otherwise be")
    print("  dedicated to rigorous study and programming practice. Consequently, on days with high video")
    print("  consumption, study hours plummet to near zero, whereas on disciplined days with 6+ hours of deep")
    print("  study, entertainment screen time drops under an hour. Because the two variables move in opposite")
    print("  directions, their relationship exhibits an inverse, negative correlation (r < 0).")


# -------------------------------------------------------------------------
# TASK 4: Spotify Time vs. Test Marks (Strong Negative Correlation)
# -------------------------------------------------------------------------
def task_4():
    print("\n" + "=" * 70)
    print("TASK 4: Spotify Time vs. Test Marks (10 Pairs Strong Negative Correlation)")
    print("=" * 70)

    # 10 pairs generated showing a strong negative correlation
    # X: Daily hours spent listening to Spotify while studying/distracted
    # Y: Marks scored in the exam (out of 100)
    spotify_hours = np.array([0.5, 1.0, 1.5, 2.0, 3.0, 3.5, 4.0, 4.5, 5.5, 6.0])
    test_marks = np.array([94, 88, 85, 81, 72, 68, 60, 55, 44, 38])

    print("Generated Dataset (10 Pairs):")
    print(f"  Spotify Hours (X): {list(spotify_hours)}")
    print(f"  Test Marks (Y):    {list(test_marks)}\n")

    # Compute correlation coefficient using numpy
    r_matrix = np.corrcoef(spotify_hours, test_marks)
    r = r_matrix[0, 1]

    print(f"Calculated Correlation Coefficient (r): {r:.4f}")
    print("  -> Confirms an extremely STRONG NEGATIVE CORRELATION (r is near -1.0)!\n")

    # Generate and save scatter plot
    current_dir = os.path.dirname(os.path.abspath(__file__))
    plots_dir = os.path.join(current_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    plot_path = os.path.join(plots_dir, "task_4_spotify_vs_marks_negative_correlation.png")

    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    ax.scatter(spotify_hours, test_marks, color="#1DB954", s=90, edgecolors="black", linewidth=1.2, zorder=3, label="Student Observations")

    # Regression trend line
    m, c = np.polyfit(spotify_hours, test_marks, 1)
    x_vals = np.linspace(min(spotify_hours) - 0.2, max(spotify_hours) + 0.2, 100)
    ax.plot(x_vals, m * x_vals + c, color="#191414", linestyle="-", linewidth=2.2, label=f"Negative Trend Line (r = {r:.4f})")

    ax.set_title("Session 7 Task 4: Daily Spotify Hours vs. Test Marks (Strong Negative Correlation)", fontsize=11, fontweight="bold")
    ax.set_xlabel("Daily Time Spent on Spotify (Hours)", fontsize=10)
    ax.set_ylabel("Marks Scored in Test (out of 100)", fontsize=10)
    ax.set_ylim(25, 105)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"[+] Plot saved to: {plot_path}")


# -------------------------------------------------------------------------
# MAIN RUNNER
# -------------------------------------------------------------------------
if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    print("\n" + "=" * 70)
    print("All Session 7 tasks executed successfully!")
    print("=" * 70)
