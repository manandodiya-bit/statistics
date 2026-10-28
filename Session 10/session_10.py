"""
SESSION 10 - Bayes Theorem (Basic)
----------------------------------
This script contains complete implementations of Bayes' Theorem functions,
Swiggy restaurant classification, Naive Bayes spam email filtering,
and an Instagram bot detection case study for Session 10.
"""


# -------------------------------------------------------------------------
# TASK 1: Generic Bayes' Posterior Probability Function
# -------------------------------------------------------------------------
def bayes_posterior(prior, likelihood, evidence):
    """
    Calculates and returns the posterior probability using Bayes' Theorem:
    P(A|B) = [P(B|A) * P(A)] / P(B)

    Parameters:
      prior: P(A) - Probability of hypothesis A before evidence B is observed.
      likelihood: P(B|A) - Probability of observing evidence B given hypothesis A is true.
      evidence: P(B) - Total marginal probability of observing evidence B.
    """
    if evidence <= 0:
        raise ValueError("Evidence P(B) must be greater than zero.")
    return (likelihood * prior) / evidence


def task_1():
    print("=" * 70)
    print("TASK 1: Function bayes_posterior() Implementation")
    print("=" * 70)

    # Example test: Medical test with 1% disease prevalence, 90% sensitivity, 5% false positive rate
    prior_disease = 0.01
    likelihood_pos = 0.90
    evidence_pos = (0.90 * 0.01) + (0.05 * 0.99)  # 0.0585

    posterior = bayes_posterior(prior_disease, likelihood_pos, evidence_pos)
    print("Bayes' Theorem Formula: P(A|B) = [P(B|A) * P(A)] / P(B)")
    print(f"  Prior P(Disease):          {prior_disease:.4f}")
    print(f"  Likelihood P(Test+|Disease): {likelihood_pos:.4f}")
    print(f"  Evidence P(Test+):         {evidence_pos:.4f}")
    print(f"  Posterior P(Disease|Test+): {posterior:.4f} ({posterior * 100:.2f}%)")


# -------------------------------------------------------------------------
# TASK 2: Swiggy Premium Restaurant Discount Classification
# -------------------------------------------------------------------------
def task_2():
    print("\n" + "=" * 70)
    print("TASK 2: Swiggy Premium Restaurant Probability Given a Discount")
    print("=" * 70)

    # Step 1: Define Priors
    # P(Premium): 10% of restaurants on Swiggy are premium
    p_premium = 0.10
    # P(Regular): 90% are regular restaurants
    p_regular = 1.0 - p_premium  # 0.90

    # Step 2: Define Likelihoods
    # P(Discount | Premium): 80% of premium restaurants offer a discount
    p_discount_given_premium = 0.80
    # P(Discount | Regular): 20% of regular restaurants offer a discount
    p_discount_given_regular = 0.20

    # Step 3: Calculate Total Evidence P(Discount) using the Law of Total Probability
    # P(Discount) = P(Discount | Premium) * P(Premium) + P(Discount | Regular) * P(Regular)
    p_discount = (p_discount_given_premium * p_premium) + (p_discount_given_regular * p_regular)

    # Step 4: Calculate Posterior P(Premium | Discount) using bayes_posterior()
    p_premium_given_discount = bayes_posterior(
        prior=p_premium,
        likelihood=p_discount_given_premium,
        evidence=p_discount
    )

    print("Defined Probabilities:")
    print(f"  Prior P(Premium):              {p_premium:.2f} (10%)")
    print(f"  Prior P(Regular):              {p_regular:.2f} (90%)")
    print(f"  Likelihood P(Discount|Premium): {p_discount_given_premium:.2f} (80%)")
    print(f"  Likelihood P(Discount|Regular): {p_discount_given_regular:.2f} (20%)\n")

    print(f"Total Evidence P(Discount):")
    print(f"  P(Discount) = (0.80 * 0.10) + (0.20 * 0.90) = 0.08 + 0.18 = {p_discount:.2f} (26%)\n")

    print(f"Posterior Probability P(Premium | Discount):")
    print(f"  P(Premium | Discount) = (0.80 * 0.10) / {p_discount:.2f}")
    print(f"                        = 0.08 / {p_discount:.2f} = {p_premium_given_discount:.4f} ({p_premium_given_discount * 100:.2f}%)")


