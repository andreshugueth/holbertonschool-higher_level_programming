#include "lists.h"
/**
 * is_palindrome - checks for a palindrome lk list
 * @head: copy of the beginning of the lk list
 *
 * Return: 1 if is palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	int scope;
	int opt[2048];
	int i;

	scope = 0;
	if (head == NULL || *head == NULL)
		return (1);

	while(*head != NULL)
	{
		scope++;
		opt[scope - 1] = (*head)->n;
		head = &(*head)->next;
	}

	for (i = 0; i < scope / 2; i++)
	{
		if (opt[i] != opt[scope - i - 1])
			return (0);
	}

	return (1);
}

