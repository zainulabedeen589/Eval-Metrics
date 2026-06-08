# 📊 EvalMetrics Pro — Advanced ML Model Evaluation Dashboard

**EvalMetrics Pro** ek powerful, intuitive aur aesthetic web application hai jise Machine Learning models (Regression aur Classification) ke absolute quantitative evaluation ke liye design kiya gaya hai. Is platform ko Python aur **Streamlit** ka use karke build kiya gaya hai, jisme custom premium **Glassmorphism UI Engine** inject kiya gaya hai taaki standard metric values ko ek modern analytics framework me dekha ja sake.

Aapko sirf ground-truth targets (`actual_values.csv`) aur model predictions (`predicted_values.csv`) upload karni hain, aur yeh application real-time me statistical calculations aur interactive visualizations generate karke unhe ek single download-ready `.zip` report bundle me export kar deti hai.

---

## 🎯 Key Capabilities & Features

- **Dual Mode Analytics Suite:** Single dashboard ke andar **Regression** aur **Classification** tasks ke evaluation frameworks ko seamlessly handle karta hai.
- **Dynamic Metrics Engine:**
  - **Regression Metrics:** Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Coefficient of Determination ($R^2$), Adjusted $R^2$, aur Mean Absolute Percentage Error (MAPE).
  - **Classification Metrics:** Precision, Recall, F1-Score, Support ke sath detailed Classification Report aur complete Confusion Matrix analysis.
- **Interactive High-Fidelity Charts (Plotly Engine):**
  - **Regression:** Actual vs Predicted Scatter Plots (with optimal fit lines) aur Residuals Distribution Histograms (error variance track karne ke liye).
  - **Classification:** Fully Annotated Confusion Matrix Heatmaps aur dynamic metric parameters ke multi-axis bar charts.
- **In-Memory Report Archiver (ZIP Bundler):** `io.BytesIO` aur `zipfile` modules ka use karke saari analytical calculations (`.csv` tables) aur generated high-resolution figures (`.png` graphs) ko real-time ek clickable `.zip` bundle me compile kiya jata hai.
- **Premium Glassmorphism Look:** Dark theme background matrix configuration, sleek neon glowing borders (`#00c6ff`), background blur filters (`backdrop-filter`), aur smooth responsive alignment matrices.

---

## 🛠️ Tech Stack & Ecosystem

| Component                     | Technology                     | Purpose                                                                     |
| :---------------------------- | :----------------------------- | :-------------------------------------------------------------------------- |
| **Frontend Framework**  | Streamlit                      | UI Rendering, Reactive components layout control, and State Management.     |
| **Data Processing**     | Pandas & NumPy                 | High-speed data manipulation, matrix operations, and shape synchronization. |
| **ML Metrics Backend**  | Scikit-Learn                   | Core computation engine for standard statistical values and matrices.       |
| **Visualization Layer** | Plotly Express & Graph Objects | Dynamic standalone vector layouts and rendering interactive charts.         |

---

## 📂 Project Structure & File Layout

```text
Eval-Metrics/
├── main.py                  # Main Python code container (UI configurations, mathematical pipelines, CSS)
├── requirements.txt         # Production library dependencies pinning system
├── actual_values.csv        # Baseline standard true target values dataset
├── predicted_values.csv     # Machine Learning model validation output prediction dataset
└── README.md                # Comprehensive project documentation manual
```

---

## ****👨‍💻 Author****

## **Zainul Abedeen**

Mail:- zainulpasha589@gmail.com

GitHub: [https://github.com/zainulabedeen589](https://github.com/zainulabedeen589)

LinkedIn: [https://linkedin.com/in/zainulabedeen589](https://linkedin.com/in/zainulabedeen589)


---
