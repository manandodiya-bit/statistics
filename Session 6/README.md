# Session 6 - Hypothesis Testing (Basic)

This directory contains the solutions, step-by-step statistical formulations, Python implementations, and an interactive Jupyter Notebook for **Session 6: Hypothesis Testing (Basic)**.

---

## Overview of Tasks

| Task | Topic | Core Focus | Deliverables & Decision |
|---|---|---|---|
| **Task 1** | Hypotheses Formulation | Instagram vs YouTube daily time | Formulating directional ($H_0: \mu_{\text{Insta}} \le \mu_{\text{YT}}$ vs $H_1: \mu_{\text{Insta}} > \mu_{\text{YT}}$). |
| **Task 2** | Two-Sample t-Test | Zomato A/B Test on Order Value | $t = 2.3238$, $p = 0.0237 < 0.05$ $\rightarrow$ **Reject $H_0$** (Significant increase). |
| **Task 3** | A/B Test Experiment Setup | App Feature Redesign | Full framework for Paytm sticky "Pay Now" button conversion experiment. |
| **Task 4** | A/B Test Significance Analysis | Flipkart 'Add to Wishlist' button | Intuitive & statistical explanation of why 520 vs 480 ($p = 0.0736$) is due to chance. |

---

## Task Details & Solutions

### Task 1: Hypotheses Formulation (Instagram vs. YouTube)

> **Prompt:** Write down the null hypothesis (H0) and alternative hypothesis (H1) for the following scenario: You believe that people spend more time on Instagram than on YouTube daily.

#### Parameter Definitions:
- Let $\mu_{\text{Insta}}$ = Population mean daily time spent on Instagram (in minutes).
- Let $\mu_{\text{YT}}$ = Population mean daily time spent on YouTube (in minutes).

#### Formulations:
1. **One-Tailed (Directional) Formulation:**
   - **Null Hypothesis ($H_0$):**
     $$H_0: \mu_{\text{Insta}} \le \mu_{\text{YT}} \quad (\text{or } \mu_{\text{Insta}} - \mu_{\text{YT}} \le 0)$$
     *Plain English:* People spend equal or less time on Instagram compared to YouTube daily (no positive difference).
   - **Alternative Hypothesis ($H_1$):**
     $$H_1: \mu_{\text{Insta}} > \mu_{\text{YT}} \quad (\text{or } \mu_{\text{Insta}} - \mu_{\text{YT}} > 0)$$
     *Plain English:* People spend significantly more time on Instagram than on YouTube daily.

2. **Standard Two-Tailed Formulation:**
   - **$H_0$:** $\mu_{\text{Insta}} = \mu_{\text{YT}}$ (No difference in daily time spent).
   - **$H_1$:** $\mu_{\text{Insta}} \ne \mu_{\text{YT}}$ (There is a significant difference in daily time spent).

---

### Task 2: Two-Sample t-Test on Zomato Home Page Redesign

> **Prompt:** Given the data: Group A (users shown a new Zomato home page) had an average order value of ₹350 from 30 users, and Group B (old home page) had an average order value of ₹320 from 30 users. Assume both groups have a standard deviation of ₹50. Calculate the p-value using a two-sample t-test (you may use Python, R, or an online calculator), and decide whether to accept or reject the null hypothesis at a 0.05 significance level.
>
> *Hint: Use scipy.stats.ttest_ind in Python or any online t-test calculator if you are not comfortable with code.*

#### Given Parameters:
- **Group A (New Design):** $\bar{x}_1 = 350$, $s_1 = 50$, $n_1 = 30$
- **Group B (Old Design):** $\bar{x}_2 = 320$, $s_2 = 50$, $n_2 = 30$
- **Significance Level:** $\alpha = 0.05$

#### Step-by-Step Mathematical Calculation:
1. **Degrees of Freedom ($df$):**
   $$df = n_1 + n_2 - 2 = 30 + 30 - 2 = 58$$
2. **Pooled Variance ($s_p^2$) and Standard Deviation ($s_p$):**
   $$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2} = \frac{29(50^2) + 29(50^2)}{58} = 2500 \implies s_p = 50.00$$
3. **Standard Error of the Difference ($SE$):**
   $$SE = s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}} = 50 \sqrt{\frac{1}{30} + \frac{1}{30}} = 50 \sqrt{\frac{2}{30}} \approx \mathbf{12.9099}$$
