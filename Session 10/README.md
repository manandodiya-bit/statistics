# Session 10 - Bayes Theorem (Basic)

This directory contains the solutions, Bayes' Theorem derivations, spam filter algorithms, and an interactive Jupyter Notebook for **Session 10: Bayes Theorem (Basic)**.

---

## Overview of Tasks

| Task | Topic | Core Focus | Deliverables & Posterior |
|---|---|---|---|
| **Task 1** | Bayes Formula Function | Function Implementation | `bayes_posterior(prior, likelihood, evidence)` calculating $P(A \mid B)$. |
| **Task 2** | Swiggy Premium Discount | Law of Total Probability | $P(\text{Premium} \mid \text{Discount}) = \mathbf{30.77\%}$ ($0.08 / 0.26$). |
| **Task 3** | Email Spam Filter | Keyword Classification ('free') | Naive Bayes filter classifying 20 emails $\rightarrow P(\text{Spam} \mid \text{'free'}) = \mathbf{80.00\%}$. |
| **Task 4** | Real-World App Problem | Instagram Bot Detection | Prompt & Python solution for detecting bots from generic comments ($\mathbf{26.92\%}$). |

---

## Task Details & Solutions

### Task 1: Generic Bayes' Posterior Probability Function

> **Prompt:** Write a Python function `bayes_posterior(prior, likelihood, evidence)` that calculates and returns the posterior probability using Bayes theorem formula for given values.

#### Mathematical Formula:
$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$
$$\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}$$

```python
def bayes_posterior(prior, likelihood, evidence):
    """
    Calculates posterior probability P(A|B) using Bayes' Theorem.
    """
    if evidence <= 0:
        raise ValueError("Evidence P(B) must be strictly greater than zero.")
    return (likelihood * prior) / evidence
```

---

### Task 2: Swiggy Premium Restaurant Probability Given a Discount

> **Prompt:** Given the following scenario: On Swiggy, 10% of restaurants are 'premium', and 80% of premium restaurants offer a discount, while only 20% of regular restaurants do. If you see a discount, use Bayes theorem in code to find the probability that the restaurant is premium.
>
> *Hint: Define prior, likelihood, and evidence in your code with comments.*

#### Probability Definitions:
1. **Priors:**
   - $P(\text{Premium}) = 0.10$
   - $P(\text{Regular}) = 1 - 0.10 = 0.90$
2. **Likelihoods:**
   - $P(\text{Discount} \mid \text{Premium}) = 0.80$
   - $P(\text{Discount} \mid \text{Regular}) = 0.20$
3. **Total Evidence $P(\text{Discount})$ (Law of Total Probability):**
   $$P(\text{Discount}) = P(\text{Discount} \mid \text{Premium}) \cdot P(\text{Premium}) + P(\text{Discount} \mid \text{Regular}) \cdot P(\text{Regular})$$
   $$P(\text{Discount}) = (0.80 \times 0.10) + (0.20 \times 0.90) = 0.08 + 0.18 = \mathbf{0.26}$$
4. **Posterior Calculation:**
   $$P(\text{Premium} \mid \text{Discount}) = \frac{0.80 \times 0.10}{0.26} = \frac{0.08}{0.26} \approx \mathbf{0.3077\text{ (30.77%)}}$$

---

### Task 3: Naive Bayes Email Spam Filter Simulation ('free')

> **Prompt:** Simulate a basic spam detection filter: Given a list of 20 email subjects (some spam, some not), and the probability that 'free' appears in spam vs non-spam emails, write code to calculate the probability an email is spam if it contains 'free', using Bayes theorem.

#### Sample Email Dataset ($N = 20$):
- **Spam Emails ($6$ total):**
  - $4$ contain 'free' (*"Get your free coupons"*, *"Claim free trial"*, *"Exclusive free gift"*, *"Win free cash"*).
  - Likelihood $P(\text{'free'} \mid \text{Spam}) = \frac{4}{6} \approx 0.6667$.
- **Ham / Non-Spam Emails ($14$ total):**
  - $1$ contains 'free' (*"Feel free to check out the shared document"*).
  - Likelihood $P(\text{'free'} \mid \text{Ham}) = \frac{1}{14} \approx 0.0714$.
- **Priors:** $P(\text{Spam}) = \frac{6}{20} = 0.30$, $P(\text{Ham}) = \frac{14}{20} = 0.70$.
- **Total Evidence:**
  $$P(\text{'free'}) = \left(\frac{4}{6} \times 0.30\right) + \left(\frac{1}{14} \times 0.70\right) = 0.20 + 0.05 = \mathbf{0.25}$$
- **Posterior Probability:**
  $$P(\text{Spam} \mid \text{'free'}) = \frac{0.6667 \times 0.30}{0.25} = \frac{0.20}{0.25} = \mathbf{0.8000\text{ (80.00%)}}$$

---

### Task 4: Real-World Bayes Theorem Problem (Instagram Bot Detection)

> **Prompt:** Use ChatGPT or Copilot to generate a real-world Bayes theorem example related to any app you use (Instagram, Zomato, Flipkart, etc.), then write code to solve it and submit both the prompt you used and your code.

#### Prompt Submitted:
> *"Generate a real-world Bayes Theorem probability problem for Instagram: calculating the probability that an account is a fake bot given that it leaves a generic repetitive comment like 'Great post!'. Include prior probabilities and likelihoods."*

#### Problem Scenario:
- On Instagram, $5\%$ of active accounts are automated spam bots ($P(\text{Bot}) = 0.05$), while $95\%$ are genuine humans ($P(\text{Real}) = 0.95$).
- $70\%$ of bots leave generic comments ($P(\text{Generic} \mid \text{Bot}) = 0.70$).
- $10\%$ of real users leave generic comments ($P(\text{Generic} \mid \text{Real}) = 0.10$).
- Question: If an account posts a generic comment on your photo, what is the probability that it is a bot?

#### Code & Mathematical Solution:
```python
p_bot = 0.05
p_real = 0.95
p_gen_given_bot = 0.70
p_gen_given_real = 0.10

# Total evidence P(Generic)
p_generic = (p_gen_given_bot * p_bot) + (p_gen_given_real * p_real)  # 0.1300

# Posterior P(Bot | Generic)
p_bot_given_generic = (p_gen_given_bot * p_bot) / p_generic
print(f"P(Bot | Generic) = {p_bot_given_generic:.4f}")  # 0.2692 (26.92%)
```

#### Analytical Insight (Base Rate Fallacy):
Even though bots are 7 times more likely to post generic comments than real humans (70% vs 10%), the probability that a generic commenter is a bot is only **$26.92\%$**. Because real human users vastly outnumber bots ($95\%$ vs $5\%$), the majority ($73.08\%$) of generic comments still originate from real users.

---

## How to Run

1. Run the Python script:
   ```bash
   python session_10.py
   ```
2. Open the Jupyter Notebook:
   ```bash
   jupyter notebook session_10.ipynb
   ```
