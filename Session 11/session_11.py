"""
Session 11: Vectors & Matrices (Basic)
--------------------------------------
Applied Linear Algebra & Statistics in Data Science:
- Task 1: 1D Vector Playlist Durations & Summation
- Task 2: 3x3 Swiggy Ratings Matrix & Column Slicing
- Task 3: 3x4 Restaurant Orders Matrix & Column Sums (axis=0)
- Task 4: 5x2 Flipkart Product Revenue Function (Hadamard Product)
"""

from typing import List, Tuple, Dict, Any
import numpy as np


# =====================================================================
# Task 1: Vector Representation of Playlist Durations
# =====================================================================

def task_1_playlist_durations() -> Dict[str, Any]:
    """
    Task 1:
    Create a Python list to represent a playlist of 5 song durations
    in seconds (e.g., [210, 180, 245, 200, 175]). Print total duration.
    """
    # Vector representation as Python list and NumPy 1D array
    song_durations: List[int] = [210, 180, 245, 200, 175]
    duration_vector: np.ndarray = np.array(song_durations)

    total_duration_sec: int = int(np.sum(duration_vector))
    minutes: int = total_duration_sec // 60
    remaining_seconds: int = total_duration_sec % 60

    print("=" * 60)
    print("TASK 1: Vector Representation of Playlist Durations")
    print("=" * 60)
    print(f"Playlist Durations Vector (seconds): {song_durations}")
    print(f"NumPy Vector Shape: {duration_vector.shape} (Dimension: {duration_vector.ndim}D)")
    print(f"Total Duration: {total_duration_sec} seconds ({minutes} mins {remaining_seconds} secs)")
    print(f"Average Song Duration: {np.mean(duration_vector):.1f} seconds")
    print(f"L2 Norm (Vector Magnitude): {np.linalg.norm(duration_vector):.2f}\n")

    return {
        "durations": song_durations,
        "total_seconds": total_duration_sec,
        "formatted_time": f"{minutes}m {remaining_seconds}s",
        "mean_duration": float(np.mean(duration_vector))
    }


# =====================================================================
# Task 2: 3x3 Swiggy Ratings Matrix
# =====================================================================

def task_2_swiggy_ratings_matrix() -> Dict[str, Any]:
    """
    Task 2:
    Represent a 3x3 matrix in Python to store the ratings (1-5) given
    by 3 friends to 3 different food items on Swiggy.
    Print the matrix and display the rating each friend gave to the second food item.
    """
    # Rows: Friends (Friend 1, Friend 2, Friend 3)
    # Columns: Food Items (Biryani, Butter Chicken / Pizza, Paneer Tikka)
    friends: List[str] = ["Friend 1 (Rahul)", "Friend 2 (Sneha)", "Friend 3 (Amit)"]
    food_items: List[str] = ["Biryani", "Butter Chicken (Item 2)", "Paneer Tikka"]

    # 3x3 Matrix
    ratings_matrix: np.ndarray = np.array([
        [5, 4, 3],  # Friend 1 ratings
        [3, 5, 2],  # Friend 2 ratings
        [4, 2, 5],  # Friend 3 ratings
    ])

    # Second food item corresponds to column index 1 (0-based indexing)
    second_item_index: int = 1
    second_item_ratings: np.ndarray = ratings_matrix[:, second_item_index]

    print("=" * 60)
    print("TASK 2: 3x3 Swiggy Food Ratings Matrix")
    print("=" * 60)
    print("Ratings Matrix (Rows: Friends, Columns: Food Items):")
    print(ratings_matrix)
    print("\nDetailed Matrix View:")
    header = f"{'Friend':<20} | " + " | ".join(f"{item:<25}" for item in food_items)
    print(header)
    print("-" * len(header))
    for i, friend in enumerate(friends):
        row_str = f"{friend:<20} | " + " | ".join(f"{ratings_matrix[i, j]:<25}" for j in range(3))
        print(row_str)

    print(f"\nRatings given to the SECOND food item ('{food_items[second_item_index]}'):")
    for i, friend in enumerate(friends):
        print(f"  - {friend}: {second_item_ratings[i]} / 5")

    avg_second_item: float = float(np.mean(second_item_ratings))
    print(f"Average rating for {food_items[second_item_index]}: {avg_second_item:.2f} / 5\n")

    return {
        "matrix": ratings_matrix.tolist(),
        "second_item_ratings": second_item_ratings.tolist(),
        "friends": friends,
        "second_item_name": food_items[second_item_index],
        "average_second_item_rating": avg_second_item
    }


# =====================================================================
# Task 3: 3x4 Orders Matrix & Dish Totals (Column Sums)
# =====================================================================

