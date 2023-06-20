# include "main.h"

/**
 * _memset - Fills amemory with a constant byte
 * @s: iput character
 * @b: input character
 * @n: inputt integer
 * Return: pointer
 */
char *_memset(char *s, char b, unsigned int n)
{
	char *start = s;

	while (n--)
	{
		*s = b;
		s++;
	}
	return (start);
}
