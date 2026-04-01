# MDL Exam Cheatsheet: Classification, Decision Trees, KNN, Ensemble Learning, Clustering & K-Means

---

## 1. CLASSIFICATION

### 1.1 Setup
- Input: x in R^d, where x = (x_1, x_2, ..., x_d)
- Labels: y in [k] = {1, 2, ..., k}
- If k = 2 => **Binary Classification**
- **Classifier**: f: X -> Y (maps input to label)
- **Scoring function**: h: X -> R

### 1.2 Confusion Matrix (MEMORIZE THIS LAYOUT)

|  | **Predicted P** | **Predicted N** |
|---|---|---|
| **Actual P** | True Positive (TP) | False Negative (FN) |
| **Actual N** | False Positive (FP) | True Negative (TN) |

> From your notes: Rows = True labels, Columns = Predicted labels

### 1.3 Metrics (ALL FORMULAS)

| Metric | Formula | What it answers |
|---|---|---|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Overall correctness |
| **Recall (TPR / Sensitivity)** | TP / (TP + FN) = TP / P | Of actual positives, how many found? |
| **Precision (PPV)** | TP / (TP + FP) | Of predicted positives, how many correct? |
| **F1 Score** | 2 / (1/Recall + 1/Precision) = 2PR/(P+R) | Harmonic mean of Precision & Recall |
| **FPR** | FP / (FP + TN) = FP / N | False alarm rate |
| **FNR** | FN / (FN + TP) = FN / P | Miss rate |
| **TNR (Specificity)** | TN / (TN + FP) = TN / N | Of actual negatives, how many found? |
| **TPR** | TP / (TP + FN) = TP / P | Same as Recall |

> **F1 = Harmonic Mean**: F1 = 2 / (1/Recall + 1/Precision)

> **EXAM TIP**: Accuracy is misleading for imbalanced datasets. A classifier that always predicts the majority class gets high accuracy but 0 recall on the minority class. Use F1 instead.

---

## 2. BAYES CLASSIFIER & NAIVE BAYES

### 2.1 Bayes Theorem
```
P(A|B) = P(B|A) * P(A) / P(B) = P(B|A) * P(A) / SUM_A [P(B|A) * P(A)]
```

### 2.2 Bayes Classifier

- **Prior**: P(Y = k) -- probability of class k before seeing data
- **Likelihood**: P(X = x | Y = k) -- probability of seeing features x given class k
- **Posterior**: P(Y = k | X = x) -- what we want
- **Evidence**: P(X = x) -- normalizing constant (same for all classes, **does not play a role in decision**)

```
P(Y=k | X=x) = P(X=x | Y=k) * P(Y=k) / P(X=x)
             = Likelihood * Prior / Evidence
```

**Optimal classifier** (minimizes error rate):
```
y_hat = argmax_k P(Y=k | X=x) = argmax_k P(X=x | Y=k) * P(Y=k)
```

### 2.3 The Problem: Curse of Dimensionality
- With d binary features: need to estimate **2^d distributions** per class
- With d = 20: that's 2^20 ~ 1 million parameters per class!
- **Impractical** to estimate from limited data

### 2.4 Naive Bayes: The Fix
**Key Assumption**: Features are **conditionally independent** given the class.

```
P(X=x | Y=k) = PRODUCT_{j=1}^{d} P(X_j = x_j | Y=k)
```

**Naive Bayes Classification Rule**:
```
y_hat = argmax_{i in [k]} P(Y=i) * PRODUCT_{j=1}^{d} P(X_j = x_j | Y=i)
```

- Reduces parameters from **2^d to 2d** per class (for binary features)
- The "naive" independence assumption is often violated but **it still works well in practice** because we only need the **ranking** of posteriors to be correct, not the exact values
- Especially good for **text classification** (spam filtering, sentiment analysis)

### 2.5 Generative vs Discriminative

| | **Generative** | **Discriminative** |
|---|---|---|
| Models | Joint P(X, Y) | Conditional P(Y given X) directly |
| Can generate data? | Yes | No |
| Examples | Naive Bayes, HMM, GMM | Logistic Regression, SVM, Decision Trees |

---

## 3. DECISION TREES

### 3.1 Structure
- **Internal nodes**: test a feature/attribute
- **Branches**: correspond to feature values
- **Leaf nodes**: assign class labels
- Interpretable: can trace path from root to leaf = explicit if-then rules

### 3.2 Entropy (Measures Uncertainty/Impurity)

```
H(S) = - SUM_{i=1}^{k} p_i * log2(p_i)
```

where p_i = proportion of class i in set S.