def task_3_dish_orders_matrix() -> Dict[str, Any]:
    """
    Task 3:
    Given a matrix representing the number of orders for 4 different dishes
    across 3 days (rows: days, columns: dishes), write code to calculate
    and print the total orders for each dish.
    """
    days: List[str] = ["Day 1 (Friday)", "Day 2 (Saturday)", "Day 3 (Sunday)"]
    dishes: List[str] = ["Butter Chicken", "Paneer Tikka", "Masala Dosa", "Hakka Noodles"]

    # 3 rows (days) x 4 columns (dishes)
    orders_matrix: np.ndarray = np.array([
        [12, 18, 25, 10],  # Day 1 orders
        [15, 22, 30, 14],  # Day 2 orders
        [20, 25, 35, 18],  # Day 3 orders
    ])

    # Total orders for each dish is the column sum (axis=0)
    total_orders_per_dish: np.ndarray = np.sum(orders_matrix, axis=0)

    print("=" * 60)
    print("TASK 3: Dish Orders Across Days (Matrix Column Sums)")
    print("=" * 60)
    print("Orders Matrix (Shape: 3 days x 4 dishes):")
    print(orders_matrix)
    print("\nDetailed Order Breakdown:")
    header = f"{'Day':<18} | " + " | ".join(f"{dish:<15}" for dish in dishes)
    print(header)
    print("-" * len(header))
    for i, day in enumerate(days):
        row_str = f"{day:<18} | " + " | ".join(f"{orders_matrix[i, j]:<15}" for j in range(4))
        print(row_str)

    print("-" * len(header))
    total_row = f"{'TOTAL ORDERS':<18} | " + " | ".join(f"{total_orders_per_dish[j]:<15}" for j in range(4))
    print(total_row)

    print("\nSummary per Dish:")
    dish_summary: Dict[str, int] = {}
    for j, dish in enumerate(dishes):
        dish_summary[dish] = int(total_orders_per_dish[j])
        print(f"  - {dish}: {total_orders_per_dish[j]} total orders")

    most_ordered_idx: int = int(np.argmax(total_orders_per_dish))
    print(f"\nMost Popular Dish: {dishes[most_ordered_idx]} ({total_orders_per_dish[most_ordered_idx]} orders)\n")

    return {
        "orders_matrix": orders_matrix.tolist(),
        "dish_totals": dish_summary,
        "most_ordered": dishes[most_ordered_idx]
    }


# =====================================================================
# Task 4: Flipkart Products Revenue (Price x Quantity Matrix)
# =====================================================================

def calculate_product_revenue(product_matrix: np.ndarray) -> np.ndarray:
    """
    Function to calculate total revenue for each product.
    Formula: Revenue_i = Price_i * Quantity_i

    Args:
        product_matrix: A 2D numpy array where:
                        - Column 0: Price of each product
                        - Column 1: Quantity sold of each product

    Returns:
        1D numpy array of revenues for each product row.
    """
    prices = product_matrix[:, 0]
    quantities = product_matrix[:, 1]
    # Element-wise vector multiplication (Hadamard product)
    revenues = prices * quantities
    return revenues


def task_4_flipkart_revenue() -> Dict[str, Any]:
    """
    Task 4:
    Imagine you have a table of 5 Flipkart products with columns for
    price and quantity sold. Represent this data as a matrix in Python,
    then write a function to calculate the total revenue for each product.
    (Multiply price and quantity for each row, then print the results).
    """
    product_names: List[str] = [
        "Wireless Mouse",
        "Bluetooth Headphones",
        "USB-C Fast Cable",
        "10000mAh Power Bank",
        "Ergonomic Laptop Stand"
    ]

    # 5 products x 2 columns [Price (INR), Quantity Sold]
    # Matrix representation
    flipkart_matrix: np.ndarray = np.array([
        [499.0, 120.0],   # Product 1
        [1499.0, 85.0],   # Product 2
        [199.0, 310.0],   # Product 3
        [999.0, 65.0],    # Product 4
        [799.0, 40.0],    # Product 5
    ])

    revenues: np.ndarray = calculate_product_revenue(flipkart_matrix)
    total_catalog_revenue: float = float(np.sum(revenues))

    print("=" * 60)
    print("TASK 4: Flipkart Product Revenue Calculation")
    print("=" * 60)
    print("Product Matrix [Price (INR), Quantity Sold]:")
    print(flipkart_matrix)
    print("\nDetailed Product Revenue Table:")
    header = f"{'Product Name':<25} | {'Price (INR)':<12} | {'Qty Sold':<10} | {'Total Revenue (INR)':<20}"
    print(header)
    print("-" * len(header))

    results: List[Dict[str, Any]] = []
    for i, name in enumerate(product_names):
        price = flipkart_matrix[i, 0]
        qty = int(flipkart_matrix[i, 1])
        rev = revenues[i]
        results.append({"product": name, "price": price, "quantity": qty, "revenue": rev})
        print(f"{name:<25} | INR {price:<8.2f} | {qty:<10} | INR {rev:<16.2f}")

    print("-" * len(header))
    print(f"{'OVERALL TOTAL REVENUE':<25} | {'':<12} | {'':<10} | INR {total_catalog_revenue:<16.2f}")

    top_product_idx: int = int(np.argmax(revenues))
    print(f"\nHighest Revenue Generator: {product_names[top_product_idx]} (INR {revenues[top_product_idx]:,.2f})\n")

    return {
        "matrix": flipkart_matrix.tolist(),
        "revenues": results,
        "total_revenue": total_catalog_revenue
    }


# =====================================================================
# Main Execution
# =====================================================================

if __name__ == "__main__":
    task_1_playlist_durations()
    task_2_swiggy_ratings_matrix()
    task_3_dish_orders_matrix()
    task_4_flipkart_revenue()
