import sys

# Dictionnaries for cookbook recipes
cookbook = {
	"sandwich":{
		"details":['salad', 'tomatoe', 'cheese', 'steak', 'mushroom', 'pizza', 'shoes', 'coke'],
		"type":"snack",
		"time":"5"
	},
	"cake":{
		"details":['flour', 'sugar', 'eggs'],
		"type":"dessert",
		"time":"60"
	},
	"salad":{
		"details":['salad', 'tomatoe', 'mozzarella', 'vinaigrette'],
		"type":"starter",
		"time":"10"
	},
}

# Types of recipes
types = ['snack', 'breakfast', 'meal', 'dessert']

# List for select arg in hud
select_tab = []

# Func for exit program
def exit():
	print("\nCookbook closed.")
	sys.exit()

# Func for print error message
def print_error(error_select, select, nb):
	hud = create_dic()
	print(hud["error"][error_select])
	index = input(">> ")
	return index;

# Func for print cookbook
def print_cookbook():
	str = ""
	for x in cookbook:
		str += x
		str += ", "
	print("\nCookbook :\n" + str + "\n")
	print_menu("main", 0)

# Func for check and print recipe
def print_recipe_check(recipe):
	for x in cookbook:
		if x == recipe:
			return recipe;
	recipe = print_error("print_recipe_no_exist", "print_recipe", 1)
	recipe = print_recipe_check(recipe)
	return recipe

def print_recipe():
	recipe = print_menu("print_recipe", 1)
	recipe = print_recipe_check(recipe)
	print("\nIngredients list: " + str(cookbook[recipe]['details']))
	print("To be eaten for " + str(cookbook[recipe]['type']))
	print("Takes " + str(cookbook[recipe]['time']) + " minutes of cooking.\n")
	print_menu("main", 0)

# Func for check en delete recipe
def del_recipe_check(recipe):
	for x in cookbook:
		if recipe == x:
			del cookbook[recipe]
			return recipe;
	recipe = print_error("del_recipe_no_exist", "print_recipe", 1)
	recipe = print_recipe_check(recipe)
	return recipe;

def del_recipe():
	recipe = print_menu("del_recipe", 1)
	recipe = del_recipe_check(recipe)
	print("\n" + recipe + " as been delete\n")
	print_menu("main", 0)

# Func for check recipe input
def add_recipe_check(recipe):
	for x in cookbook:
		if recipe == x:
			recipe = print_error("add_recipe_exist", "add_recipe", 1)
			recipe = add_recipe_check(recipe)
			return recipe;
	if recipe == "exit":
		exit()
	return recipe

def add_recipe_details(nb, list):
	new = input("Add new ingredients, write stop for next step:\n>> ")
	if new == "stop":
		return list;
	elif new == "exit":
		print("You cant leave now !")
	elif len(new) <= 0:
		print("Enter a ingredients")
		add_recipe_details(nb, list)
	else:
		list.insert(nb, new)
		nb += 1
		add_recipe_details(nb, list)
	return list;

def add_recipe_type():
	type = input("Enter a type (snack, breakfast, meal, dessert)\n>> ")
	if type in types:
		return type;
	else:
		return add_recipe_type()
	return type;

def add_recipe_time():
	time = input("Enter cooking time for recipe\n>> ")
	if len(time) <= 0 or not time.isnumeric() or int(time) <= 0:
		print("Not a valid time")
		return add_recipe_time()
	return time;


# Func for add new recipes
def add_recipe():
	recipe = print_menu("add_recipe", 1)
	recipe = add_recipe_check(recipe)
	list = []
	list = add_recipe_details(0, list)
	type = add_recipe_type()
	time = add_recipe_time()
	new_dic = {recipe:{"details":list, "type":type, "time":time}}
	cookbook.update(new_dic)
	print("\nRecipe " + recipe + " as been add in cookbook !\n")
	print_menu("main", 0)

# Function for check en call specific function
# in relation to the selected elements
def selections(select, i, nb):
	err = 0
	index = input(">> ")
	if index == "exit":
		exit()
	if nb == 0:
		for char in index:
			if not char.isnumeric():
				err = 1
				break ;
		if err == 1 or len(index) <= 0 or int(index) >= i:
			print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter " + str(i-1))
			selections(select, i, 0)
			sys.exit()
		select_tab[int(index)-1]()
	elif nb == 1:
		if i == 1:
			if len(index) <= 0:
				print_menu(select, nb)
				sys.exit()
			return index;
	return ;


# Func for print_menu
def print_menu(select, nb):
	select_tab.clear()
	hud = create_dic()
	i = 0
	for x in hud[select]:
		if x == "title":
			if i == 0:
				print(hud[select][x])
		elif x == "func":
			if i == 0:
				select_tab.insert(i, hud[select][x])
		else :
			select_tab.insert(i, hud[select][x])
			print(str(i+1) +": "+ x)
			i += 1
	index = selections(select, i+1, nb)
	return index;

# Dictionnaries for hud menu or error message
def create_dic():
	hud = {
		"main":{
			"title":"Please select an option by typing the corresponding number:",
			"Add recipe":add_recipe,
			"Delete a recipe":del_recipe,
			"Print a recipe":print_recipe,
			"Print the cookbook":print_cookbook,
			"Quit":exit
		},
		"add_recipe":{
			"title":"\nPlease enter the recipe's name to add it:",
		},
		"del_recipe":{
			"title":"\nPlease enter the recipe's name delete it:"
		},
		"print_recipe":{
			"title":"\nPlease enter the recipe's name to get its details:"
		},
		"error":{
			"add_recipe_exist":"\nRecipe already exist, please retry",
			"print_recipe_no_exist":"\nYour recipe doesnt exist, please retry",
			"del_recipe_no_exist":"\nYour recipe doesnt exist, please retry"
		}
	}
	return hud;

print_menu("main", 0)
