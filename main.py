import streamlit as st
import pandas as pd
import numpy as np
import io
import zipfile

from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score, 
    confusion_matrix, classification_report,
    mean_absolute_percentage_error
)

import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# =============================
# 🌌 UI CONFIG
# =============================
st.set_page_config(page_title="EvalMetrics Pro", layout="wide", page_icon="📊")

st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: radial-gradient(circle at center, #0a1118 0%, #05080c 100%);
    color: #e0f7fa;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: rgba(10, 17, 24, 0.95) !important;
    border-right: 2px solid #00c6ff;
    box-shadow: 0 0 25px rgba(0, 198, 255, 0.4);
}

/* CARDS */
div[data-testid="stExpander"], 
.stMetric, 
div.element-container {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(0, 198, 255, 0.4) !important;
    border-radius: 18px !important;
    padding: 20px !important;
    margin-bottom: 20px !important;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 15px rgba(0, 198, 255, 0.2);
}

/* HOVER */
div.element-container:hover {
    transform: scale(1.02);
    box-shadow: 0 0 30px rgba(0, 198, 255, 0.6);
}

/* BUTTON */
div.stButton > button {
    background: transparent;
    color: #00c6ff;
    border: 2px solid #00c6ff;
    padding: 15px 50px;
    border-radius: 50px;
    font-weight: bold;
    letter-spacing: 2px;
}

div.stButton > button:hover {
    background: #00c6ff;
    color: #0a1118;
    box-shadow: 0 0 40px #00c6ff;
}

/* TITLE */
h1 {
    text-align: center;
    color: #00c6ff;
    text-shadow: 0 0 20px #00c6ff;
}

</style>
""", unsafe_allow_html=True)

st.title("📊 EvalMetrics Pro")

# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.header("⚙️ Configuration")
    task = st.radio("Select Task Type", ["Regression", "Classification"])
    true_file = st.file_uploader("Upload True Values CSV", type=['csv'])
    pred_file = st.file_uploader("Upload Predictions CSV", type=['csv'])

if true_file and pred_file:
    if st.button("🚀 Run Evaluation"):
        st.session_state.run = True
else:
    st.warning("👈 Upload both files")

# =============================
# MAIN LOGIC
# =============================
if 'run' in st.session_state and true_file and pred_file:

    df_true = pd.read_csv(true_file).iloc[:, 0]
    df_pred = pd.read_csv(pred_file).iloc[:, 0]

    # =============================
    # REGRESSION
    # =============================
    if task == "Regression":

        mae = mean_absolute_error(df_true, df_pred)
        mse = mean_squared_error(df_true, df_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(df_true, df_pred)

        n, p = len(df_true), 1
        adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

        mape = mean_absolute_percentage_error(df_true, df_pred)

        st.subheader("📊 Metrics")

        c1, c2, c3 = st.columns(3)
        c1.metric("MAE", f"{mae:.4f}")
        c2.metric("MSE", f"{mse:.4f}")
        c3.metric("RMSE", f"{rmse:.4f}")

        c4, c5, c6 = st.columns(3)
        c4.metric("R²", f"{r2:.4f}")
        c5.metric("Adj R²", f"{adj_r2:.4f}")
        c6.metric("MAPE", f"{mape*100:.2f}%")

        # Graphs
        g1, g2 = st.columns(2)

        with g1:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df_true, y=df_pred, mode='markers'))
            fig.update_layout(title="Actual vs Predicted")
            st.plotly_chart(fig, use_container_width=True)

        with g2:
            residuals = df_true - df_pred
            fig_res = px.histogram(residuals, nbins=30)
            fig_res.update_layout(title="Residual Distribution")
            st.plotly_chart(fig_res, use_container_width=True)

        # =============================
        # DOWNLOAD
        # =============================
        metrics_df = pd.DataFrame({
            "Metric": ["MAE","MSE","RMSE","R2","Adj_R2","MAPE"],
            "Value": [mae,mse,rmse,r2,adj_r2,mape]
        })

        output_df = pd.DataFrame({
            "y_true": df_true,
            "y_pred": df_pred,
            "residual": residuals
        })

        img1 = fig.to_image(format="png")
        img2 = fig_res.to_image(format="png")

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("metrics.csv", metrics_df.to_csv(index=False))
            zf.writestr("predictions.csv", output_df.to_csv(index=False))
            zf.writestr("scatter.png", img1)
            zf.writestr("residual.png", img2)

        zip_buffer.seek(0)

        st.download_button(
            "📦 Download Full Report",
            data=zip_buffer,
            file_name="regression_report.zip"
        )

        # =============================
        # FORMULAS
        # =============================
        # --- DEFINITIONS & FORMULAS (ENGLISH) ---
        
        st.markdown("---")
        st.subheader("📖 Metric Definitions & Formulas")
        st.markdown("""
        * **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted values.
        $$MAE = \\frac{1}{n} \\sum_{i=1}^{n} |y_i - \\hat{y}_i|$$

        * **MSE (Mean Squared Error):** Calculates the average of squared differences between actual and predicted values, giving higher weight to larger errors.
        $$MSE = \\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2$$

        * **RMSE (Root Mean Squared Error):** The square root of MSE, which brings the error back to the original unit of the target variable.
        $$RMSE = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2}$$

        * **R² Score (Coefficient of Determination):** Indicates how well the model explains the variance in the data. Ranges from 0 to 1, where 1 represents a perfect fit.
        $$R^2 = 1 - \\frac{\\sum (y_i - \\hat{y}_i)^2}{\\sum (y_i - \\bar{y})^2}$$

        * **Adjusted R²:** A modified version of R² that adjusts for the number of predictors in the model, preventing overestimation.
        $$Adjusted R^2 = 1 - \\left[ \\frac{(1-R^2)(n-1)}{n-k-1} \\right]$$

        * **MAPE (Mean Absolute Percentage Error):** Measures prediction error as a percentage, making it easy to interpret.
        $$MAPE = \\frac{100\\%}{n} \\sum_{i=1}^{n} \\left| \\frac{y_i - \\hat{y}_i}{y_i} \\right|$$
        """)

    # =============================
    # CLASSIFICATION
    # =============================
    else:

        report_df = pd.DataFrame(
            classification_report(df_true, df_pred, output_dict=True)
        ).transpose()

        st.dataframe(report_df)

        cm = confusion_matrix(df_true, df_pred)

        fig_cm = ff.create_annotated_heatmap(z=cm)
        st.plotly_chart(fig_cm, use_container_width=True)

        img_cm = fig_cm.to_image(format="png")

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("classification_report.csv", report_df.to_csv())
            zf.writestr("confusion_matrix.png", img_cm)

        zip_buffer.seek(0)

        st.download_button(
            "📦 Download Report",
            data=zip_buffer,
            file_name="classification_report.zip"
        )