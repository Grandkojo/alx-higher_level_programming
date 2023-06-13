#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - A function that checks if a singly linked list 
* is a palindrome.`
* @head: double pointer to the head of the linked list
* Return: 0 if not a palindrome, 1 if it's a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *node;
	int values[9999], i = 0, c = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	node = *head;
	if (!node->next)
	{
		return (1);
	}
	while (node)
	{
		values[i] = node->n;
		node = node->next;
		i++;
	}
	i--;
	while (i >= 0 && c <= i)
	{
		if (values[i] != values[c])
		{
			return (0);
		}
		i--;
		c++;
	}
	return (1);
}
