"""
SESSION 3 - Variance & Standard Deviation
------------------------------------------
This script contains complete solutions, step-by-step hand calculations,
and Python implementations for all 4 tasks in Session 3.
"""

import math
import statistics


# -------------------------------------------------------------------------
# TASK 1: Step Counts Variance Hand Calculation
# -------------------------------------------------------------------------
def task_1():
    print("=" * 70)
    print("TASK 1: Weekly Step Counts - Variance Calculation (Step-by-Step)")
    print("=" * 70)

    steps = [4500, 7000, 5000, 8000, 4000, 9000, 6000]
    n = len(steps)
    sum_steps = sum(steps)
    mean_steps = sum_steps / n

    print(f"Data Points (Step Counts): {steps}")
    print(f"Number of Days (n):         {n}")
    print(f"Sum of Steps (Sigma x):     {sum_steps}")
    print(f"Mean Steps (x_bar):         {sum_steps} / {n} = {mean_steps:.4f} steps\n")

    print(f"{'Day':<6}{'Steps (x_i)':<14}{'Deviation (x_i - mean)':<26}{'Squared Deviation (x_i - mean)^2':<32}")
    print("-" * 75)

    squared_deviations = []
    for idx, x in enumerate(steps, 1):
        dev = x - mean_steps
        sq_dev = dev ** 2
        squared_deviations.append(sq_dev)
        print(f"{idx:<6}{x:<14}{dev:<26.4f}{sq_dev:<32.2f}")

    sum_sq_dev = sum(squared_deviations)
    print("-" * 75)
    print(f"Sum of Squared Deviations:  {sum_sq_dev:.2f}\n")

    # Sample Variance (divided by n - 1)
    sample_var = sum_sq_dev / (n - 1)
    sample_sd = math.sqrt(sample_var)

    # Population Variance (divided by N)
    pop_var = sum_sq_dev / n
    pop_sd = math.sqrt(pop_var)

    print("Formulas & Final Results:")
    print(f"  1. Sample Variance (s^2)     = Sigma(x_i - x_bar)^2 / (n - 1)")
    print(f"                               = {sum_sq_dev:.2f} / 6 = {sample_var:.2f}")
    print(f"     Sample Std Dev (s)        = sqrt({sample_var:.2f}) = {sample_sd:.2f} steps\n")
    print(f"  2. Population Variance (sig^2)= Sigma(x_i - mu)^2 / N")
    print(f"                               = {sum_sq_dev:.2f} / 7 = {pop_var:.2f}")
    print(f"     Population Std Dev (sig)  = sqrt({pop_var:.2f}) = {pop_sd:.2f} steps")


# -------------------------------------------------------------------------
# TASK 2: Python Function for Standard Deviation
# -------------------------------------------------------------------------
def calculate_standard_deviation(scores):
    """
    Takes a list of exam scores and returns the sample standard deviation
    rounded to two decimal places.
    """
    if len(scores) < 2:
        return 0.0
    
    # Using arithmetic calculation:
    mean_val = sum(scores) / len(scores)
    squared_diff_sum = sum((x - mean_val) ** 2 for x in scores)
    variance = squared_diff_sum / (len(scores) - 1)
    std_dev = math.sqrt(variance)
    return round(std_dev, 2)


def task_2():
    print("\n" + "=" * 70)
    print("TASK 2: Python Function `calculate_standard_deviation(scores)`")
    print("=" * 70)

    sample_exam_scores = [78, 85, 92, 60, 88, 75, 95]
    result = calculate_standard_deviation(sample_exam_scores)
    builtin_result = round(statistics.stdev(sample_exam_scores), 2)

    print(f"Sample Exam Scores:        {sample_exam_scores}")
    print(f"Mean Score:                {statistics.mean(sample_exam_scores):.2f}")
    print(f"Custom Function Output:    {result}")
    print(f"statistics.stdev() Output: {builtin_result}")


# -------------------------------------------------------------------------
# TASK 3: Spending Consistency Comparison on Zomato
# -------------------------------------------------------------------------
def task_3():
    print("\n" + "=" * 70)
    print("TASK 3: Zomato Daily Spending Consistency (Friend A vs Friend B)")
    print("=" * 70)

    friend_a = [200, 200, 200, 200, 200]
    friend_b = [100, 300, 150, 400, 50]

    mean_a = statistics.mean(friend_a)
    sd_a = statistics.stdev(friend_a)

    mean_b = statistics.mean(friend_b)
    sd_b = statistics.stdev(friend_b)

    print("Friend A Spending (INR):", friend_a)
    print(f"  Mean:               INR {mean_a:.2f}")
    print(f"  Standard Deviation: INR {sd_a:.2f}\n")

    print("Friend B Spending (INR):", friend_b)
    print(f"  Mean:               INR {mean_b:.2f}")
    print(f"  Standard Deviation: INR {sd_b:.2f}\n")

    print("Explanation & Consistency Decision (2-3 lines):")
    print("  1. Friend A has a standard deviation of INR 0.00, meaning their spending exhibits zero")
    print("     variability and is 100% predictable (exactly INR 200 every single day).")
    print("  2. In contrast, Friend B has a high standard deviation of INR 145.77 despite having the exact")
    print("     same mean (INR 200), reflecting highly volatile daily spending between INR 50 and INR 400.")
    print("  3. Conclusion: Friend A has significantly more consistent spending than Friend B.")


# -------------------------------------------------------------------------
# TASK 4: Startup Employee Salary Spread & Interpretation
# -------------------------------------------------------------------------
def task_4():
    print("\n" + "=" * 70)
    print("TASK 4: Startup Monthly Salary Spread Analysis")
    print("=" * 70)

    salaries = [28000, 29000, 27000, 60000, 26500, 27500]
    n = len(salaries)
    mean_sal = statistics.mean(salaries)
    median_sal = statistics.median(salaries)
    var_sample = statistics.variance(salaries)
    sd_sample = statistics.stdev(salaries)
    var_pop = statistics.pvariance(salaries)
    sd_pop = statistics.pstdev(salaries)

    print(f"Monthly Salaries (INR):    {salaries}")
    print(f"Number of Employees:       {n}")
    print(f"Mean Salary:               INR {mean_sal:,.2f}")
    print(f"Median Salary:             INR {median_sal:,.2f}\n")

    print(f"Sample Variance (s^2):     {var_sample:,.2f}")
    print(f"Sample Std Dev (s):        INR {sd_sample:,.2f}")
    print(f"Population Variance (sigma^2): {var_pop:,.2f}")
    print(f"Population Std Dev (sigma):    INR {sd_pop:,.2f}\n")

    print("Interpretation of High Spread (2-3 lines):")
    print("  1. Five of the six employees earn very similar salaries tightly clustered between INR 26,500")
    print("     and INR 29,000, but the team's standard deviation is exceptionally high (over INR 13,000).")
    print("  2. This large spread is driven by a single high-earning outlier (INR 60,000, likely a founder or lead),")
    print("     which distorts the mean (INR 33,000) well above what 83% of the team actually makes.")
    print("  3. For this team, the median (INR 27,750) is a much fairer representation of standard employee pay.")


# -------------------------------------------------------------------------
# MAIN EXECUTION
# -------------------------------------------------------------------------
if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    print("\n" + "=" * 70)
    print("All Session 3 tasks executed successfully!")
    print("=" * 70)
