# include "main.h"

/**
 * _strcpy - check description
 * Description: copies the string pointed to src, including
 * the terminating null byte (\0)., to the buffer poited
 * to by dest
 * @dest: A pointer to destination of string
 * @src: A pointer to source string to copy from
 * Return: pointer to dest
 */
char *_strcpy(char *dest, char *src)
{
	char *aux = dest;

	while (*src)
		*dest++ = *src++;
	return (aux);
}
