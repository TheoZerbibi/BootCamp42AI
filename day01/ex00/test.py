from book import Book
from recipe import Recipe


cookbook = {
	'sandwich': {
		'ingredients': [ 'ham', 'bread', 'cheese', 'tomatoes'],
		'meal': 'lunch',
		'prep_time': 10,
	},
	'cake': {
		'ingredients': [ 'flour', 'sugar', 'eggs'],
		'meal': 'dessert',
		'prep_time': 60,
	},
	'salad': {
		'ingredients': [ 'salad', 'tomatoe', 'mozzarella', 'spinach' ],
		'meal': 'lunch',
		'prep_time': 15,
		}
}

sandwich = Recipe('sandwich', 5, 1, [ 'ham', 'salad', 'tomatoe', 'cheese', 'steak', 'mushroom', 'pizza', 'shoes', 'coke' ], 'The awesome sandwich', 'lunch')
print(sandwich)

cake = Recipe('cake', 2, 4, [ 'flour', 'sugar', 'eggs', 'sugar', 'chocolate'], 'The delicious cake', 'dessert')
print(cake)

salad = Recipe('salad', 1, 2, [ 'arugula', 'tomatoes', 'spinach'], 'The awesome salad', 'starter')

my_book = Book('Awesome book', dict(starter=[salad], lunch=[sandwich], dessert=[cake]))

print(my_book)