# -------------------------------------------------------------------------
# TASK 3: Basic Spam Filter Simulation ('free' in Subject Line)
# -------------------------------------------------------------------------
def task_3():
    print("\n" + "=" * 70)
    print("TASK 3: Naive Bayes Email Spam Filter Simulation ('free')")
    print("=" * 70)

    # Dataset of 20 realistic email subjects with binary spam labels (1 = Spam, 0 = Ham/Not Spam)
    emails = [
        {"subject": "Get your free coupons now!", "is_spam": 1},
        {"subject": "Meeting rescheduled to 3 PM", "is_spam": 0},
        {"subject": "Claim your free trial access today", "is_spam": 1},
        {"subject": "Project status update for Q3", "is_spam": 0},
        {"subject": "Exclusive free luxury gift card inside", "is_spam": 1},
        {"subject": "Invoice for your recent purchase", "is_spam": 0},
        {"subject": "Urgent: Verify your account details", "is_spam": 1},
        {"subject": "Team lunch this Friday at noon", "is_spam": 0},
        {"subject": "Win free cash prizes instantly!", "is_spam": 1},
        {"subject": "Doctor appointment confirmation", "is_spam": 0},
        {"subject": "Earn extra income from home easily", "is_spam": 1},
        {"subject": "Flight ticket itinerary details", "is_spam": 0},
        {"subject": "Weekly product development newsletter", "is_spam": 0},
        {"subject": "Feel free to check out the shared document", "is_spam": 0},
        {"subject": "Your monthly bank statement is ready", "is_spam": 0},
        {"subject": "GitHub security alert for repository", "is_spam": 0},
        {"subject": "HR policy guidelines update", "is_spam": 0},
        {"subject": "Course assignment grades published", "is_spam": 0},
        {"subject": "Gym membership renewal reminder", "is_spam": 0},
        {"subject": "Coffee chat tomorrow morning?", "is_spam": 0}
    ]

    total_emails = len(emails)
    spam_emails = [e for e in emails if e["is_spam"] == 1]
    ham_emails = [e for e in emails if e["is_spam"] == 0]

    n_spam = len(spam_emails)
    n_ham = len(ham_emails)

    # 1. Priors
    p_spam = n_spam / total_emails
    p_ham = n_ham / total_emails

    # 2. Likelihoods: Check occurrences of 'free'
    spam_with_free = sum(1 for e in spam_emails if "free" in e["subject"].lower())
    ham_with_free = sum(1 for e in ham_emails if "free" in e["subject"].lower())

    p_free_given_spam = spam_with_free / n_spam
    p_free_given_ham = ham_with_free / n_ham

    # 3. Evidence P('free')
    p_free = (p_free_given_spam * p_spam) + (p_free_given_ham * p_ham)

    # 4. Posterior P(Spam | 'free')
    p_spam_given_free = bayes_posterior(
        prior=p_spam,
        likelihood=p_free_given_spam,
        evidence=p_free
    )

    print(f"Total Emails Analyzed:         {total_emails}")
    print(f"Spam Emails Count:             {n_spam} (Prior P(Spam) = {p_spam:.2f})")
    print(f"Ham (Non-Spam) Count:          {n_ham} (Prior P(Ham) = {p_ham:.2f})\n")

    print(f"Spam containing 'free':        {spam_with_free}/{n_spam} -> P('free'|Spam) = {p_free_given_spam:.4f}")
    print(f"Ham containing 'free':         {ham_with_free}/{n_ham} -> P('free'|Ham) = {p_free_given_ham:.4f}")
    print(f"Total Evidence P('free'):      {p_free:.4f}\n")

    print(f"Bayes Calculation: P(Spam | 'free') = [P('free'|Spam) * P(Spam)] / P('free')")
    print(f"Result: P(Spam | 'free') = ({p_free_given_spam:.4f} * {p_spam:.2f}) / {p_free:.4f}")
    print(f"                        = {p_spam_given_free:.4f} ({p_spam_given_free * 100:.2f}%)")
    print("\nInterpretation: If an email subject line contains the word 'free', there is an 80% chance it is spam.")


# -------------------------------------------------------------------------
# TASK 4: Real-World Bayes Theorem Example (Instagram Bot Detection)
# -------------------------------------------------------------------------
def task_4():
    print("\n" + "=" * 70)
    print("TASK 4: Real-World Bayes Theorem Problem & Solution (Instagram Bots)")
    print("=" * 70)

    print("PROMPT USED:")
    print("  'Generate a real-world Bayes Theorem probability problem for Instagram:")
    print("   calculating the probability that an account is a fake bot given that it leaves")
    print("   a generic repetitive comment like \"Great post!\". Include prior probabilities and likelihoods.'\n")

    print("PROBLEM SCENARIO:")
    print("  - On Instagram, 5% of active accounts are automated spam bots: P(Bot) = 0.05.")
    print("  - 95% of accounts are genuine real humans: P(Real) = 0.95.")
    print("  - 70% of bot accounts leave generic comments: P(Generic | Bot) = 0.70.")
    print("  - Only 10% of genuine users leave generic comments: P(Generic | Real) = 0.10.")
    print("  - Question: If an account leaves a generic comment on your photo, what is the")
    print("    probability that the account is actually an automated bot: P(Bot | Generic)?\n")

    # Code Solution:
    p_bot = 0.05
    p_real = 0.95
    p_generic_given_bot = 0.70
    p_generic_given_real = 0.10

    # Evidence: Total probability of generic comment
    p_generic = (p_generic_given_bot * p_bot) + (p_generic_given_real * p_real)

    # Posterior: P(Bot | Generic)
    p_bot_given_generic = bayes_posterior(
        prior=p_bot,
        likelihood=p_generic_given_bot,
        evidence=p_generic
    )

    print("CODE SOLUTION:")
    print(f"  Evidence P(Generic) = (0.70 * 0.05) + (0.10 * 0.95) = 0.035 + 0.095 = {p_generic:.4f}")
    print(f"  Posterior P(Bot | Generic) = (0.70 * 0.05) / {p_generic:.4f}")
    print(f"                             = 0.035 / {p_generic:.4f} = {p_bot_given_generic:.4f} ({p_bot_given_generic * 100:.2f}%)\n")

    print("Analytical Insight (Base Rate Fallacy):")
    print("  Even though bots are 7 times more likely to leave generic comments than humans (70% vs 10%),")
    print("  the posterior probability is only ~26.92%. This occurs because genuine humans vastly outnumber")
    print("  bots (95% vs 5%), meaning the majority of generic comments still come from real users.")


# -------------------------------------------------------------------------
# MAIN RUNNER
# -------------------------------------------------------------------------
if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    print("\n" + "=" * 70)
    print("All Session 10 tasks executed successfully!")
    print("=" * 70)
