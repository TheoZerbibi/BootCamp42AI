import sys

def alpha(str):
	if str.isupper():
		str = str.lower()
	elif str.islower():
		str = str.upper()
	return str;

def arg(argv):
	res = ""
	for i in range(1, len(argv)):
		for x in range(len(argv[i])-1, -1, -1):
			if argv[i][x].isalpha():
				res += alpha(argv[i][x])
			else:
				res += argv[i][x]
		if i != len(argv) - 1:
			res += " "
	print(res)
	return;

if len(sys.argv) <= 1:
	exit()
arg(sys.argv)
