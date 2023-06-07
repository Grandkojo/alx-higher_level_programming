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

	if (list == NULL || list->next == NULL)
        	return (0);

	c_one = list;
	c_two = list->next;
	
	while(c_one != NULL  && c_two != NULL)
	{
		if (c_one == c_two)
			return (1);
		c_one = c_one->next;
		c_two = c_two->next->next;
	}
	return (0);
}
