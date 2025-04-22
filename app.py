import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Cybersecurity Threat Predictor", layout="centered")

st.title("🔐 Cybersecurity Threat Prediction Dashboard")
st.markdown("🔍 Upload your network traffic data")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.subheader("📄 Uploaded Data Preview:")
    st.dataframe(df.head())

    try:
        model = joblib.load("threat_model.pkl")
        predictions = model.predict(df)
        df["Prediction"] = predictions
        df["Prediction Label"] = df["Prediction"].apply(lambda x: "Safe" if x == 0 else "Unsafe")

        st.subheader("📊 Prediction Summary")
        safe_count = df["Prediction Label"].value_counts().get("Safe", 0)
        unsafe_count = df["Prediction Label"].value_counts().get("Unsafe", 0)

        col1, col2 = st.columns(2)
        col1.metric("✅ Safe Connections", safe_count)
        col2.metric("⚠️ Unsafe Connections", unsafe_count)

        st.subheader("🔐 Detailed Prediction Results")

        # Highlight unsafe connections
        def highlight_unsafe(row):
            return ["background-color: #ffcccc" if row["Prediction Label"] == "Unsafe" else "" for _ in row]

        styled_df = df.style.apply(highlight_unsafe, axis=1)
        st.dataframe(styled_df)

        # Download CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
