import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/forms/"
columns = ["Team", "Year", "Wins", "Losses", "OT Losses",
           "Win %", "Goals For", "Goals Against", "Diff"]

all_rows = []
page = 1

while True:
    response = requests.get(url, params={"page_num": page})
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr", class_="team")

    if len(rows) == 0:
        break

    for row in rows:
        cells = row.find_all("td")
        all_rows.append([c.get_text(strip=True) for c in cells])

    print("Page", page, "done -", len(rows), "teams")
    page += 1
    time.sleep(1)

df = pd.DataFrame(all_rows, columns=columns)

for col in columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.to_excel("hockey_teams.xlsx", index=False)
print("Saved", len(df), "rows to hockey_teams.xlsx")