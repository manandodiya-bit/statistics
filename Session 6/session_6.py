"""
SESSION 6 - Hypothesis Testing (Basic)
--------------------------------------
This script contains complete solutions, statistical tests,
and explanations for all 4 tasks in Session 6.
"""

import math
from scipy import stats


# -------------------------------------------------------------------------
# TASK 1: Null (H0) & Alternative (H1) Hypotheses Formulation
# -------------------------------------------------------------------------
def task_1():
    print("=" * 70)
    print("TASK 1: Hypotheses Formulation (Instagram vs. YouTube Daily Time)")
    print("=" * 70)

    print("Scenario: You believe that people spend more time on Instagram than on YouTube daily.\n")
    print("Let:")
    print("  mu_insta = Population mean daily time spent on Instagram (minutes)")
    print("  mu_yt    = Population mean daily time spent on YouTube (minutes)\n")

    print("Hypotheses Formulation (One-Tailed / Directional Test):")
    print("  Null Hypothesis (H0):")
    print("    H0: mu_insta <= mu_yt  (or mu_insta - mu_yt <= 0)")
    print("    In Plain English: People spend equal or less daily time on Instagram compared to YouTube.")
    print("    (There is no positive difference in daily screen time).\n")

    print("  Alternative Hypothesis (H1):")
    print("    H1: mu_insta > mu_yt   (or mu_insta - mu_yt > 0)")
    print("    In Plain English: People spend significantly MORE daily time on Instagram than on YouTube.")
    print("    (Reflects the researcher's directional claim).")

    print("\nAlternative Formulation (Standard Two-Tailed Test):")
    print("  H0: mu_insta = mu_yt (No difference between Instagram and YouTube daily screen time)")
    print("  H1: mu_insta != mu_yt (There is a significant difference in daily screen time)")


# -------------------------------------------------------------------------
# TASK 2: Two-Sample t-Test on Zomato Home Page Redesign
# -------------------------------------------------------------------------
def task_2():
    print("\n" + "=" * 70)
    print("TASK 2: Two-Sample t-Test (Zomato A/B Test on Average Order Value)")
    print("=" * 70)

    # Given data
    mean_a, sd_a, n_a = 350, 50, 30  # Group A: New Home Page
    mean_b, sd_b, n_b = 320, 50, 30  # Group B: Old Home Page
    alpha = 0.05

    print("Given Experiment Data:")
    print(f"  Group A (New Home Page): Mean = INR {mean_a}, SD = INR {sd_a}, n = {n_a}")
    print(f"  Group B (Old Home Page): Mean = INR {mean_b}, SD = INR {sd_b}, n = {n_b}")
    print(f"  Significance Level:      alpha = {alpha}\n")

    # Step-by-step formula calculation:
    # 1. Degrees of Freedom
    df = n_a + n_b - 2

    # 2. Pooled Standard Deviation
    sp2 = (((n_a - 1) * (sd_a ** 2)) + ((n_b - 1) * (sd_b ** 2))) / df
    sp = math.sqrt(sp2)

    # 3. Standard Error of the difference
    se = sp * math.sqrt((1 / n_a) + (1 / n_b))

    # 4. t-statistic
    t_stat = (mean_a - mean_b) / se

    # 5. p-value calculation using scipy.stats
    # Two-tailed test
    t_stat_scipy, p_val_two_tailed = stats.ttest_ind_from_stats(
        mean1=mean_a, std1=sd_a, nobs1=n_a,
        mean2=mean_b, std2=sd_b, nobs2=n_b,
        equal_var=True
    )
    p_val_one_tailed = p_val_two_tailed / 2

    print("Statistical Calculations:")
    print(f"  Degrees of Freedom (df):   {df}")
    print(f"  Pooled Std Dev (s_p):      INR {sp:.2f}")
    print(f"  Standard Error (SE):       INR {se:.4f}")
    print(f"  t-statistic (t):           {t_stat:.4f}")
    print(f"  p-value (Two-Tailed):      {p_val_two_tailed:.4f}")
    print(f"  p-value (One-Tailed):      {p_val_one_tailed:.4f}\n")

    # Decision rule
    print("-" * 70)
    print("DECISION & CONCLUSION (at alpha = 0.05):")
    print("-" * 70)
    if p_val_two_tailed < alpha:
        print(f"  Condition: p-value ({p_val_two_tailed:.4f}) < alpha ({alpha})")
        print("  Decision:  REJECT the Null Hypothesis (H0).")
        print("  Conclusion:")
        print("    There is statistically significant evidence at the 5% significance level that the")
        print("    new Zomato home page significantly increased average order value (INR 350 vs INR 320).")
        print("    Zomato can confidently roll out the new home page design.")
    else:
        print(f"  Condition: p-value ({p_val_two_tailed:.4f}) >= alpha ({alpha})")
        print("  Decision:  FAIL TO REJECT the Null Hypothesis (H0).")


