import functools

def ft_reduce(function_to_apply, list_of_inputs):
	res = list_of_inputs[0]
	res = function_to_apply(res, list_of_inputs[1])
	for i in range(len(list_of_inputs) - 1, len(list_of_inputs)):
		print("res : "+ str(res))
		print(i)
		res = function_to_apply(res, list_of_inputs[i])
	return res


if __name__ == '__main__':
	def add(x, y):
		return x + y
	my_numbers = [1,2,3,4,5]

	results = functools.reduce(add, [1,2,3,4,5])
	ft_results = ft_reduce(add, [1,2,3,4,5])

	print(results)
	print(ft_results)
	print(results == ft_results)
