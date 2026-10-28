"""
Session 12: Matrix Multiplication & Linear Regression Math Intuition
--------------------------------------------------------------------
Applied Linear Algebra & Machine Learning Foundations:
- Task 1: 2x2 Instagram Engagement Matrix Multiplication
- Task 2: Linear Regression Prediction Function (y = mx + c)
- Task 3: Zomato Delivery Time Predictions (x = [2, 5, 8] km)
- Task 4: Slope and Intercept Interpretation in Flipkart Pricing
- Task 5: Matrix Multiplication in Spotify Recommender Systems
"""

from typing import List, Dict, Any, Union
import numpy as np


# =====================================================================
# Task 1: 2x2 Instagram Engagement Matrix Multiplication
# =====================================================================

def task_1_instagram_matrix_multiplication() -> Dict[str, Any]:
    """
    Task 1:
    Given two 2x2 matrices representing the number of likes and comments
    on two Instagram posts over two days, write Python code to multiply
    them and display the resulting matrix.
    """
    # Matrix A: Post 1 and Post 2 metrics [Likes, Comments] on Day 1 & Day 2
    # Row 0: Post 1 [Day 1, Day 2], Row 1: Post 2 [Day 1, Day 2]
    # Matrix A: Engagement count matrix (Post 1 vs Post 2 across Day 1 & Day 2)
    matrix_A: np.ndarray = np.array([
        [120, 45],   # Post 1: 120 likes/comments Day 1, 45 Day 2
        [80, 60]     # Post 2: 80 likes/comments Day 1, 60 Day 2
    ])

    # Matrix B: Weight / Interaction conversion matrix across 2 engagement channels
    # Row 0: Channel multiplier 1, Row 1: Channel multiplier 2
    matrix_B: np.ndarray = np.array([
        [2, 1],      # Weight multiplier for Day 1
        [1, 3]       # Weight multiplier for Day 2
    ])

    # Matrix Multiplication (Dot Product): C = A @ B
    matrix_C: np.ndarray = np.matmul(matrix_A, matrix_B)  # Equivalent to matrix_A @ matrix_B

    # Manual Step-by-Step calculation for demonstration:
    # C[0,0] = 120*2 + 45*1 = 240 + 45 = 285
    # C[0,1] = 120*1 + 45*3 = 120 + 135 = 255
    # C[1,0] = 80*2 + 60*1 = 160 + 60 = 220
    # C[1,1] = 80*1 + 60*3 = 80 + 180 = 260

    print("=" * 65)
    print("TASK 1: Instagram Post Engagement 2x2 Matrix Multiplication")
    print("=" * 65)
    print("Matrix A (Instagram Post Engagements):")
    print(matrix_A)
    print("\nMatrix B (Engagement Weight / Multiplier Matrix):")
    print(matrix_B)
    print("\nResult of Matrix Multiplication (A @ B):")
    print(matrix_C)

    print("\nStep-by-Step Dot Product Proof:")
    print(f"  C[0,0] = (120 * 2) + (45 * 1) = {120*2} + {45*1} = {matrix_C[0,0]}")
    print(f"  C[0,1] = (120 * 1) + (45 * 3) = {120*1} + {45*3} = {matrix_C[0,1]}")
    print(f"  C[1,0] = (80 * 2) + (60 * 1)  = {80*2} + {60*1}  = {matrix_C[1,0]}")
    print(f"  C[1,1] = (80 * 1) + (60 * 3)  = {80*1} + {60*3}  = {matrix_C[1,1]}\n")

    return {
        "matrix_A": matrix_A.tolist(),
        "matrix_B": matrix_B.tolist(),
        "result_matrix": matrix_C.tolist()
    }


# =====================================================================
# Task 2: Linear Regression Prediction Function
# =====================================================================

def linear_regression_predict(
    x: Union[float, int, np.ndarray, List[float]],
    m: float,
    c: float
) -> Union[float, np.ndarray]:
    """
    Predicts the output y for a simple linear regression equation:
        y = m * x + c

    Parameters:
        x (float, int, or array-like): Input feature value(s) (independent variable)
        m (float): Slope (rate of change / weight)
        c (float): Y-intercept (baseline constant / bias)

    Returns:
        float or np.ndarray: Predicted value(s) y (dependent variable)
    """
    if isinstance(x, (list, tuple)):
        x_arr = np.array(x, dtype=float)
        return m * x_arr + c
    return m * x + c


def task_2_demonstrate_prediction_function() -> None:
    """Demonstrates Task 2 function definition with test cases."""
    print("=" * 65)
    print("TASK 2: Simple Linear Regression Prediction Function")
    print("=" * 65)
    print("Function defined: linear_regression_predict(x, m, c)")
    print("Formula: y = m * x + c")
    # Quick test
    sample_x = 3.0
    sample_m = 2.5
    sample_c = 5.0
    sample_y = linear_regression_predict(sample_x, sample_m, sample_c)
    print(f"Test Evaluation: For x={sample_x}, m={sample_m}, c={sample_c} => y = {sample_y}\n")


# =====================================================================
# Task 3: Zomato Delivery Time Predictions
# =====================================================================

