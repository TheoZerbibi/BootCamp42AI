import pandas as pd


def youngestFellah(data, year):
	male = data["Sex"] == "M"
	female = data["Sex"] == "F"
	sel_year = data["Year"] == year
	age_male = data[male & sel_year]["Age"].min()
	age_female = data[female & sel_year]["Age"].min()
	return dict(f=age_female, m=age_male)
