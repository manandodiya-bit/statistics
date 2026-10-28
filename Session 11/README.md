# Session 11: Vectors & Matrices (Basic)

Welcome to **Session 11** of the Data Science & Statistics curriculum. This session introduces foundational **Linear Algebra concepts**—specifically **Vectors and Matrices**—and their hands-on representation, indexing, and arithmetic operations using Python and NumPy.

---

## 📌 Conceptual Overview: Linear Algebra in Data Science

In modern Data Science, Machine Learning, and Big Data engineering:
1. **Scalars ($c \in \mathbb{R}$)**: Single numeric values (e.g., the price of one item, a user's age).
2. **Vectors ($\mathbf{v} \in \mathbb{R}^n$)**: 1-dimensional ordered arrays of numbers representing a single entity's features (e.g., song durations in a playlist, customer demographic vector, word embedding).
3. **Matrices ($\mathbf{M} \in \mathbb{R}^{m \times n}$)**: 2-dimensional grids with $m$ rows and $n$ columns (e.g., user-item rating matrices in collaborative filtering recommendation engines, transactional order ledgers across time).
4. **Tensors ($\mathcal{T} \in \mathbb{R}^{d_1 \times d_2 \times \dots \times d_k}$)**: Multidimensional generalizations (e.g., image batches `[batch, channels, height, width]`).

---

## 📋 Tasks & Solutions

### Task 1: 1D Vector Representation of Playlist Durations

#### Problem Statement
> *Create a Python list to represent a playlist of 5 song durations in seconds (e.g., `[210, 180, 245, 200, 175]`). Print the total duration of the playlist.*

#### Linear Algebra Formulation
A vector $\mathbf{d} \in \mathbb{R}^5$ represents the duration of 5 songs:
$$\mathbf{d} = \begin{bmatrix} 210 \\ 180 \\ 245 \\ 200 \\ 175 \end{bmatrix}$$

The total playlist duration is the sum of all vector components ($\ell_1$ norm or sum reduction):
$$T = \sum_{i=1}^{5} d_i = 210 + 180 + 245 + 200 + 175 = 1010 \text{ seconds}$$

#### Python Code
```python
import numpy as np

# Python list and NumPy vector
playlist_durations = [210, 180, 245, 200, 175]
d_vec = np.array(playlist_durations)

total_seconds = int(np.sum(d_vec))
minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"Playlist Durations: {playlist_durations}")
print(f"Total Duration: {total_seconds} seconds ({minutes}m {seconds}s)")
print(f"Mean Track Duration: {np.mean(d_vec):.1f}s")
```

#### Output
- **Total Duration:** `1010 seconds` (`16 minutes 50 seconds`)
- **Mean Track Length:** `202.0 seconds`
- **Vector Magnitude ($\|\mathbf{d}\|_2$):** `455.14`

---

### Task 2: 3x3 Swiggy Food Ratings Matrix

#### Problem Statement
> *Represent a 3x3 matrix in Python to store the ratings (1-5) given by 3 friends to 3 different food items on Swiggy. Print the matrix and display the rating each friend gave to the second food item.*

#### Mathematical Representation
Let $\mathbf{R} \in \mathbb{R}^{3 \times 3}$ be the User-Item Rating Matrix, where row $i$ represents Friend $i$ and column $j$ represents Food Item $j$:

$$\mathbf{R} = \begin{bmatrix} 5 & 4 & 3 \\ 3 & 5 & 2 \\ 4 & 2 & 5 \end{bmatrix}$$

- **Rows (Friends):** Friend 1 (Rahul), Friend 2 (Sneha), Friend 3 (Amit)
- **Columns (Food Items):** Biryani (Col 0), Butter Chicken (Col 1), Paneer Tikka (Col 2)

The ratings given to the **second food item** correspond to column index `1` (0-indexed in Python):
$$\mathbf{R}_{*, 1} = \begin{bmatrix} 4 \\ 5 \\ 2 \end{bmatrix}$$

#### Python Code
```python
import numpy as np

# 3x3 Matrix
ratings_matrix = np.array([
    [5, 4, 3],  # Friend 1
    [3, 5, 2],  # Friend 2
    [4, 2, 5]   # Friend 3
])

friends = ["Friend 1 (Rahul)", "Friend 2 (Sneha)", "Friend 3 (Amit)"]
second_item_name = "Butter Chicken (Item 2)"

# Slice column index 1
second_item_ratings = ratings_matrix[:, 1]

print("Ratings Matrix:")
print(ratings_matrix)

print(f"\nRatings for {second_item_name}:")
for friend, rating in zip(friends, second_item_ratings):
    print(f"  {friend}: {rating} / 5")
```

#### Output Table
| Friend | Biryani (Item 1) | Butter Chicken (Item 2) | Paneer Tikka (Item 3) |
| :--- | :---: | :---: | :---: |
| **Friend 1 (Rahul)** | 5 | **4** | 3 |
| **Friend 2 (Sneha)** | 3 | **5** | 2 |
| **Friend 3 (Amit)** | 4 | **2** | 5 |
| **Average Rating** | 4.00 | **3.67** | 3.33 |

---

### Task 3: 3x4 Orders Matrix & Dish Totals (Column Sums)

#### Problem Statement
> *Given a matrix representing the number of orders for 4 different dishes across 3 days (rows: days, columns: dishes), write code to calculate and print the total orders for each dish.*

#### Mathematical Formulation
Let $\mathbf{O} \in \mathbb{R}^{3 \times 4}$ be the order volume matrix:

$$\mathbf{O} = \begin{bmatrix}
12 & 18 & 25 & 10 \\
15 & 22 & 30 & 14 \\
20 & 25 & 35 & 18
\end{bmatrix}$$

To calculate the total orders for each dish, we sum across all days (rows), which is a **column sum reduction** along `axis=0`:
$$\mathbf{t}_{\text{dish}} = \mathbf{1}^T \mathbf{O} = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 12 & 18 & 25 & 10 \\ 15 & 22 & 30 & 14 \\ 20 & 25 & 35 & 18 \end{bmatrix} = \begin{bmatrix} 47 & 65 & 90 & 42 \end{bmatrix}$$

#### Python Code
```python
import numpy as np

orders_matrix = np.array([
    [12, 18, 25, 10],  # Day 1 (Friday)
    [15, 22, 30, 14],  # Day 2 (Saturday)
    [20, 25, 35, 18]   # Day 3 (Sunday)
])

dishes = ["Butter Chicken", "Paneer Tikka", "Masala Dosa", "Hakka Noodles"]

# Sum across rows (axis=0) to obtain column totals
total_orders_per_dish = np.sum(orders_matrix, axis=0)

for dish, total in zip(dishes, total_orders_per_dish):
    print(f"{dish}: {total} orders")
```

#### Breakdown Table
| Day | Butter Chicken | Paneer Tikka | Masala Dosa | Hakka Noodles | Daily Total |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Day 1 (Friday)** | 12 | 18 | 25 | 10 | 65 |
| **Day 2 (Saturday)** | 15 | 22 | 30 | 14 | 81 |
| **Day 3 (Sunday)** | 20 | 25 | 35 | 18 | 98 |
| **Total Orders (Dish)** | **47** | **65** | **90** | **42** | **244** |

- **Top Ordered Dish:** Masala Dosa (**90 orders**)

---

### Task 4: Flipkart Products Revenue (Price x Quantity Matrix)

#### Problem Statement
> *Imagine you have a table of 5 Flipkart products with columns for price and quantity sold. Represent this data as a matrix in Python, then write a function to calculate the total revenue for each product.*  
> *Hint: Multiply price and quantity for each row, then print the results.*

#### Mathematical Formulation
Let $\mathbf{P} \in \mathbb{R}^{5 \times 2}$ be the Flipkart inventory matrix:
$$\mathbf{P} = \begin{bmatrix}
\text{price}_1 & \text{quantity}_1 \\
\text{price}_2 & \text{quantity}_2 \\
\text{price}_3 & \text{quantity}_3 \\
\text{price}_4 & \text{quantity}_4 \\
\text{price}_5 & \text{quantity}_5
\end{bmatrix} = \begin{bmatrix}
499 & 120 \\
1499 & 85 \\
199 & 310 \\
999 & 65 \\
799 & 40
\end{bmatrix}$$

The revenue for each product is the row-wise product (or Hadamard product of the price and quantity column vectors):
$$\mathbf{r} = \mathbf{p} \odot \mathbf{q} = \begin{bmatrix} p_1 \cdot q_1 \\ p_2 \cdot q_2 \\ \dots \\ p_5 \cdot q_5 \end{bmatrix}$$

Total catalog revenue is the inner product (dot product):
$$R_{\text{total}} = \mathbf{p} \cdot \mathbf{q} = \sum_{i=1}^{5} p_i q_i$$

#### Python Function
```python
import numpy as np

def calculate_product_revenue(product_matrix: np.ndarray) -> np.ndarray:
    """
    Calculates total revenue for each product row.
    Revenue_i = Price_i * Quantity_i
    """
    prices = product_matrix[:, 0]
    quantities = product_matrix[:, 1]
    return prices * quantities

# 5 Flipkart products x 2 columns [Price (INR), Quantity Sold]
flipkart_matrix = np.array([
    [499.0, 120.0],   # Wireless Mouse
    [1499.0, 85.0],   # Bluetooth Headphones
    [199.0, 310.0],   # USB-C Cable
    [999.0, 65.0],    # 10000mAh Power Bank
    [799.0, 40.0]     # Laptop Stand
])

product_revenues = calculate_product_revenue(flipkart_matrix)
```

#### Revenue Calculation Table
| Product Name | Unit Price (INR) | Quantity Sold | Calculation | Total Revenue (INR) |
| :--- | :---: | :---: | :---: | :---: |
| **Wireless Mouse** | 499.00 | 120 | $499 \times 120$ | 59,880.00 |
| **Bluetooth Headphones** | 1,499.00 | 85 | $1499 \times 85$ | **127,415.00** |
| **USB-C Fast Cable** | 199.00 | 310 | $199 \times 310$ | 61,690.00 |
| **10000mAh Power Bank** | 999.00 | 65 | $999 \times 65$ | 64,935.00 |
| **Ergonomic Laptop Stand** | 799.00 | 40 | $799 \times 40$ | 31,960.00 |
| **Total Catalog Revenue** | — | **620 units** | — | **INR 345,880.00** |

---

## 🚀 Execution & Verification
To execute the complete script:
```bash
python "Session 11/session_11.py"
```
Or open the interactive Jupyter Notebook:
```bash
jupyter notebook "Session 11/session_11.ipynb"
```
