#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: head of the list
 *
 * Return: 1 if there is a cycle, 0 if there isn't
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (list == NULL)
		return (0);

	first = second = list;
	while (second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
