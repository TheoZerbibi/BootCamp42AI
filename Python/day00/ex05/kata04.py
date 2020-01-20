i = (51, 81, 1302.5642222, 100045343540, 1234654345.67)

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