**Properties**:
- H(S) = 0 when all samples belong to one class (pure -- no uncertainty)
- H(S) = 1 for binary split with 50/50 (maximum uncertainty)
- Convention: 0 * log2(0) = 0 (since lim_{p->0} p*log(1/p) = 0)
- From your notes: 2 messages = 1 bit, 4 messages = 2 bits

**Quick calculation example**:
- 9 positive, 5 negative (total 14):
  H = -(9/14)*log2(9/14) - (5/14)*log2(5/14) = 0.940 bits

### 3.3 Information Gain (ID3 Splitting Criterion)

```
IG(S, A) = H(S) - SUM_{t in T} (|S_t| / |S|) * H(S_t)
```

where T = set of different values for attribute A, and S_t = subset of S where attribute A has value t.

**Algorithm**: At each node, pick the attribute with the **highest information gain**.
Sort attributes by descending order of IG.

### 3.4 ID3 Algorithm
```
BuildTree(S, Features):
    if all samples in S have same class c:
        return Leaf(c)
    if Features is empty:
        return Leaf(majority class in S)
    
    A* = feature with max IG(S, A)
    create node for A*
    for each value v of A*:
        S_v = {x in S | x.A* = v}
        if S_v is empty:
            add Leaf(majority class of S)
        else:
            add subtree BuildTree(S_v, Features - {A*})
```

### 3.5 CART (Classification and Regression Trees)
**Key difference from ID3**: CART produces **only 2 children** (binary splits).

**Gini Index** (splitting criterion for CART):
```
Gini(S) = 1 - SUM_{i=1}^{k} p_i^2 = SUM_i p_i * (1 - p_i)
```

> From your notes: Gini Index = 2 * SUM p_L * (1 - p_L)

- Gini = 0 for pure node; maximum for equal class distribution
- **No logarithm needed** -- computationally simpler than entropy
- In practice, Gini and entropy produce **similar trees**

### 3.6 Overfitting in Decision Trees
> From your notes: "Small change in data leads to different tree"

- Deep trees memorize training data (zero training error, poor test performance)
- **Pre-pruning**: Stop early (limit max depth, min samples per leaf, min IG threshold)
- **Post-pruning**: Grow full tree, then remove branches that don't improve validation performance
- **Fix**: Use **ensembles** (bagging / boosting) to stabilize

---

## 4. K-NEAREST NEIGHBORS (KNN)

### 4.1 Algorithm
Given training data D = {(x_1,y_1), (x_2,y_2), ..., (x_n,y_n)} and query point x:

1. Compute distance from x to every training point
2. Sort: |x_{sigma(1)} - x| <= |x_{sigma(2)} - x| <= ... <= |x_{sigma(n)} - x|
3. Find the K nearest neighbors
4. y_hat = **most frequently occurring label** among the K neighbors (majority vote)

> KNN is a **lazy learner**: no training phase, all computation at prediction time.

### 4.2 Distance Metrics

