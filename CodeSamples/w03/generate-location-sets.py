# Before starting, please run:
## python3 -m pip install --upgrade pip
## python3 -m pip install --upgrade pandas
## python3 -m pip install --upgrade pandasql

import numpy as np
import pandas as pd
import pandasql as ps
from datetime import datetime

df_covid_data = pd.read_csv('owid-covid-data.csv')

known_locs = ps.sqldf(
	"SELECT location, MAX(people_fully_vaccinated_per_hundred) AS max_full_vac, date"
	+ " FROM df_covid_data GROUP BY location"
	+ " HAVING location != 'World'"
	+ " ORDER BY 2 DESC"
)


# blacklisted conditions
known_locs = known_locs[known_locs['location'] != 'Gibraltar']
known_locs = known_locs[known_locs['location'] != 'Pitcairn']
known_locs = known_locs[known_locs['max_full_vac'].notnull()]
known_locs = known_locs[known_locs['max_full_vac'] > 1]
known_locs.reset_index(drop=True, inplace=True)


list_location_sets = []
for index, row in known_locs.iterrows():
	if index % 5 == 0:
		this_set = [row['location']]
		list_location_sets.append(this_set)
	else:
		pos_of_last_item = len(list_location_sets) - 1
		list_location_sets[pos_of_last_item].append(row['location'])

df_location_sets = pd.DataFrame(list_location_sets, columns=['Location1','Location2','Location3','Location4','Location5'])
df_location_sets.to_csv("df_location_sets.csv")