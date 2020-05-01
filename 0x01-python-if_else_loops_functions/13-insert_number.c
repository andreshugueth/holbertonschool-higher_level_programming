#include "lists.h"
/**
 * insert_node - Insert a node in a position
 * @head: copy of head pointer in main
 * @number: Data in the struct
 * Return: ptr of the new element on sucess
 * NUll if a failure ocur
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *ptr, *curr;
	if (!head)
		return (NULL);
	ptr = malloc(sizeof(listint_t));
	if (!ptr)
		return (NULL);
	ptr->n = number;
	prev = NULL;
	curr = *head;
	while(curr && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}
	ptr->next = curr;
	if (prev)
		prev->next = ptr;
	else
		*head = ptr;
	return (ptr);
}
