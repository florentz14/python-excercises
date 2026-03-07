# 21 - Machine Learning

Comprehensive Python exercises covering fundamental Machine Learning concepts using **NumPy**, **SciPy**, **scikit-learn**, and **Matplotlib**.

## Resources

| Resource | Description |
|----------|-------------|
| [`00_ml_algorithms_guide.md`](00_ml_algorithms_guide.md) | Complete guide: what each algorithm is, when to use it, pros/cons, Python examples |
| [`comparative_table.md`](comparative_table.md) | Comparative table of the 15 algorithms (files 24-38) |

## Prerequisites

```bash
pip install numpy scipy scikit-learn matplotlib pandas
# For XGBoost (file 35):
pip install xgboost
```

## Files (43 programs)

| #  | File | Topic |
|----|------|-------|
| 01 | `01_getting_started.py` | ML introduction, workflow, data types, library check |
| 02 | `02_mean_median_mode.py` | Mean, median, mode, weighted mean, skewed data |
| 03 | `03_standard_deviation.py` | Std dev, variance, 68-95-99.7 rule, population vs sample |
| 04 | `04_percentile.py` | Percentiles, quartiles, IQR, outlier detection |
| 05 | `05_data_distribution.py` | Uniform, normal, skewed distributions, histograms |
| 06 | `06_normal_data_distribution.py` | Bell curve, Z-score, normality testing, Shapiro-Wilk |
| 07 | `07_scatter_plot.py` | Scatter plots, correlation, trend lines, color maps |
| 08 | `08_linear_regression.py` | Linear regression, R², prediction, residuals |
| 09 | `09_polynomial_regression.py` | Polynomial fitting, overfitting, degree comparison |
| 10 | `10_multiple_regression.py` | Multiple features, feature importance, evaluation |
| 11 | `11_scale.py` | StandardScaler, MinMaxScaler, RobustScaler, impact on models |
| 12 | `12_train_test.py` | Train/test split, stratified split, overfitting detection |
| 13 | `13_decision_tree.py` | Classification & regression trees, feature importance, visualization |
| 14 | `14_confusion_matrix.py` | TP/TN/FP/FN, precision, recall, F1, multi-class |
| 15 | `15_hierarchical_clustering.py` | Dendrograms, agglomerative clustering, linkage methods |
| 16 | `16_logistic_regression.py` | Sigmoid, binary/multi-class, decision boundary, regularization |
| 17 | `17_grid_search.py` | GridSearchCV, RandomizedSearchCV, hyperparameter tuning |
| 18 | `18_categorical_data.py` | Label encoding, one-hot encoding, ordinal encoding, pipelines |
| 19 | `19_kmeans.py` | K-Means clustering, elbow method, silhouette score |
| 20 | `20_bootstrap_aggregation.py` | Bagging, Random Forest, OOB score, ensemble methods |
| 21 | `21_cross_validation.py` | K-Fold, stratified, LOO, time series CV, model comparison |
| 22 | `22_auc_roc_curve.py` | ROC curve, AUC, precision-recall, threshold analysis |
| 23 | `23_knn.py` | K-Nearest Neighbors, optimal K, distance metrics, weighted KNN |
| 24 | `24_linear_regression.py` | Linear Regression (scikit-learn reference) |
| 25 | `25_logistic_regression.py` | Logistic Regression (scikit-learn reference) |
| 26 | `26_decision_tree.py` | Decision Tree (scikit-learn reference) |
| 27 | `27_random_forest.py` | Random Forest (scikit-learn reference) |
| 28 | `28_svm.py` | Support Vector Machine (scikit-learn reference) |
| 29 | `29_knn.py` | K-Nearest Neighbors (scikit-learn reference) |
| 30 | `30_naive_bayes.py` | Naive Bayes (scikit-learn reference) |
| 31 | `31_kmeans.py` | K-Means (scikit-learn reference) |
| 32 | `32_hierarchical_clustering.py` | Hierarchical Clustering (scikit-learn reference) |
| 33 | `33_pca.py` | PCA (scikit-learn reference) |
| 34 | `34_gradient_boosting.py` | Gradient Boosting (scikit-learn reference) |
| 35 | `35_xgboost.py` | XGBoost (scikit-learn reference) |
| 36 | `36_mlp_neural_network.py` | MLP Neural Network (scikit-learn reference) |
| 37 | `37_rnn_lstm_conceptual.py` | RNN/LSTM conceptual (TensorFlow/PyTorch) |
| 38 | `38_transformers_conceptual.py` | Transformers conceptual (Hugging Face) |
| 39 | `39_load_explore.py` | Load CSV, explore with pandas (Iris, Students) |
| 40 | `40_student_regression.py` | Predict math grade - regression (StudentsPerformance) |
| 41 | `41_iris_classification.py` | Classify flower species (Iris) |
| 42 | `42_wine_clustering.py` | Cluster wines without labels (Wine Quality) |
| 43 | `43_complete_pipeline.py` | Full pipeline: preprocess → train → evaluate |

## Topics Covered

### Statistics Fundamentals (01-06)
- Central tendency (mean, median, mode)
- Dispersion (standard deviation, variance)
- Percentiles, quartiles, IQR
- Data distributions (normal, uniform, skewed)

### Regression (07-10)
- Scatter plots and correlation
- Linear, polynomial, and multiple regression
- R² score, RMSE, residual analysis

### Preprocessing (11, 18)
- Feature scaling (standardization, normalization)
- Categorical encoding (label, one-hot, ordinal)

### Model Evaluation (12, 14, 21, 22)
- Train/test split and cross-validation
- Confusion matrix and classification metrics
- ROC-AUC curves and precision-recall

### Classification Algorithms (13, 16, 23, 25, 26, 27, 28, 29, 30, 34, 35, 36)
- Decision Trees, Logistic Regression, KNN, Naive Bayes
- Random Forest, SVM, Gradient Boosting, XGBoost, MLP

### Clustering (15, 19, 31, 32)
- K-Means clustering
- Hierarchical clustering

### Dimensionality Reduction (33)
- PCA

### Deep Learning / Sequential (37, 38)
- RNN/LSTM conceptual
- Transformers conceptual

### Advanced Techniques (17, 20)
- Hyperparameter tuning (Grid Search)
- Ensemble methods (Bootstrap Aggregation, Random Forest)

### Practical Course with Real Data (39-43)
- Load and explore datasets (Iris, Students, Wine)
- Regression, classification, clustering on real CSV data
- Complete ML pipeline
