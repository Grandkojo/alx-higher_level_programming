# include "main.h"

/**
 * _memcpy - copies memory area
 * @dest: input character
 * @src: input character
 * @n: input integer
 * Return: pointer
 */
char *_memcpy(char *dest, char *src, unsigned int n)
{
	char *start = dest;

	while (n--)
	{
		*dest = *src;
		src++;
		dest++;
	}
	return (start);
}
