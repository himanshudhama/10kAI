# graph.py

import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def show_keyword_graph(ticker):
    csv_path = os.path.join("downloaded_files", f"{ticker}.csv")

    if not os.path.exists(csv_path):
        st.error(f"No CSV found for ticker: {ticker}")
        return

    # Load the CSV
    df = pd.read_csv(csv_path)

    # Group by keyword and sum the counts across all files
    keyword_counts = df.groupby("keyword")["count"].sum().sort_values(ascending=False)

    # Plot using Matplotlib
    st.subheader(f"📊 Keyword Frequency for {ticker}")
    plt.figure(figsize=(10, 5))
    keyword_counts.plot(kind="bar")
    plt.ylabel("Count")
    plt.xlabel("Keyword")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)
