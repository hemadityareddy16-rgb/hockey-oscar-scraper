import pandas as pd

file = "hockey_teams.xlsx"
teams = pd.read_excel(file, sheet_name=0)
films = pd.read_excel(file, sheet_name="Oscar Films")

top_teams = (teams.sort_values("Win %", ascending=False)
                  .head(10)[["Team", "Year", "Wins", "Losses", "Win %"]])

by_year = films.groupby("Year").agg(
    Films=("Title", "count"),
    Nominations=("Nominations", "sum"),
    Awards=("Awards", "sum"),
).reset_index()

winners = (films[films["Best Picture"] == "Yes"][["Year", "Title"]]
           .rename(columns={"Title": "Best Picture Winner"}))
by_year = by_year.merge(winners, on="Year", how="left")

with pd.ExcelWriter(file, mode="a", if_sheet_exists="replace") as writer:
    top_teams.to_excel(writer, sheet_name="Top Teams", index=False)
    by_year.to_excel(writer, sheet_name="Oscar Summary", index=False)

print("Summary sheets added")
print(top_teams)
print(by_year)