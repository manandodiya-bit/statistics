# Session 12: Matrix Multiplication & Linear Regression Math Intuition

Welcome to **Session 12** of the Data Science & Statistics curriculum. This session bridges the gap between foundational **Linear Algebra (Matrix Operations)** and introductory **Machine Learning (Linear Regression intuition and Recommendation System architectures)**.

---

## 📌 Theoretical Intuition

### 1. Matrix Multiplication
In machine learning and statistics, matrix multiplication forms the bedrock of linear mappings, neural network layers, and similarity metrics:
- Given matrix $\mathbf{A} \in \mathbb{R}^{m \times k}$ and matrix $\mathbf{B} \in \mathbb{R}^{k \times n}$, their product $\mathbf{C} = \mathbf{A}\mathbf{B} \in \mathbb{R}^{m \times n}$ is defined element-wise by the dot product of the $i$-th row of $\mathbf{A}$ with the $j$-th column of $\mathbf{B}$:
  $$C_{i,j} = \sum_{r=1}^{k} A_{i,r} B_{r,j}$$
- **Key Requirement:** The inner dimensions must match ($k = k$).

### 2. Linear Regression Model
A simple linear regression equation predicts a continuous target variable $y$ from a single feature $x$:
$$y = mx + c \quad \text{or} \quad \hat{y} = w x + b$$
- **$x$ (Independent Variable / Feature):** Input measurement (e.g., delivery distance, product rating).
- **$m$ or $w$ (Slope / Weight):** The rate of change in $y$ for each unit change in $x$.
- **$c$ or $b$ (Intercept / Bias):** The expected baseline value of $y$ when $x = 0$.
- **$y$ or $\hat{y}$ (Dependent Variable / Target):** The predicted response.

---

## 📋 Tasks & Solutions

### Task 1: 2x2 Instagram Post Engagement Matrix Multiplication

#### Problem Statement
> *Given two 2x2 matrices representing the number of likes and comments on two Instagram posts over two days, write Python code to multiply them and display the resulting matrix.*

#### Formulation
Let Matrix $\mathbf{A}$ represent the engagements for Post 1 and Post 2 across Day 1 and Day 2:
$$\mathbf{A} = \begin{bmatrix} 120 & 45 \\ 80 & 60 \end{bmatrix}$$

Let Matrix $\mathbf{B}$ represent the channel engagement conversion weights:
$$\mathbf{B} = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$$

#### Matrix Product:
$$\mathbf{C} = \mathbf{A} \cdot \mathbf{B} = \begin{bmatrix} 120 & 45 \\ 80 & 60 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$$

Step-by-step element calculations:
- $C_{0,0} = (120 \times 2) + (45 \times 1) = 240 + 45 = \mathbf{285}$
- $C_{0,1} = (120 \times 1) + (45 \times 3) = 120 + 135 = \mathbf{255}$
- $C_{1,0} = (80 \times 2) + (60 \times 1) = 160 + 60 = \mathbf{220}$
- $C_{1,1} = (80 \times 1) + (60 \times 3) = 80 + 180 = \mathbf{260}$

$$\mathbf{C} = \begin{bmatrix} 285 & 255 \\ 220 & 260 \end{bmatrix}$$

#### Python Code
```python
import numpy as np

# Matrix A: Post 1 and Post 2 across Day 1 and Day 2
A = np.array([
    [120, 45],
    [80, 60]
])

# Matrix B: Interaction weights
B = np.array([
    [2, 1],
    [1, 3]
])

# Matrix multiplication
C = np.matmul(A, B)  # Or A @ B
print("Resulting Matrix C:")
print(C)
```

---

### Task 2: Linear Regression Prediction Function

#### Problem Statement
> *Create a simple Python function `linear_regression_predict(x, m, c)` that takes an input value `x`, slope `m`, and intercept `c`, and returns the predicted output `y` for a linear regression equation $y = mx + c$.*

