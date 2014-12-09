def slices(number_string, length):

	if length > len(number_string):
		raise ValueError('slice length should not be larger than string length.')

	elif length < 1:
		raise ValueError('slice length should not be zero.')

	number_list = number_string.split()

	list_of_lists = []

	for i in range(len(number_list)):
		#sub_list = number_list[i:i+length-1]
		list_of_lists.append(number_list[i:i+length-1])

	return list_of_lists