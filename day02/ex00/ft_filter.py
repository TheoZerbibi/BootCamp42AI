def ft_filter(function_to_apply, list_of_inputs):
	return [element for element in list_of_inputs if function_to_apply(element)]



if __name__ == '__main__':
	results = list(filter(lambda x : x > 2, [1,2,3,4,5]))
	ft_results = list(ft_filter(lambda x : x > 2, [1,2,3,4,5]))

	print(results)
	print(ft_results)
	print(results == ft_results)
