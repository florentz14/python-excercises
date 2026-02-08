"""
Machine Learning - Getting Started
===================================
Machine Learning is about making computers learn from data
and make predictions or decisions without being explicitly programmed.

Key concepts:
- Data Set: A collection of data used to train the model
- Features (X): Input variables used for prediction
- Labels (y): Output variable we want to predict
- Training: The process of learning patterns from data
- Prediction: Using the trained model on new data

Types of Machine Learning:
1. Supervised Learning   - learns from labeled data (regression, classification)
2. Unsupervised Learning - finds patterns in unlabeled data (clustering)
3. Reinforcement Learning - learns by trial and reward

Required libraries: numpy, scipy, scikit-learn, matplotlib
"""

# ============================================================
# 1. Check that required libraries are installed
# ============================================================
import sys

print("Python version:", sys.version)

try:
    import numpy as np
    print(f"NumPy version:        {np.__version__}")
except ImportError:
    print("NumPy is NOT installed. Run: pip install numpy")

try:
    import scipy
    print(f"SciPy version:        {scipy.__version__}")
except ImportError:
    print("SciPy is NOT installed. Run: pip install scipy")

try:
    import sklearn
    print(f"Scikit-learn version: {sklearn.__version__}")
except ImportError:
    print("Scikit-learn is NOT installed. Run: pip install scikit-learn")

try:
    import matplotlib
    print(f"Matplotlib version:   {matplotlib.__version__}")
except ImportError:
    print("Matplotlib is NOT installed. Run: pip install matplotlib")


# ============================================================
# 2. Basic workflow: Load data -> Train model -> Predict
# ============================================================
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data: hours studied vs exam score
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)  # Features (X)
exam_scores   = np.array([35, 45, 55, 60, 70, 75, 82, 90])          # Labels (y)

# Create and train the model
model = LinearRegression()
model.fit(hours_studied, exam_scores)

# Make a prediction
new_hours = np.array([[9]])
predicted_score = model.predict(new_hours)
print(f"\nPredicted exam score for 9 hours of study: {predicted_score[0]:.1f}")
# Output: Predicted exam score for 9 hours of study: ~95.4


# ============================================================
# 3. Understanding data types in ML
# ============================================================
"""
Data Types:
- Numerical  : numbers (age, salary, temperature)
  - Discrete   : countable (number of children)
  - Continuous  : measurable (weight, height)
- Categorical: labels / categories (color, yes/no)
  - Nominal    : no order (red, blue, green)
  - Ordinal    : ordered (low, medium, high)
"""

# Example: numerical vs categorical
import numpy as np

data = {
    "age":    [25, 30, 35, 40, 45],          # Numerical - continuous
    "city":   ["NY", "LA", "NY", "LA", "NY"], # Categorical - nominal
    "rating": ["low", "mid", "high", "mid", "high"],  # Categorical - ordinal
}

print("\nSample dataset:")
for key, values in data.items():
    print(f"  {key:8s} -> {values}")


# ============================================================
# 4. Train / Test split concept (preview)
# ============================================================
from sklearn.model_selection import train_test_split

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5, 7, 8, 9, 10, 12])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTrain/Test split (80/20):")
print(f"  Training samples: {len(X_train)}")
print(f"  Testing samples:  {len(X_test)}")
# Output: Training samples: 8, Testing samples: 2


# ============================================================
# 5. Model evaluation concept (preview)
# ============================================================
model2 = LinearRegression()
model2.fit(X_train, y_train)

score = model2.score(X_test, y_test)  # R² score
print(f"  Model R² score:   {score:.4f}")
# R² closer to 1.0 means better fit

print("\n--- Getting Started complete! ---")
