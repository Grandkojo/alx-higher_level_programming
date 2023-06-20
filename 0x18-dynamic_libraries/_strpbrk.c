#include "main.h"
# include <stdio.h>

/**
 * _strpbrk - function that searches for any of a ser of bytes
 * @s: input char
 * @accept: input char
 * Return: pointer
 */
char *_strpbrk(char *s, char *accept)
{
	char *start = accept;

	while (*s)
	{
		while (*accept)
		{
			if (*accept == *s)
				return (s);
			accept++;
		}

		accept = start;
		s++;
	}
	return (NULL);
}