4. **t-statistic ($t$):**
   $$t = \frac{\bar{x}_1 - \bar{x}_2}{SE} = \frac{350 - 320}{12.9099} \approx \mathbf{2.3238}$$
5. **p-value:**
   - Two-tailed p-value: $p = 2 \times P(T > 2.3238 \mid df = 58) \approx \mathbf{0.0237}$
   - One-tailed p-value: $p \approx \mathbf{0.0118}$

#### Decision & Conclusion:
- Since **$p\text{-value } (0.0237) < \alpha (0.05)$**, we **REJECT the null hypothesis ($H_0$)**.
- **Conclusion:** There is statistically significant evidence at the 5% significance level that the new home page design results in a higher average order value (₹350 vs. ₹320). Zomato can confidently roll out the redesign.

---

### Task 3: Complete A/B Test Design for an App Feature

> **Prompt:** Pick any feature from your favorite app (like the new dark mode in WhatsApp or a redesigned payment button in Paytm) and describe how you would set up an A/B test for it. Clearly state what your control and variant groups would be, what metric you would measure, and what your null and alternative hypotheses are.

#### Selected Feature: **Paytm Redesigned Sticky 'Pay Now' Button**

1. **User Groups:**
   - **Control Group ($A$):** $50\%$ of randomly sampled active users who experience the existing checkout screen with the static bottom payment button.
   - **Variant Group ($B$):** $50\%$ of randomly sampled active users who experience the redesigned floating sticky "Pay Now" button featuring elevated contrast and one-tap biometric confirmation.

2. **Metrics:**
   - **Primary Metric:** **Payment Conversion Rate (Checkout Completion Rate):**
     $$\text{Conversion Rate} = \frac{\text{Completed Successful Transactions}}{\text{Total Users Landing on Checkout Screen}} \times 100\%$$
   - **Guardrail Metrics:** Checkout abandonment rate, average seconds to complete payment, and payment error rates.

3. **Hypotheses:**
   - **Null Hypothesis ($H_0$):**
     $$H_0: p_{\text{variant}} = p_{\text{control}}$$
     *(The redesigned sticky payment button produces no difference in checkout completion rate).*
   - **Alternative Hypothesis ($H_1$):**
     $$H_1: p_{\text{variant}} > p_{\text{control}}$$
     *(The redesigned sticky payment button significantly increases checkout completion rate).*

---

### Task 4: Flipkart 'Add to Wishlist' Button A/B Test Analysis

> **Prompt:** Suppose you run an A/B test for a new 'Add to Wishlist' button design on Flipkart. Out of 1000 users, 520 clicked the new button versus 480 who clicked the old button. Without doing detailed calculations, explain if this difference is likely to be significant or just due to chance. Briefly explain how the p-value helps you decide.

#### 1. Is this difference likely to be significant or just due to chance?
- **Answer:** It is **LIKELY DUE TO RANDOM CHANCE (Not statistically significant)**.
- **Reasoning:**
  - Click rates are $52.0\%$ ($520/1000$) vs. $48.0\%$ ($480/1000$), a modest difference of only $40$ clicks ($4.0\%$).
  - In a sample size of $1,000$ users, a $52\%$ to $48\%$ split is completely typical random sampling variation (analogous to tossing a fair coin $1,000$ times and landing $520$ heads).
  - The standard error for a proportion around $0.50$ with $n = 1000$ is:
    $$SE = \sqrt{\frac{0.5 \times 0.5}{1000}} \approx 1.58\%$$
  - A $2\%$ shift from the midpoint ($50\%$) is only $\approx 1.26$ to $1.79$ standard errors away, well within the expected $\pm 2$ standard error range of natural random noise.

#### 2. How the p-value helps you decide:
- The **p-value** calculates the exact probability of observing an edge of $40$ clicks or larger purely by random luck if the null hypothesis is true (i.e., both buttons are actually identical in performance).
- Computing the two-proportion test yields **$p \approx 0.0736$ ($7.36\%$)**, which is **greater than the standard decision threshold of $\alpha = 0.05$**.
- Because $p > 0.05$, there is greater than a $7\%$ chance that this $40$-click lead was just a lucky fluctuation. Therefore, we **fail to reject $H_0$**, advising Flipkart not to commit engineering resources to a redesign that lacks proven statistical significance.

---

## How to Run

1. Run the Python verification script:
   ```bash
   python session_6.py
   ```
2. Launch the interactive Jupyter Notebook:
   ```bash
   jupyter notebook session_6.ipynb
   ```
