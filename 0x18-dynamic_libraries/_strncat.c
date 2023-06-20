#include "main.h"

/**
 * _strncat - Check description
 * Description: concatenates two strings up to n number
 * @dest: input string
 * @src: input string
 * @n: input integer
 * Return: default pointer
 */

char *_strncat(char *dest, char *src, int n)
{
	int srclen = 0, i = 0;
	char *temp = dest, *start = src;

	while (src)
	{
		srclen++;
		src++;
	}

	while (*dest)
		dest++;

	if (n > srclen)
		n = srclen;

	src = start;

	for (; i < n; i++)
		*dest++ = *src++;

	*dest = '\0';
	_putchar('\n');
	return (temp);
}