#### Python Function Implementation
```python
from typing import Union
import numpy as np

def linear_regression_predict(
    x: Union[float, int, np.ndarray], 
    m: float, 
    c: float
) -> Union[float, np.ndarray]:
    """
    Predicts the target value y for a linear regression model: y = mx + c.
    
    Parameters:
        x: Input feature value (distance, rating, etc.)
        m: Slope (rate of change / weight)
        c: Intercept (baseline offset / bias)
        
    Returns:
        Predicted target output y
    """
    return m * x + c
```

---

### Task 3: Zomato Order Delivery Time Predictions

#### Problem Statement
> *Imagine you are predicting the delivery time for Zomato orders based on distance. Given three distances (2km, 5km, 8km) and a linear regression equation $y = 4x + 10$ (where $y$ is minutes), use your function from the previous task to calculate the predicted delivery time for each distance.*

#### Analysis
- Linear model: $y = 4x + 10$
  - Slope $m = 4$: Every additional kilometer adds **4 minutes** of transit time.
  - Intercept $c = 10$: Base restaurant prep, packaging, and rider dispatch buffer of **10 minutes**.

#### Calculations
1. **$x = 2 \text{ km}$:**
   $$y = 4(2) + 10 = 8 + 10 = \mathbf{18.0 \text{ minutes}}$$
2. **$x = 5 \text{ km}$:**
   $$y = 4(5) + 10 = 20 + 10 = \mathbf{30.0 \text{ minutes}}$$
3. **$x = 8 \text{ km}$:**
   $$y = 4(8) + 10 = 32 + 10 = \mathbf{42.0 \text{ minutes}}$$

#### Delivery Schedule Table
| Distance ($x$) | Formula ($4x + 10$) | Predicted Delivery Time ($y$) |
| :---: | :---: | :---: |
| **2 km** | $4(2) + 10$ | **18 minutes** |
| **5 km** | $4(5) + 10$ | **30 minutes** |
| **8 km** | $4(8) + 10$ | **42 minutes** |

---

### Task 4: Slope and Intercept Interpretation in Flipkart Price Prediction

#### Problem Statement
> *Explain in your own words what the slope and intercept represent in the context of Flipkart's product price prediction (e.g., predicting price based on product rating). Write 2-3 sentences for each term.*

#### 1. What the Slope ($m$) Represents:
> In Flipkart's product price model, the **slope ($m$)** represents the expected increase in a product's price for each additional 1-star improvement in customer rating. A positive slope indicates that highly rated products command a premium price because higher customer satisfaction signals superior build quality, durability, and brand reputation. For instance, a slope of ₹150 means that, on average, a 4.5-star product sells for ₹150 more than an otherwise comparable 3.5-star item.

#### 2. What the Intercept ($c$) Represents:
> The **intercept ($c$)** represents the estimated baseline price of a product when its rating is zero ($x = 0$). In an e-commerce context, this reflects the underlying fixed cost of manufacturing, packaging, warehousing, and platform logistics that any item incurs regardless of user reviews. While few items on Flipkart have an active rating of 0 stars, the intercept anchors the linear equation at its theoretical starting baseline before rating premiums are applied.

---

### Task 5: Matrix Multiplication in Spotify Recommender Systems

#### Problem Statement
> *Use ChatGPT to ask: "How does matrix multiplication help in training a machine learning model like Spotify's song recommendation system?" Summarize the answer in your own words in 3-4 sentences.*

#### Executive Summary (3-4 Sentences):
> In Spotify's recommendation engine, users and tracks are projected into lower-dimensional latent embedding vectors that capture musical taste, acoustic traits, and listening preferences. Through **Matrix Factorization** and deep collaborative filtering, matrix multiplication allows the system to compute billions of user-song affinity scores simultaneously across millions of catalog tracks. During model training, matrix operations parallelize forward predictions and backpropagation gradient updates on GPUs, making real-time, personalized playlist generation computationally scalable.

---

## 🚀 Execution & Verification
Run the complete Python script:
```bash
python "Session 12/session_12.py"
```

Or open the interactive Jupyter Notebook:
```bash
jupyter notebook "Session 12/session_12.ipynb"
```
