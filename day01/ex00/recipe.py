class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, new_name):
		if not new_name or len(new_name) <= 0:
			raise Exception("Invalid name !\nName cannot be empty !")
			return ;
		self._name = new_name

	@property
	def cooking_lvl(self):
		return self._cooking_lvl

	@cooking_lvl.setter
	def cooking_lvl(self, new_level):
		if new_level not in range(1,6):
			raise Exception("Invalid cooking_level !\ncooking_lvl must superior at 1 and inferior at 5 !")
		self._cooking_lvl = new_level

	@property
	def cooking_time(self):
		return self._cooking_time

	@cooking_time.setter
	def cooking_time(self, new_time):
		if new_time < 0:
			raise Exception("Invalid cooking time !\ncooking_time must be superior at 0 !")
		self._cooking_time = new_time

	@property
	def ingredients(self):
		return self._ingredients

	@ingredients.setter
	def ingredients(self, new_ingredients):
		if not new_ingredients:
			raise Exception("Ingredients cannot be empty !")
		self._ingredients = new_ingredients

	@property
	def recipe_type(self):
		return self._recipe_type

	@recipe_type.setter
	def recipe_type(self, new_type):
		if new_type not in ["starter", "lunch", "dessert"]:
			raise Exception("Invalid recipe_list !\nMust be starter, lunch or dessert only")
		self._recipe_type = new_type

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = f"""
		The recipe name is : {self.name}
		Of type {self.recipe_type}, is made with : {', '.join(self.ingredients)}
		The cooking time is : {self.cooking_time}
		The cooking level is : {self.cooking_lvl}
		"""
		return txt
