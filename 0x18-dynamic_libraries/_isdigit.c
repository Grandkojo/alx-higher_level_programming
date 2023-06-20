# include "main.h"

/**
 * _isdigit - Check description
 * @c: input character
 * Description: Checks for a digit (0 through 9)
 * Return: 1 if c is digit or otherwise
 */
int _isdigit(int c)
{
	char num;

	int ret = 0;

	for (num = '0'; num <= '9'; num++)
	{
		if (c == num)
		{
			ret = 1;
			break;
		}
	}
	return (ret);
}
