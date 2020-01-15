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

# Type of recipes
type = ['snack', 'steak', 'dish', 'dessert']

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


def testfunc():
	print("yes")
def testfunc2():
	print("no")

# Func for check recipe input
def add_recipe_check(recipe):
	for x in cookbook:
		if recipe == x:
			recipe = print_error("add_recipe_exist", "add_recipe", 1)
			add_recipe_check(recipe)
			sys.exit()
	if recipe == "exit":
		exit()
	return recipe

# Func for add new recipes
def add_recipe():
	recipe = print_menu("add_recipe", 1)
	add_recipe_check(recipe)
	print(recipe + " new recipe !")
	sys.exit()

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
			"Delete a recipe":testfunc,
			"Print a recipe":testfunc,
			"Print the cookbook":testfunc,
			"Quit":exit
		},
		"add_recipe":{
			"title":"\nPlease enter the recipe's name:",
		},
		"error":{
			"add_recipe_exist":"\nRecipe already exist, retry please"
		}
	}
	return hud;

print_menu("main", 0)
