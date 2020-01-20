class SpatioTemporalData:
	def __init__(self, data):
		self.data = data

	def when(self, location):
		if location not in self.data["City"].values:
			raise NameError("Invalid City !")
		select_city = self.data["City"] == location
		res = self.data[select_city]["Year"].unique()
		return res.tolist();

	def where(self, date):
		if date not in self.data["Year"].values:
			raise NameError("Invalid Date !")
		select_year = self.data["Year"] == date
		res = self.data[select_year]["City"].unique()
		return res.tolist()