def task_3_zomato_delivery_predictions() -> Dict[str, Any]:
    """
    Task 3:
    Imagine predicting delivery time for Zomato orders based on distance.
    Given three distances (2km, 5km, 8km) and linear regression equation:
        y = 4x + 10 (where y is minutes, x is distance in km)
    Use linear_regression_predict() to calculate predicted delivery time.
    """
    distances_km = [2, 5, 8]
    slope_m = 4.0      # 4 minutes per kilometer
    intercept_c = 10.0 # 10 minutes base preparation and dispatch time

    predicted_times = [linear_regression_predict(d, slope_m, intercept_c) for d in distances_km]

    print("=" * 65)
    print("TASK 3: Zomato Order Delivery Time Predictions")
    print("=" * 65)
    print("Linear Regression Equation: y = 4x + 10")
    print("  - Feature (x): Distance in kilometers (km)")
    print("  - Slope (m = 4): Travel time rate (4 mins/km)")
    print("  - Intercept (c = 10): Fixed base kitchen preparation delay (10 mins)")
    print("  - Target (y): Estimated delivery time in minutes\n")

    print(f"{'Distance (km)':<15} | {'Equation':<15} | {'Predicted Delivery Time':<25}")
    print("-" * 60)

    results: List[Dict[str, Any]] = []
    for d, pred_y in zip(distances_km, predicted_times):
        eq_str = f"4*({d}) + 10"
        time_str = f"{pred_y:.1f} minutes"
        print(f"{d:<15} | {eq_str:<15} | {time_str:<25}")
        results.append({"distance_km": d, "predicted_minutes": pred_y})

    print("-" * 60)
    print("Summary:")
    print(f"  - 2 km order: {predicted_times[0]} minutes")
    print(f"  - 5 km order: {predicted_times[1]} minutes")
    print(f"  - 8 km order: {predicted_times[2]} minutes\n")

    return {
        "equation": "y = 4x + 10",
        "predictions": results
    }


# =====================================================================
# Task 4: Slope and Intercept Interpretation (Flipkart Pricing)
# =====================================================================

def task_4_flipkart_slope_intercept_explanation() -> Dict[str, str]:
    """
    Task 4:
    Explain in your own words what the slope and intercept represent
    in the context of Flipkart's product price prediction
    (e.g., predicting price based on product rating). Write 2-3 sentences for each.
    """
    slope_explanation = (
        "In Flipkart's product price model, the slope represents the expected change in a "
        "product's price for each additional 1-star increase in customer rating. A positive slope "
        "indicates that higher customer satisfaction commands a higher market price due to premium "
        "brand perception and verified buyer confidence. If the slope is 150, the product price rises "
        "by an estimated INR 150 for each full rating point gained."
    )

    intercept_explanation = (
        "The intercept represents the estimated baseline price of a product when its rating is zero "
        "(the theoretical starting value where x = 0). In a practical retail context, it reflects "
        "the intrinsic base cost of production, packaging, and platform listing fees before any consumer "
        "reviews are recorded. It provides the baseline starting anchor from which customer rating premiums "
        "are subsequently added."
    )

    print("=" * 65)
    print("TASK 4: Slope & Intercept Intuition (Flipkart Product Pricing)")
    print("=" * 65)
    print("[1] What the Slope (m) Represents:")
    print(f"    {slope_explanation}\n")
    print("[2] What the Intercept (c) Represents:")
    print(f"    {intercept_explanation}\n")

    return {
        "slope_interpretation": slope_explanation,
        "intercept_interpretation": intercept_explanation
    }


# =====================================================================
# Task 5: Matrix Multiplication in Spotify Recommender Systems
# =====================================================================

def task_5_spotify_recommendation_intuition() -> str:
    """
    Task 5:
    Use ChatGPT to ask: 'How does matrix multiplication help in training
    a machine learning model like Spotify's song recommendation system?'
    Summarize the answer in your own words in 3-4 sentences.
    """
    summary = (
        "In Spotify's recommendation engine, users and songs are mapped into dense latent feature vectors "
        "representing tastes and track attributes such as acousticness, tempo, and genre affinity. "
        "Matrix multiplication allows the system to compute billions of dot-product similarity scores between "
        "the user matrix and song feature matrix simultaneously in parallel on GPUs. During model training via "
        "collaborative filtering and deep neural networks, matrix multiplication accelerates vectorized forward "
        "passes and backpropagation weight adjustments, making real-time personalization scalable across millions "
        "of active listeners and catalog songs."
    )

    print("=" * 65)
    print("TASK 5: Matrix Multiplication in Spotify Recommender Engine")
    print("=" * 65)
    print("Summary of Matrix Multiplication in Spotify Recommendation ML:")
    print(f"\"{summary}\"\n")

    return summary


# =====================================================================
# Main Execution Block
# =====================================================================

if __name__ == "__main__":
    task_1_instagram_matrix_multiplication()
    task_2_demonstrate_prediction_function()
    task_3_zomato_delivery_predictions()
    task_4_flipkart_slope_intercept_explanation()
    task_5_spotify_recommendation_intuition()
