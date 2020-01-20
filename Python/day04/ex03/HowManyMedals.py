import pandas as pd

def howManyMedals(data, name):
	if name not in data["Name"].values:
		raise NameError("Invalid Name !")
	select_name = data["Name"] == name
	data_result =data[select_name]
	count = {}
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
	return result
