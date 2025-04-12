# downloader.py

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from unidecode import unidecode

def download_sec_filings(ticker, start_date_str, end_date_str, filing_type):
    """
    Use Selenium to download specified filings for the given ticker
    from the SEC EDGAR site (basic example).
    """

    # 1) Configure ChromeDriver options (optional: run headless)
    chrome_options = Options()
    # Uncomment to run headless (no visible browser window):
    # chrome_options.add_argument("--headless")

    # Replace with webdriver.Firefox(), etc. if you prefer another browser
    #driver = webdriver.Chrome(options=chrome_options,executable_path ='E:\tools\chromedriver')
    #driver = webdriver.Chrome(options=chrome_options, service=ChromeDriverManager().install())
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # 2) Build basic EDGAR URL (this example omits date range in the query)
    url ="https://www.sec.gov/edgar/search/#/dateRange=custom&category=custom&entityName="+ticker+"&startdt="+start_date_str+"&enddt="+end_date_str+"&forms="+filing_type
    driver.get(url)
    time.sleep(2)  # give the page time to load

    # 3) Find table rows for each filing row (often 'blueRow' or 'grayRow')
    rows = driver.find_elements(By.XPATH, ".//a[@data-file-name]")
    all_links=[]
    for index, row in enumerate(rows):
        # Each row typically has a second <td> with a link to "Documents"
        #try:
        all_links+=[row.get_attribute("href")]

    print(all_links)
    for index,doc_link in enumerate(all_links):
        print(doc_link)
        driver.get(doc_link)
        time.sleep(5)
        print("downloaded_files\\"+ticker+filing_type+str(index))
        #import  pdb;pdb.set_trace()
        open("downloaded_files\\"+ticker+filing_type+str(index)+".html" , 'w').write(unidecode(driver.page_source))
        print("downloaded 213")
        for i in range(10):
            print(i)
        #except:
         #   continue  # skip if not found

        # Click to open the filing details page
        

        # 4) On the detail page, the primary .html doc often in row 2 of the main table
        