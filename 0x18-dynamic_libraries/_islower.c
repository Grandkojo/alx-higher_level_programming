# include "main.h"

/**
 * _islower - Check Description
 * @c: An input character
 * Description: function uses _putchar to print alphabet in lowercase
 * Return: 1 if is lowercase or 0 if is uppercase
 */
int _islower(int c)
{
	char alpha;
	int lower = 0;

	for (alpha = 'a'; alpha <= 'z'; alpha++)
	{
		if (alpha == c)
			lower = 1;
	}
	return (lower);
}
