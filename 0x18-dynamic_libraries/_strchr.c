# include "main.h"
# include <stdio.h>

/**
 * _strchr - Locates a character in a string
 * @s: input character
 * @c: input char
 * Return: pointer;
 */
char *_strchr(char *s, char c)
{
	while (*s)
	{
		if (c == *s)
			return (s);
		s++;
	}
	if (c == *s)
		return (s);
	return (NULL);
}

