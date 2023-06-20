#include "main.h"

/**
 * _strlen - Check description
 * @s: input string
 * Description: print the length of a string
 * Return: Always l Success
 */
int _strlen(char *s)
{
	int len = 0;

	while (s[len] != '\0')
		len++;
	return (len);
}
