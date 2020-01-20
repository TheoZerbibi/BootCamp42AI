import sys

def check(argv):
	res = argv % 2
	if argv == 0:
		print("I'm Zero.")
	elif res > 0:
		print("I'm Odd.")
	else:
		 print("I'm Even.")
	return;

if len(sys.argv) == 1:
	sys.exit();
if len(sys.argv) >= 3 or sys.argv[1].isalpha():
	print("ERROR")
	sys.exit()

check(int(sys.argv[1]))
