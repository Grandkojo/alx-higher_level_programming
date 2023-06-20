# include "main.h"

/**
 *  _strncpy - Check description
 *  Description: function copies a string
 *  @dest: input chracteer
 *  @src: input character
 *  @n: input integer
 *  Return: Original pointer
 */
char *_strncpy(char *dest, char *src, int n)
{
	int srclen = 0, i = 0;
	char *temp = dest, *start = src;

	while (*src)
	{
		srclen++;
		src++;
	}

	srclen++;

	if (n > srclen)
		n = srclen;

	src  = start;

	for (; i < n; i++)
		*dest++ = *src++;

	return (temp);
}
