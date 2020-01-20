from random import shuffle

def generator(text, sep=" ", option=None):
	"""Option is an optional arg, sep is mandatory"""
	if type(text) is not str or option not in ["ordered", "shuffle", "unique", None]:
		return "ERROR"

	liste = text.split(sep)
	if option == "ordered":
		liste.sort(key=lambda word : word[0].swapcase())
	elif option == "unique":
		liste = set(liste)
	elif option == "shuffle":
		shuffle(liste)
	for word in liste:
		yield word

if __name__ == '__main__':
	text = "Le Lorem Ipsum est simplement du faux texte."
	print("Simple :\n")
	for word in generator(text, sep=" "):
		print(word)
	print("\nOrdered :\n")
	for word in generator(text, sep=" ", option="ordered"):
		print(word)
	print("\nShuffle :\n")
	for word in generator(text, sep=" ", option="shuffle"):
		print(word)
	print("\nUnique :\n")
	for word in generator(text, sep=" ", option="unique"):
		print(word)
