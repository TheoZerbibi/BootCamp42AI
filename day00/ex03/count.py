import sys
import string

class List:
	def __init__(self,upper,lower,punctuation,spaces):
		self.upper = upper
		self.lower = lower
		self.punctuation = punctuation
		self.spaces = spaces

def print_result(res):
	print("- " + str(res.upper) + " upper letters")
	print("- " + str(res.lower) + " lower letters")
	print("- " + str(res.punctuation) + " punctuation marks")
	print("- " + str(res.spaces) + " spaces")
	return ;

def upper(str):
	nbr = 0
	for i in range(0, len(str)):
		if str[i].isupper():
			nbr +=1
	return nbr;

def lower(str):
	nbr = 0
	for i in range(0, len(str)):
		if str[i].islower():
			nbr +=1
	return nbr;

def punctuation(str):
	nbr = 0
	listPunctuation = string.punctuation
	for i in range(0, len(str)):
		if str[i] in listPunctuation:
			nbr +=1
	return nbr;

def spaces(str):
	nbr = 0
	for i in range(0, len(str)):
		if str[i].isspace():
			nbr +=1
	return nbr;

def checker(str):

	res = List(upper(str), lower(str), punctuation(str), spaces(str))
	print_result(res)
	return ;

def text_analyzer(str=None):
	"""
	This function counts the number of upper characters, lower characters,
 	punctuation and spaces in a given text.
	"""
	if str is None:
		str = input("What is the text to analyse?\n>> ")
		if len(str) <= 0:
			str = None
			text_analyzer(str)
			return ;
	checker(str)
	return ;
