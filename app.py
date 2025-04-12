# app.py

import streamlit as st
from datetime import date
from downloader import download_sec_filings # <-- Import from downloader.py
from process import run_process
from graph import show_keyword_graph

def main():
    st.title("SEC Filings Downloader")

    # Streamlit input fields
    ticker = st.text_input("Ticker Symbol (e.g., AAPL)", "AAPL")
    user_name = st.text_input("Name", "")
    start_date = st.date_input("Start Date", date(2021, 1, 1))
    end_date = st.date_input("End Date", date.today())
    filing_type = st.text_input("Filing Type (e.g., 10-K, 10-Q, 8-K)", "10-K")

    # Button triggers the Selenium download logic
    if st.button("Download Filings"):
        # Convert date objects to string (if you plan to do date-based filtering)
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")

        st.write(f"Downloading {filing_type} filings for {ticker} "
                 f"from {start_date_str} to {end_date_str}...")

        # Call the Selenium function from downloader.py
        download_sec_filings(ticker, start_date_str, end_date_str, filing_type)

        st.success("Download complete! Check your folder for the downloaded files.")

    if st.button("Run Post-Processing"):
        st.write("Running processing...")
        run_process(ticker)
        st.success("Processing complete!")
    if st.button("Show Keyword Graph"):
        st.write(f"Generating graph for {ticker}...")
        show_keyword_graph(ticker)

if __name__ == "__main__":
    main()
