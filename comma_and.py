# For; 'Automating the boring stuff with Python - Chapter 4'


def comma_and(any_list):
	"""
	Attempt to determine the last item from a list.
	Remove last item from the list.
	Convert list to string, separate with a comman and
	then print the string inserting 'and' before concluding
	with printing the initially removed last_value.
	"""
	last_value = any_list[-1]
	any_list.remove(last_value)
	result = ', '.join(any_list)
	print (result.title() + ' and ' + last_value.title() + '.')
	
my_list_1 = ['the girl', 'the gold watch', 'everything']
comma_and(my_list_1)
