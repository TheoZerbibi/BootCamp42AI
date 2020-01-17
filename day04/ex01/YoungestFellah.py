import pandas as pd


def youngestFellah(data, year):
	male = data["Sex"] == "M"
	female = data["Sex"] == "F"
	select_year = data["Year"] == year
	age_male = data[male & select_year]["Age"].min()
	age_female = data[female & select_year]["Age"].min()
	return dict(f=age_female, m=age_male)
