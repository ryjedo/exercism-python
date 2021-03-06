from operator import mul

def largest_product(number_string, series_length):

	result = 0
	for number_slice in slices(number_string, series_length):
		if series_product(number_slice) > result:
			result = series_product(number_slice)
	
	return result

def slices(number_string, series_length):

	#error checking
	if series_length > len(number_string):
		raise ValueError('Series length should not be larger than string length.')

	#convert input string to list of ints
	numberstring_list_as_ints = [int(i) for i in list(number_string)]

	#iterate through list of ints, and make series list.
	return [(numberstring_list_as_ints[i:i+series_length]) for i in range(0,len(numberstring_list_as_ints) - series_length + 1)]

def series_product(number_slice):
	return reduce(mul, number_slice, 1)