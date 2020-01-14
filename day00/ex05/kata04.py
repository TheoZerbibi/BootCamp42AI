i = (0, 4, 132.42222, 10000, 12345.67)

def printint(t):
	if (t < 10):
		print("0" + str(t), end='')
	else:
		print(t, end='')

if len(i) == 5:
	print("day_", end='')
	printint(i[0])
	print(", ex_", end='')
	printint(i[1])
	print(" : " + '%.*f' % (2, i[2]) + ", " + '%.2e' % (i[3]), end='')
	print(", " + '%.2e' % (i[4]))
