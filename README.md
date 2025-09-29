# 🌊 Hydrostatic Pressure Prediction with CatBoost

This project predicts **hydrostatic pressure** in marine environments using **machine learning pipelines** with **CatBoost Regressor** and **Optuna hyperparameter tuning**.

---

## 📂 Dataset

* **train.csv** → Training data with target `hydrostatic_pressure`.
* **test.csv** → Testing data for final predictions.

### Key Features:

* `oxygen_saturation_50m`
* `perceived_water_density`
* `sediment_deposition`
* `dissolved_gas_pressure`
* `current_turbulence`
* `sediment_porosity_*` (4 layers: 0–10cm, 10–30cm, 30–100cm, 100–250cm)
* `perpendicular_light_intensity`
* `thermal_emissions`
* `depth_reading_time` (datetime → extracted into year, month, day, hour)
* **Target**: `hydrostatic_pressure` (continuous)

---

## 🛠️ Workflow

### 1. Exploratory Data Analysis (EDA)

* Shape, datatypes, null values, duplicates.
* Distribution analysis (histograms, boxplots).
* Outlier detection.
* Correlation heatmaps.

### 2. Preprocessing with Pipelines

* **Custom Transformer** → `InitialFeatureEngineer`

  * Convert numeric strings with commas → floats.
  * Extract year, month, day, hour from datetime.
* **Imputation** → Missing values filled with mean.
* **Scaling** → StandardScaler for numerical features.

### 3. Modelling

* Model: **CatBoost Regressor**
* Optimized with **Optuna** (Tree-structured Parzen Estimator).
* Objective: Maximize **R² Score**.

### 4. Hyperparameter Tuning

Parameters tuned:

* `learning_rate`
* `depth`
* `l2_leaf_reg`
* `subsample`

Optuna ran multiple trials to find the best config.

### 5. Final Model Training

* Trained on full processed training data.
* Saved using `joblib` → `catboost_model_final.pkl`.

### 6. Evaluation

* Metrics: **R² score**.
* Plots:

  * **Actual vs Predicted** (regression plot).
  * **Residuals plot** (error analysis).

---

## 📊 Results

* **Best R² (validation set): ~0.xx**
* Visuals showed good alignment between predictions and actual values.
* Residuals mostly centered around 0 (low bias).

---

## 🚀 Usage

### Train + Save Model

```bash
python train.py
```

### Load Model & Predict

```python
import joblib
import pandas as pd

# Load model
model = joblib.load("catboost_model_final.pkl")

# Predict on new test data
preds = model.predict(X_test_final)
print(preds[:5])
```

---

## 📌 Future Improvements

* Try **XGBoost** and **LightGBM** for comparison.
* Add feature selection or PCA.
* Deploy as an API (FastAPI) or web app (Streamlit).

---

## 📑 Citation

If you use this project, please cite:
**Gervasius Russell (2025), BINUS University – Hydrostatic Pressure Prediction with CatBoost**

---
