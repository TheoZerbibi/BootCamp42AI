from datetime import datetime

class Book:
	def __init__(self, name, recipe_list):
		self.name = name
		self.last_update = datetime.now()
		self._creation_date = datetime.now()
		self.recipe_list = recipe_list

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, new_name):
		if not new_name or len(new_name) <= 0:
			raise Exception("Name cannot be empty !")
			return ;
		self._name = new_name

	@property
	def last_update(self):
		return self._last_update

	@last_update.setter
	def last_update(self, new_time):
		if type(new_time) is not datetime:
			raise Exception("Invalid time !")
		self._last_update = new_time

	@property
	def creation_date(self):
		return self._creation_date

	@property
	def recipe_list(self):
		return self._recipe_list

	@recipe_list.setter
	def recipe_list(self, new_list):
		for i in new_list.keys():
			if i not in ["starter", "lunch", "dessert"]:
				raise Exception("Invalid recipe_list !\nMust be starter, lunch or dessert only")
		self._recipe_list = new_list

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for _, recipe in self.recipe_list.items():
			if recipe.name == name:
				print(recipe)
				return recipe

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		return [recipe for recipe in self.recipe_list[recipe_type]]

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if type(recipe) is Recipe:
			self.recipe_list[recipe.recipe_type].append(recipe)
			self.last_update = datetime.now()
		else:
			print(f"{recipe} doesn't exist !")
			return

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = f"""
		The recipe's book name is {self.name}
		Contains {', '.join([name[0] for name in [[recipe.name for recipe in recipes] for recipes in self.recipe_list.values()]])},
		Was create at {self.creation_date} and last updated at {self.last_update}
		"""
		return txt
