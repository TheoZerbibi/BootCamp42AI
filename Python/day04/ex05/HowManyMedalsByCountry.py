import pandas as pd
import time

def howManyMedalsByCountry(data, country):
	if country not in data["Team"].values:
		raise NameError("Invalid Country !")
	select_team = data["Team"] == country
	data_result =data[select_team]
	count = {}
	start = time.time()
	for year in data_result["Year"]:
		select_year = data_result["Year"] == year
		count[year] = dict(data_result[select_year]["Medal"].value_counts())
	result = {}
	for year in count:
		try:
			gold = count[year]["Gold"]
		except KeyError:
			gold = 0
		try:
			silver = count[year]["Silver"]
		except KeyError:
			silver = 0
		try:
			bronze = count[year]["Bronze"]
		except KeyError:
			bronze = 0
		result[year] = dict(G=gold, S=silver, B=bronze)
	end = time.time()
	diff = end - start
	time_end = f"{diff:.03f} s" if diff > 0.01 else f"{(diff  * 1000):.03f} ms]"
	print(time_end)
	return result
