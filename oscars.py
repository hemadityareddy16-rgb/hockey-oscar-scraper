import time
import requests
import pandas as pd

url = "https://www.scrapethissite.com/pages/ajax-javascript/"
all_films = []

for year in range(2010, 2016):
    response = requests.get(url, params={"ajax": "true", "year": year})
    films = response.json()

    for film in films:
        all_films.append({
            "Title": film.get("title", "").strip(),
            "Year": film.get("year"),
            "Nominations": film.get("nominations"),
            "Awards": film.get("awards"),
            "Best Picture": "Yes" if film.get("best_picture", False) else "No",
        })

    print(year, "done -", len(films), "films")
    time.sleep(1)

df = pd.DataFrame(all_films)

with pd.ExcelWriter("hockey_teams.xlsx", mode="a",
                    if_sheet_exists="replace") as writer:
    df.to_excel(writer, sheet_name="Oscar Films", index=False)

print("Saved", len(df), "films to sheet 'Oscar Films'")