# -------------------------------------------------------------------------
# TASK 3: A/B Test Design for a Favorite App Feature
# -------------------------------------------------------------------------
def task_3():
    print("\n" + "=" * 70)
    print("TASK 3: Complete A/B Test Design for an App Feature")
    print("=" * 70)

    print("Selected Feature: Paytm Redesigned Sticky 'Pay Now' Button\n")
    print("1. Context & Business Goal:")
    print("   Paytm wants to test whether replacing their standard payment button with a prominent,")
    print("   floating sticky 'Pay Now' button with instant biometric prompt increases successful checkout completion.\n")

    print("2. User Split & Groups:")
    print("   - Control Group (Group A): 50% of randomly sampled users who see the existing checkout screen")
    print("     with the standard static payment button.")
    print("   - Variant Group (Group B): 50% of randomly sampled users who see the newly redesigned floating")
    print("     sticky 'Pay Now' button with elevated contrast.\n")

    print("3. Metrics to Measure:")
    print("   - Primary Metric: Payment Conversion Rate (Checkout Completion Rate):")
    print("     (Completed Successful Payments / Total Users Entering Checkout Screen) * 100%")
    print("   - Guardrail Metrics: Payment drop-off / abandonment rate, average seconds to complete payment,\n"
          "     and customer support ticket volume regarding payment issues.\n")

    print("4. Hypotheses:")
    print("   - Null Hypothesis (H0):")
    print("     H0: p_variant = p_control")
    print("     (The redesigned sticky payment button has no effect on checkout completion rate).\n")
    print("   - Alternative Hypothesis (H1):")
    print("     H1: p_variant > p_control")
    print("     (The redesigned sticky payment button significantly increases checkout completion rate).")


# -------------------------------------------------------------------------
# TASK 4: Flipkart 'Add to Wishlist' Button A/B Test Analysis
# -------------------------------------------------------------------------
def task_4():
    print("\n" + "=" * 70)
    print("TASK 4: Flipkart Wishlist Button A/B Test (520 vs 480 Clicks out of 1000)")
    print("=" * 70)

    n = 1000
    clicks_new = 520
    clicks_old = 480

    p_new = clicks_new / n
    p_old = clicks_old / n

    print(f"Sample Size (Users per variant): n = {n}")
    print(f"New Button Clicks:  {clicks_new} / {n} ({p_new * 100:.1f}%)")
    print(f"Old Button Clicks:  {clicks_old} / {n} ({p_old * 100:.1f}%)\n")

    # Analytical Explanation
    print("1. Is this difference likely to be significant or just due to chance?")
    print("   Answer: It is LIKELY DUE TO RANDOM CHANCE (Not statistically significant).")
    print("   Reasoning:")
    print("   - The difference is only 40 clicks (4% percentage points: 52% vs 48%).")
    print("   - In a sample size of 1,000 users, an outcome of 52% vs 48% is typical random fluctuation,")
    print("     equivalent to tossing a fair coin 1,000 times and landing 520 heads.")
    print("   - The standard error for a 50/50 proportion with n=1000 is sqrt(0.5 * 0.5 / 1000) = 1.58%.")
    print("     The observed 2% deviation is well within the expected +/- 2 standard error noise range.\n")

    print("2. How does the p-value help you decide?")
    print("   - The p-value measures the exact probability of observing a difference of 40 clicks or larger")
    print("     purely by random luck, assuming both buttons are actually equally effective (H0 is true).")
    print("   - When the p-value is greater than the standard threshold (alpha = 0.05), we conclude that")
    print("     the observed gain cannot be distinguished from random noise.")
    print("   - This prevents Flipkart from investing engineering resources into rolling out a redesign")
    print("     that offers no true measurable lift.")

    # Verification with two-proportion z-test in Python
    count = [clicks_new, clicks_old]
    nobs = [n, n]
    # Pooled proportion
    p_pool = (clicks_new + clicks_old) / (2 * n)
    se_prop = math.sqrt(p_pool * (1 - p_pool) * (2 / n))
    z_score = (p_new - p_old) / se_prop
    p_val_z = 2 * (1 - stats.norm.cdf(abs(z_score)))

    print("\n--- Numerical Verification (Two-Proportion z-test) ---")
    print(f"  z-score: {z_score:.4f}")
    print(f"  p-value: {p_val_z:.4f} (approx 7.36%)")
    print(f"  Conclusion: Since p-value ({p_val_z:.4f}) >> 0.05, the difference is NOT statistically significant.")


# -------------------------------------------------------------------------
# MAIN RUNNER
# -------------------------------------------------------------------------
if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    print("\n" + "=" * 70)
    print("All Session 6 tasks executed successfully!")
    print("=" * 70)
