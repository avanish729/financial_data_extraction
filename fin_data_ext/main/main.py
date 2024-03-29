import streamlit as st 
import pandas as pd
import openai_helper 
col1,col2=st.columns([3,2])
financial_data_df=pd.DataFrame({
    "Measure": ["Company Name", "Revenue", "EPS","Net Icome"],
        "Value": ["", "", "",""]
    
})

with col1:
    st.title("Data Extraction Tool ")
    news_article=st.text_area("paste your financial news article here ",height=300)
    if st.button("extract"):
        financial_data_df=openai_helper.extract_financial_data(news_article)

with col2:
    st.markdown("<br/>" * 5, unsafe_allow_html=True)  # Creates 5 lines of vertical space
    st.dataframe(financial_data_df,
    column_config={
        "Measure":st.column_config.Column(width=150),
        "Value":st.column_config.Column(width=150)
    },hide_index=True)