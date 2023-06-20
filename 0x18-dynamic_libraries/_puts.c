# include "main.h"

/**
 * _puts - check description
 * Description: prints a string followed by a new line
 * @str: input character
 * Return: Nothing
 */
void _puts(char *str)
{
	int index = 0;


	while (str[index] != '\0')
	{
		_putchar(str[index]);
		index++;
	}
	_putchar('\n');
}
