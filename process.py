import os
import re
import pandas as pd

# Folder containing downloaded HTML files
DOWNLOAD_DIR = "downloaded_files"

# List of keywords to search (lowercase)
KEYWORDS = [
    "artificial intelligence", "ai", "machine learning", "chatgpt", "openai",
    "language model", "generative ai", "deep learning", "neural network", "automation","Color","name"
]

def clean_text(html):
    """Remove HTML tags and convert to lowercase"""
    return re.sub(r"<.*?>", " ", html).lower()

def run_process(ticker):
    print(f"🔍 Processing files for ticker: {ticker}")
    results = []
    for filename in os.listdir(DOWNLOAD_DIR):
        if not filename.lower().startswith(ticker.lower()):
            continue

        filepath = os.path.join(DOWNLOAD_DIR, filename)
        
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
            text = html
            
            for kw in KEYWORDS:
                count = text.count(kw)
                results.append({
                    "file_name": filename,
                    "keyword": kw,
                    "count": count
                })

    # Save results to a CSV
    output_file = os.path.join(DOWNLOAD_DIR, f"{ticker}.csv")
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"✅ Saved: {output_file}")