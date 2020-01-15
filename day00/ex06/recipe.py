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

def testfunc():
	print("yes")
def testfunc2():
	print("no")

# Dictionnaries for menu hud
hud = {
	"main":{
		"Add recipe":testfunc,
		 "Delete a recipe":testfunc2,
	}
}

# Func for print_menu
def print_menu(select):
	i = 0
	for x in hud[select]:
		select_tab.insert(i, hud[select][x])
		print(str(i+1) +": "+ x)
		i += 1
	index = int(input(">> ")) - 1
	select_tab[int(index)]()
	return ;

print_menu("main")
