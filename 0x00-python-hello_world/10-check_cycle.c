#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
*check_cycle - check if a singly linked list has a cycle or not
*@list: pointer to the list
*
*Return: 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *c_one, *c_two;

	c_one = list;
	c_two = list;
	
	while(c_one && c_two)
	{
		if (c_two == NULL)
			return (0);
		c_two =  c_two->next;
		c_one = c_one->next->next;
		if (c_one == c_two)
				return (1);
	}
	return (0);
}
