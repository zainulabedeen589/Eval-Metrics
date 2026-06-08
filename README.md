# 📊 EvalMetrics Pro — Advanced ML Model Evaluation Dashboard

## 🌐 **Live Application:-**[https://evalmetrics.streamlit.app/](https://evalmetrics.streamlit.app/)

## 🚀 Overview

**EvalMetrics Pro** is a powerful, intuitive, and aesthetically designed web application built for comprehensive Machine Learning model evaluation. It supports both **Regression** and **Classification** tasks, enabling users to perform accurate quantitative performance analysis through an interactive and modern analytics dashboard.

Developed using **Python** and  **Streamlit** , the platform incorporates a premium **Glassmorphism UI Engine** that transforms traditional model evaluation metrics into a visually engaging and professional analytical experience.

Users simply upload the ground-truth target values (`actual_values.csv`) and model predictions (`predicted_values.csv`), and the application automatically generates real-time metrics, interactive visualizations, and downloadable reports bundled into a single ZIP archive.

---

# 🎯 Key Features

## 🔄 Dual Analytics Framework

Evaluate both:

* **Regression Models**
* **Classification Models**

within a unified dashboard experience.

---

## 📈 Advanced Regression Metrics

The platform automatically computes:

* Mean Absolute Error ( **MAE** )
* Mean Squared Error ( **MSE** )
* Root Mean Squared Error ( **RMSE** )
* Coefficient of Determination ( **R² Score** )
* Adjusted R² Score
* Mean Absolute Percentage Error ( **MAPE** )

---

## 📊 Comprehensive Classification Metrics

Generate detailed classification analysis including:

* Precision
* Recall
* F1-Score
* Support
* Classification Report
* Confusion Matrix Analysis

---

## 🎨 Interactive Visualization Suite

### Regression Visualizations

* Actual vs Predicted Scatter Plot
* Best-Fit Trend Line Analysis
* Residual Error Distribution Histogram

### Classification Visualizations

* Annotated Confusion Matrix Heatmap
* Interactive Performance Metric Bar Charts

Built using the powerful **Plotly Visualization Engine** for high-quality and responsive analytics.

---

## 📦 Automated ZIP Report Generation

The application automatically compiles:

* Evaluation Metrics (.csv)
* Classification Reports (.csv)
* Generated Charts (.png)
* Analytical Outputs

into a downloadable ZIP archive using:

* `io.BytesIO`
* `zipfile`

for efficient in-memory report generation.

---

## ✨ Premium Glassmorphism User Interface

The dashboard includes a modern design system featuring:

* Dark Themed Analytics Workspace
* Glassmorphism Cards
* Neon Accent Highlights (`#00c6ff`)
* Backdrop Blur Effects
* Responsive Layout Components
* Smooth Interactive User Experience

---

# 🛠️ Technology Stack

| Component           | Technology                           | Purpose                                                |
| ------------------- | ------------------------------------ | ------------------------------------------------------ |
| Frontend Framework  | Streamlit                            | UI Rendering, State Management, Interactive Components |
| Data Processing     | Pandas, NumPy                        | Data Cleaning, Transformation, Numerical Computation   |
| ML Metrics Engine   | Scikit-Learn                         | Statistical Evaluation and Performance Metrics         |
| Visualization Layer | Plotly Express, Plotly Graph Objects | Interactive Data Visualization                         |
| Report Generation   | io, zipfile                          | Dynamic ZIP Archive Creation                           |

---

# 📂 Project Structure

```text
Eval-Metrics/
│
├── main.py
│   └── Main application file containing UI, analytics pipeline, visualizations, and CSS styling
│
├── requirements.txt
│   └── Project dependencies and package requirements
│
├── actual_values.csv
│   └── Ground truth target values
│
├── predicted_values.csv
│   └── Model prediction outputs
│
└── README.md
    └── Project documentation
```

---

# ⚙️ How to Use

### Step 1: Upload Files

Upload:

* `actual_values.csv`
* `predicted_values.csv`

through the dashboard interface.

### Step 2: Select Evaluation Type

Choose:

* Regression
* Classification

depending on your machine learning problem.

### Step 3: Analyze Results

Instantly view:

* Performance Metrics
* Interactive Charts
* Statistical Insights

### Step 4: Download Reports

Export all generated analytics and visualizations as a ZIP report package.

---

# 🎯 Use Cases

This platform is ideal for:

* Machine Learning Engineers
* Data Scientists
* MLOps Engineers
* AI Researchers
* Students & Educators
* Model Validation Teams

---

# 🔮 Future Enhancements

Planned features include:

* Multi-Class ROC Curve Analysis
* Precision-Recall Curve Visualization
* Cross-Validation Performance Dashboard
* Model Comparison Framework
* Experiment Tracking Integration
* Automated PDF Report Generation
* Explainable AI (XAI) Metrics Support

---

# 👨‍💻 Author

## Zainul Abedeen

📧 Email: [zainulpasha589@gmail.com](mailto:zainulpasha589@gmail.com)

🐙 GitHub: [https://github.com/zainulabedeen589](https://github.com/zainulabedeen589)

💼 LinkedIn: [https://linkedin.com/in/zainulabedeen589](https://linkedin.com/in/zainulabedeen589)

---

## ⭐ Support

If you found this project useful, consider giving it a **Star ⭐** on GitHub and sharing it with the community.

---

**Built with ❤️ using Python, Streamlit, Plotly, and Scikit-Learn**
