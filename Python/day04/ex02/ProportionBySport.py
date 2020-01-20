def proportionBySport(data, year, sport, gender):
	if gender.upper() not in ["M", "F"]:
		raise NameError("Invalid gender !")
	if sport not in data["Sport"].values:
		raise NameError("Invalid Sport !")
	select_gender = data["Sex"] == gender
	select_year = data["Year"] == year
	select_sport = data["Sport"] == sport
	players = data[select_gender & select_year & select_sport]["Name"].nunique()
	total = data[select_gender & select_year]["Name"].nunique()
	return players / total
