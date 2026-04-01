# =========================
# frontend/dashboard_ready.py
# =========================
import streamlit as st
from backend.app.services.advanced_service import analyze_advanced

st.title(" Financial Sentiment AI Dashboard ")

text = st.text_area("Enter financial text:")

if st.button("Analyze"):
    if text:
        with st.spinner("Analyzing..."):
            result = analyze_advanced(text)
        
        st.success("Analysis Complete!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Sentiment", result['sentiment'])
        with col2:
            st.metric("Confidence", f"{result['confidence']:.2f}")
        
        st.subheader("Explanation")
        st.write(result['explanation'])
        
        st.subheader("Context")
        for ctx in result['context']:
            st.info(ctx)
    else:
        st.warning("Please enter some text to analyze.")
