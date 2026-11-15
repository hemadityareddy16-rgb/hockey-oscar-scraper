\# Hockey Teams and Oscar Films Scraper



Python scraper that collects data from two different types of web pages and delivers it as a clean, formatted Excel report.



\## What it does



\- \*\*Hockey teams:\*\* scrapes all 24 pages of team stats (582 rows), using the site's page number in the URL.

\- \*\*Oscar films:\*\* reads the JSON data that the page loads in the background (AJAX), for the years 2010 to 2015 (87 films).

\- \*\*Cleaning:\*\* strips extra spaces, converts text to real numbers, and handles missing fields without crashing.

\- \*\*Report:\*\* one Excel file with 4 sheets: Hockey Teams, Oscar Films, Top Teams (top 10 by win %), and Oscar Summary (per-year totals and Best Picture winner).



\## Tools used



Python, requests, BeautifulSoup, pandas, openpyxl



\## How to run



&#x20;   pip install -r requirements.txt

&#x20;   python hockey.py

&#x20;   python oscars.py

&#x20;   python summary.py

&#x20;   python format\_excel.py



Output: `hockey\_teams.xlsx`



\## Data source



\[scrapethissite.com](https://www.scrapethissite.com), a site built for practising web scraping.



\## Available for freelance work



I build scrapers that collect data from websites and deliver it as clean Excel or CSV files.

