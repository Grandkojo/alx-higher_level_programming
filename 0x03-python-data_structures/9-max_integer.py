#!/usr/bin/python3
def max_integer(my_list=[]):
	max = 0
	if my_list is None:
       		return
   	elif len(my_list) == 0:
        	return

	else:	
		for i in range(len(my_list)):
			if my_list[i] >= max:
				max = my_list[i]
		return max
