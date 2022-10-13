import bs4
import requests
import pandas as pd


def scrap_and_save_csv(table_id):
    table_overall = soup.find(id=table_id)
    headers_table_overall = []
    for i in table_overall.select("thead tr:not(.over_header) th"):
        title = i.text
        headers_table_overall.append(title)

    df_table_overall = pd.DataFrame(columns=headers_table_overall)
    for j in table_overall.select("tbody tr"):
        row_rank = j.find_all("th")
        row_data = j.find_all("td")
        row = [i.text for i in row_rank + row_data]
        df_table_overall.loc[len(df_table_overall)] = row

    df_table_overall.to_csv(table_id + ".csv")


EPL_DATA = "https://fbref.com/en/comps/9/Premier-League-Stats"
response = requests.get(EPL_DATA)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

table_ids = ["results2022-202391_overall",
             "div_stats_squads_standard_for",
             ]

for table_id in table_ids:
    scrap_and_save_csv(table_id)
