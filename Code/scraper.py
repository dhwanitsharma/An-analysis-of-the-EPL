from bs4 import BeautifulSoup
import requests
import pandas as pd

import time

passing_df = pd.DataFrame()
pass_type_df = pd.DataFrame()
response = requests.get('https://fbref.com/en/comps/9/1889/2018-2019-Premier-League-Stats')
soup = BeautifulSoup(response.content)
soup = BeautifulSoup(response.content,parser = 'lxml')
table = soup.find('table',{'id':'results18891_overall'})
rows = [x.find('td') for x in table.find_all('tr')[:]][1:]
team_link = [x.find('a')["href"] for x in rows]
team_name = [x.find('a').text for x in rows]
for n,p in zip(team_name,team_link):
    soup = BeautifulSoup(requests.get('https://fbref.com/'+p).content)
    table = soup.find('table',{'id':'stats_passing_1889'})
    data = pd.read_html(str(table))[0]
    data['Unnamed: 27_level_0', 'Matches'] = [n for i in range(len(data))]
    passing_df = passing_df.append(data,ignore_index=1)
    table = soup.find('table',{'id':'stats_passing_types_1889'})
    data = pd.read_html(str(table))[0]

    data['Unnamed: 30_level_0', 'Matches'] = [n for i in range(len(data))]
    pass_type_df = pass_type_df.append(data, ignore_index=1)

    print("f")
    time.sleep(2)
passing_df.to_csv('passing_df1819.csv',index=0)
pass_type_df.to_csv('pass_type_df_1819.csv',index = 0)