| Metric | Formula | Use for |
|---|---|---|
| **Euclidean** | sqrt(SUM (x_j - x'_j)^2) | Continuous features |
| **Manhattan** | SUM abs(x_j - x'_j) | Continuous, grid-like |
| **Hamming** | SUM 1[x_j != x'_j] | Discrete/categorical features |
| **Minkowski** | (SUM abs(x_j - x'_j)^p)^(1/p) | General (p=1: Manhattan, p=2: Euclidean) |

### 4.3 Properties of a Valid Distance Function
d: X x X -> R+

1. **Non-negativity**: d(x, y) >= 0
2. **Identity**: d(x, y) = 0 iff x = y  (also d(x,y) = d(y,x) -- symmetry)
3. **Triangle inequality**: d(x, y) + d(y, z) >= d(x, z)

### 4.4 Choosing K
- **Small K** (e.g., K=1): Low bias, high variance => overfitting, sensitive to noise
- **Large K**: High bias, low variance => underfitting, smoother boundaries
- Choose K via **cross-validation**
- From your notes' error vs K graph: error first decreases then increases as K grows

> **Key result from your notes**: As n -> infinity, 1-NN error rate is at most **2 times** Bayes Classifier error rate.

### 4.5 KNN Weaknesses
- **Curse of dimensionality**: In high dimensions, all points become equidistant
- **Feature scaling required**: Features with large ranges dominate distance (use Z-score: (x - mu) / sigma)
- **Slow prediction**: O(n * d) per query (scans entire dataset)

---

## 5. ENSEMBLE LEARNING (FROM YOUR NOTES)

> "Combining Classifiers" -- from your handwritten notes page 11/3

### 5.1 Core Idea
Instead of using one classifier, **combine multiple classifiers** to get better performance. Like asking multiple experts and combining their opinions.

### 5.2 Bagging (Bootstrap Aggregating)

**Key idea**: Train multiple classifiers on **different random subsets** of training data, combine by **majority vote**.

**Algorithm**:
1. From training set of size n, create B bootstrap samples (sample n points **with replacement**)
2. Train a separate classifier on each bootstrap sample
3. For a new point, each classifier votes => **majority vote** wins

**Why it works**:
- Each bootstrap sample is slightly different => classifiers make **different errors**
- Majority vote smooths out individual mistakes
- Reduces **VARIANCE** (great for high-variance models like deep decision trees)

**Classic example**: **Random Forest** = Bagging with Decision Trees (+ random feature subsets at each split)

**Properties**:
- Each model is trained **independently** (can parallelize)
- All models have **equal weight** in voting
- Best when base classifier has **high variance, low bias** (e.g., unpruned decision trees)

### 5.3 Boosting

**Key idea**: Train classifiers **sequentially**, each one focusing on the mistakes of the previous ones. Combine using **weighted accuracy** (not equal votes).

**Algorithm (AdaBoost)**:
1. Initialize: give all training points equal weight w_i = 1/n
2. For t = 1, 2, ..., T:
   - Train classifier h_t on the **weighted** training data
   - Compute weighted error: epsilon_t = SUM_{misclassified} w_i
   - Compute classifier weight: alpha_t = (1/2) * ln((1 - epsilon_t) / epsilon_t)
     - (better classifiers get higher alpha)
   - Update sample weights: **increase** weights of misclassified points, **decrease** weights of correct ones
   - Normalize weights to sum to 1
3. Final prediction: H(x) = sign(SUM_{t=1}^{T} alpha_t * h_t(x))

**Why it works**:
- Each new classifier focuses on the **hard examples** (previously misclassified)
- Weighted combination gives more influence to **better classifiers**
- Reduces **BIAS** (turns weak learners into a strong learner)

### 5.4 Bagging vs Boosting -- THE KEY TABLE

| | **Bagging** | **Boosting** |
|---|---|---|
| Training | **Independent** (parallel) | **Sequential** (each depends on previous) |
| Combination | **Majority vote** (equal weight) | **Weighted vote** (better classifiers = more say) |
| Reduces | **Variance** | **Bias** |
| Data sampling | Bootstrap (with replacement) | Reweight samples (focus on errors) |
| Overfitting | Resistant | Can overfit if too many rounds |
| Best for | High-variance models (deep trees) | Weak learners (stumps, shallow trees) |
| Example | Random Forest | AdaBoost, Gradient Boosting, XGBoost |

---

## 6. CLUSTERING

### 6.1 Setup
- **Unsupervised learning**: No labels, discover structure
- **Hard clustering** (this course): each point belongs to exactly one cluster
  - S_i INTERSECT S_j = empty for i != j
  - UNION S_i = {x_1, x_2, ..., x_n} (all points assigned)
- **Soft clustering**: points have probability of belonging to each cluster

### 6.2 Types of Clustering

#### Connectivity-Based (Hierarchical)

**Agglomerative (Bottom-Up)** -- also called **AGNES**
1. Start: each point is its own cluster (n clusters)
2. Find the two **closest** clusters
3. **Merge** them into one cluster
4. Repeat until desired number of clusters (or 1 cluster)
5. Result: a **dendrogram** (tree of merges) -- cut at desired level

- **Handles outliers** well
- Linkage types: Single (min distance), Complete (max distance), Average, Ward's (min variance)

**Divisive (Top-Down)** -- also called **DIANA**
1. Start: all points in one cluster
2. Find the **least cohesive** cluster
3. **Split** it into two clusters
4. Repeat until desired number of clusters

- **Outliers may disrupt** the splitting
- Computationally more expensive than agglomerative

#### Centroid-Based
- K-Means (see Section 7)
- Goal: **minimize variance** within clusters

### 6.3 All Clustering is NP-Hard
> From your notes: "But all of them are NP-Hard. Calculate Heuristically."

---

## 7. K-MEANS

### 7.1 Algorithm
```
1. Randomly select k points as centers (centroids)
2. Assign each point to the cluster of the closest center
3. Compute mean of all points in each cluster
4. Call these new means the new centers
5. Repeat steps 2-4 until convergence (centers stop moving)
```

### 7.2 Objective Function
```
J = min_{S1,...,Sk} SUM_{i=1}^{k} |S_i| * Var(S_i) 
  = min SUM_{i=1}^{k} SUM_{x in S_i} ||x - mu_i||^2
```

where mu_i = (1/|S_i|) * SUM_{x_j in S_i} x_j is the centroid of cluster i.

> Equivalent form from your notes: min SUM_{i=1}^{k} (1/|S_i|) SUM_{x,y in S_i} ||x_p - y_q||^2

- **Converges?** YES -- objective decreases monotonically at each step
- **Global optimum?** NO -- only finds a **local** minimum (NP-hard problem)
- **Fix**: Run multiple times with different random initializations, pick best

### 7.3 Choosing K: Three Methods

#### (i) Elbow Method
- Plot within-cluster sum of squares J vs K
- Look for the **"elbow"** -- the point where adding more clusters gives diminishing returns
- From your notes: the classic S-curve/elbow plot

#### (ii) Silhouette Score (PER POINT)
```
S(i) = (b(i) - a(i)) / max{a(i), b(i)}
```

where:
- a(i) = average distance from point i to **other points in same cluster** (intra-cluster)
- b(i) = average distance from point i to **points in nearest other cluster** (inter-cluster)

**Interpretation**:
- S(i) ~ +1: point is **well-clustered** (far from other clusters, close to own)
- S(i) ~ 0: point is **on the border** between clusters
- S(i) ~ -1: point is **misclassified** (closer to another cluster)

**Overall Silhouette Score** = SUM S(i) / n => Best K maximizes this, values close to 1.

> From your notes: S(i) UP => Better

#### (iii) Davies-Bouldin Index
```
DB = (1/k) * SUM_i max_{j != i} (sigma_i + sigma_j) / delta(c_i, c_j)
```

where:
- sigma_i = **intra-cluster** distance (avg distance of points in cluster i to its centroid)
- delta(c_i, c_j) = **inter-cluster** distance (distance between centroids i and j)

**Interpretation**: **Lower DB = Better** clustering (tight clusters that are far apart)

> **Minimize DB, Maximize Silhouette.**

---

## 8. QUICK-FIRE FORMULA REFERENCE

### Classification
```
Accuracy = (TP+TN) / (TP+TN+FP+FN)
Recall = TP / (TP+FN)
Precision = TP / (TP+FP)
F1 = 2TP / (2TP+FP+FN)
```

### Bayes / Naive Bayes
```
y_hat = argmax_k  P(Y=k) * PRODUCT_{j=1}^{d} P(X_j=x_j | Y=k)
```

### Entropy & Info Gain
```
H(S) = -SUM p_i * log2(p_i)
IG(S,A) = H(S) - SUM_t (|S_t|/|S|) * H(S_t)
```

### Gini (CART)
```
Gini(S) = 1 - SUM p_i^2
```

### Distance
```
Euclidean: sqrt(SUM (x_j - x'_j)^2)
Manhattan: SUM |x_j - x'_j|
Hamming: SUM 1[x_j != x'_j]
```

### K-Means
```
J = SUM_{i=1}^{k} SUM_{x in C_i} ||x - mu_i||^2
mu_i = (1/|C_i|) * SUM_{x in C_i} x
```

### Silhouette
```
S(i) = (b(i) - a(i)) / max(a(i), b(i))     range: [-1, +1]     higher = better
```

### Davies-Bouldin
```
DB = (1/k) * SUM_i max_{j!=i} (sigma_i + sigma_j) / delta(c_i, c_j)     lower = better
```

---

## 9. COMMON EXAM TRAPS & TIPS

1. **Accuracy vs F1**: Always mention F1 for imbalanced data. Accuracy is misleading.
2. **Naive Bayes "naive"**: The assumption is conditional independence OF FEATURES GIVEN CLASS, not absolute independence.
3. **Evidence in Bayes**: P(X=x) does NOT affect the argmax decision. You can ignore it.
4. **ID3 vs CART**: ID3 = multi-way splits + entropy. CART = binary splits + Gini.
5. **KNN needs scaling**: Always standardize features before KNN (Z-score).
6. **KNN is lazy**: No training! All work happens at prediction time.
7. **K-Means initialization matters**: Different starts => different results. Run multiple times.
8. **K-Means convergence**: Always converges, but to LOCAL minimum, not global.
9. **Silhouette**: Higher = better (maximize). Davies-Bouldin: Lower = better (minimize).
10. **Bagging reduces VARIANCE, Boosting reduces BIAS** -- this is the most tested distinction.
11. **Bagging = parallel + equal vote. Boosting = sequential + weighted vote.**
12. **1-NN result**: As n -> infinity, 1-NN error <= 2 * Bayes optimal error.
13. **Decision trees are unstable**: Small data changes => very different trees. Use ensembles to fix.
14. **Agglomerative = AGNES (bottom-up, handles outliers). Divisive = DIANA (top-down, outliers disrupt).**
15. **All clustering problems are NP-Hard** -- we solve heuristically.
16. **Curse of dimensionality**: affects both Naive Bayes (solved by independence assumption) and KNN (no good fix, all points equidistant).
