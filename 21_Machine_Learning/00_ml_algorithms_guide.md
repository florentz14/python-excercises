# Guide: 15 Most Important Machine Learning Algorithms

**Author:** Florentino Báez  
**Focus:** Practical, simple language, scikit-learn

---

## Structure of Each Algorithm

1. **What it is**
2. **When to use it**
3. **Advantages**
4. **Disadvantages**
5. **Python example**

---

# 1) Linear Regression

## What it is

Supervised algorithm for **predicting continuous numerical values**.

Examples:
- predict house price
- predict salary
- predict sales

## When to use it

When the relationship between variables is approximately **linear**.

## Advantages

- Very simple
- Easy to interpret
- Fast

## Disadvantages

- Does not work well with complex relationships
- Sensitive to outliers

## Python

See: `24_linear_regression.py`

---

# 2) Logistic Regression

## What it is

Supervised algorithm for **classification**.

Although it's called "regression", it's used to answer questions like:
- yes or no?
- spam or not spam?
- fraud or not fraud?

## When to use it

When you want to classify between **two classes** or multiple classes.

## Advantages

- Easy to understand
- Very fast
- Good baseline

## Disadvantages

- May fall short with very complex data

## Python

See: `25_logistic_regression.py`

---

# 3) Decision Tree

## What it is

Model that makes decisions in the form of a **tree**.

Example:
- if income > 5000 → likely to buy
- if age < 25 → likely not to buy

## When to use it

When you want an easy-to-interpret model.

## Advantages

- Very visual
- Easy to explain
- Does not require much preprocessing

## Disadvantages

- Can overfit

## Python

See: `26_decision_tree.py`

---

# 4) Random Forest

## What it is

Ensemble of many decision trees.

Instead of relying on a single tree, it combines several to give a better answer.

## When to use it

When you want more accuracy than a single tree.

## Advantages

- Very powerful
- Reduces overfitting
- Works well on many real-world problems

## Disadvantages

- Less interpretable than a single tree
- More computationally expensive

## Python

See: `27_random_forest.py`

---

# 5) Support Vector Machine (SVM)

## What it is

Finds the best boundary to separate classes.

## When to use it

When data can be clearly separated and the dataset is not huge.

## Advantages

- Very effective at classification
- Works well in high-dimensional spaces

## Disadvantages

- Can be slow on large datasets
- Harder to interpret

## Python

See: `28_svm.py`

---

# 6) K-Nearest Neighbors (KNN)

## What it is

Classifies a data point based on its **nearest neighbors**.

Example: if the 3 nearest neighbors are "red", this point is probably "red" too.

## When to use it

On small or medium problems where proximity between points matters.

## Advantages

- Very intuitive
- Easy to implement

## Disadvantages

- Slow with large amounts of data
- Sensitive to variable scale

## Python

See: `29_knn.py`

---

# 7) Naive Bayes

## What it is

Probabilistic algorithm based on Bayes' theorem.

Widely used in:
- text classification
- spam detection
- sentiment analysis

## When to use it

When working with text or simple probabilities.

## Advantages

- Very fast
- Excellent for basic NLP

## Disadvantages

- Makes simplifying assumptions that are not always realistic

## Python

See: `30_naive_bayes.py`

---

# 8) K-Means Clustering

## What it is

Unsupervised algorithm for **grouping data into clusters**.

## When to use it

When you have no labels and want to discover natural groups.

## Advantages

- Easy to use
- Very popular
- Good for segmentation

## Disadvantages

- Must choose `k`
- Sensitive to scale and initialization

## Python

See: `31_kmeans.py`

---

# 9) Hierarchical Clustering

## What it is

Groups data by forming a **hierarchy of clusters**.

## When to use it

When you want to see relationships between groups and subgroups.

## Advantages

- Very useful for exploratory analysis
- You don't always need to define k upfront

## Disadvantages

- Can be expensive with large amounts of data

## Python

See: `32_hierarchical_clustering.py`

---

# 10) Principal Component Analysis (PCA)

## What it is

Technique for **dimensionality reduction**.

If you have many columns, PCA helps summarize them while preserving as much information as possible.

## When to use it

Before visualizing data or speeding up models.

## Advantages

- Reduces complexity
- Facilitates visualization
- Can improve performance

## Disadvantages

- Loses interpretability
- May lose important information

## Python

See: `33_pca.py`

---

# 11) Gradient Boosting

## What it is

Ensemble model that builds several weak models sequentially, correcting previous errors.

## When to use it

When you want high accuracy on tabular problems.

## Advantages

- Very powerful
- Excellent performance on structured data

## Disadvantages

- Slower
- Requires hyperparameter tuning

## Python

See: `34_gradient_boosting.py`

---

# 12) XGBoost

## What it is

Highly optimized version of boosting.

Widely used in competitions and real-world tabular problems.

## When to use it

When you seek high performance on tabular datasets.

## Advantages

- Very accurate
- Very popular
- Excellent in Kaggle and production

## Disadvantages

- More complex
- Requires additional installation: `pip install xgboost`

## Python

See: `35_xgboost.py`

---

# 13) Artificial Neural Network (MLP)

## What it is

Basic neural network with layers.

## When to use it

When the problem is more complex than what classical models can solve.

## Advantages

- Flexible
- Can capture nonlinear relationships

## Disadvantages

- Requires more data
- Less interpretable

## Python

See: `36_mlp_neural_network.py`

---

# 14) Recurrent Neural Network (RNN) / LSTM

## What it is

Models designed for sequential data:
- text
- time series
- audio

## When to use it

When order matters.

## Advantages

- Good for sequences
- Capture temporal context

## Disadvantages

- More complex
- Often replaced by Transformers today

## Note

Typically implemented with **TensorFlow** or **PyTorch**, not scikit-learn.

---

# 15) Transformers

## What it is

Modern architecture for processing sequences.

It's the foundation of models like:
- GPT
- BERT
- T5

## When to use it

In:
- NLP
- translation
- summarization
- text generation
- modern computer vision as well

## Advantages

- Very powerful
- Better handling of long context
- State of the art on many problems

## Disadvantages

- Heavy
- Require many resources

## Note

Implemented with `transformers` (Hugging Face): `pip install transformers`

---

# Quick Summary by Category

## Supervised

- Linear Regression
- Logistic Regression
- Decision Tree
- Random Forest
- SVM
- KNN
- Naive Bayes
- Gradient Boosting
- XGBoost
- MLP

## Unsupervised

- K-Means
- Hierarchical Clustering
- PCA

## Sequential / Deep Learning

- RNN / LSTM
- Transformers

---

# Which Should You Learn First?

## Level 1 — Fundamentals

1. Linear Regression
2. Logistic Regression
3. Decision Tree
4. Random Forest
5. KNN

## Level 2 — More Powerful

6. SVM
7. Naive Bayes
8. K-Means
9. PCA
10. Gradient Boosting

## Level 3 — Modern

11. XGBoost
12. Neural Networks
13. LSTM
14. Transformers

---

# Practical Learning Path

### Week 1
- Linear Regression
- Logistic Regression

### Week 2
- Decision Tree
- Random Forest
- KNN

### Week 3
- SVM
- Naive Bayes
- K-Means

### Week 4
- PCA
- Gradient Boosting
- XGBoost

### Week 5
- MLP
- LSTM
- Transformers

---

# Important Advice

Don't just memorize names.

You should learn to answer these 4 questions for each algorithm:

1. Is it supervised or unsupervised?
2. Does it classify, predict, or cluster?
3. What are its advantages?
4. What type of problem is it best suited for?

When you master that, you begin to think like a true Machine Learning engineer.
