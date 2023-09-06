#include "lists.h"
/**
 * insert_node - A function that inserts a 
 * number into a sorted singly-linked list.
 * @head: A pointer
 * @number: A number
 * Return: If the function fails return NULL,
 * Otherwise return  a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *hd, *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = number;
	if (node == NULL || node->n >= number)
	{
		nw->next = node;
		*hd = nw;
		return (nw);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	nw->next = node->next;
	node->next = nw;
	return (nw);
}
