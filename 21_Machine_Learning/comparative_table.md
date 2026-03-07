# Tabla comparativa: 15 algoritmos de Machine Learning

**Author:** Florentino Báez

---

| # | Algoritmo | Tipo | Tarea | Interpretable | Velocidad | Datos necesarios |
|---|-----------|------|------|--------------|-----------|------------------|
| 1 | Linear Regression | Supervisado | Regresión | ✅ Alta | ⚡ Rápido | Pocos |
| 2 | Logistic Regression | Supervisado | Clasificación | ✅ Alta | ⚡ Rápido | Pocos |
| 3 | Decision Tree | Supervisado | Clasif./Regr. | ✅ Muy alta | ⚡ Rápido | Pocos |
| 4 | Random Forest | Supervisado | Clasif./Regr. | ⚠️ Media | 🐢 Medio | Moderados |
| 5 | SVM | Supervisado | Clasificación | ❌ Baja | 🐢 Medio | Pequeños-medianos |
| 6 | KNN | Supervisado | Clasif./Regr. | ⚠️ Media | 🐢 Lento (inference) | Pequeños |
| 7 | Naive Bayes | Supervisado | Clasificación | ✅ Alta | ⚡ Muy rápido | Pocos |
| 8 | K-Means | No supervisado | Clustering | ⚠️ Media | ⚡ Rápido | Moderados |
| 9 | Hierarchical Clustering | No supervisado | Clustering | ✅ Alta (dendrograma) | 🐢 Lento | Pequeños |
| 10 | PCA | No supervisado | Reducción dim. | ⚠️ Media | ⚡ Rápido | Cualquiera |
| 11 | Gradient Boosting | Supervisado | Clasif./Regr. | ❌ Baja | 🐢 Medio | Moderados |
| 12 | XGBoost | Supervisado | Clasif./Regr. | ❌ Baja | ⚡ Rápido (optimizado) | Moderados-grandes |
| 13 | MLP (Neural Network) | Supervisado | Clasif./Regr. | ❌ Baja | 🐢 Medio | Muchos |
| 14 | RNN / LSTM | Supervisado | Secuencias | ❌ Baja | 🐢 Lento | Muchos |
| 15 | Transformers | Supervisado | Secuencias/NLP | ❌ Baja | 🐢 Muy lento | Muchísimos |

---

## Por tipo de problema

| Problema | Algoritmos recomendados |
|----------|-------------------------|
| **Regresión simple** | Linear Regression |
| **Clasificación binaria** | Logistic Regression, SVM, Naive Bayes |
| **Clasificación multiclase** | Random Forest, XGBoost, Gradient Boosting |
| **Clustering sin etiquetas** | K-Means, Hierarchical Clustering |
| **Reducir dimensiones** | PCA |
| **Máxima precisión tabular** | XGBoost, Gradient Boosting, Random Forest |
| **Texto / NLP** | Naive Bayes (básico), Transformers (avanzado) |
| **Series temporales** | LSTM, Transformers |
| **Baseline rápido** | Logistic Regression, KNN |

---

## Dependencias por algoritmo

| Algoritmo | Librería |
|-----------|----------|
| 1-11, 13 | scikit-learn |
| 12 | xgboost |
| 14 | TensorFlow o PyTorch |
| 15 | transformers (Hugging Face) |
