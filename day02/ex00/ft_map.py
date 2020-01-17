def ft_map(function_to_apply, list_of_inputs):
	return (function_to_apply(element) for element in list_of_inputs)

if __name__ == '__main__':
	def square(x):
		return x * x

	results = list(map(square, [1, 2, 3, 4, 5]))
	ft_results = list(ft_map(square, [1, 2, 3, 4, 5]))

	print(results)
	print(ft_results)
	print(results == ft_results)
