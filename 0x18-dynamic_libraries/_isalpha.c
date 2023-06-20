# include "main.h"

/**
 * _isalpha - Check code
 * @c: An input character
 * Description: Checks for alphabetic character
 *Return: Always 0 (Success)
 */
int _isalpha(int c)
{
	char lower, upper;
	int isletter = 0;

	for (lower = 'a'; lower <= 'z'; lower++)
	{
		for (upper = 'A'; upper <= 'z'; upper++)
		{
			if (c == lower || c == upper)
				isletter = 1;
		}
	}
	return (isletter);
}
