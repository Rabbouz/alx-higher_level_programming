#include "lists.h"
/**
 * check_cycle - A function that check if a linked list
 * contains a cycle in it
 * @list: linked list
 * Return: 1 if the list has a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (!fast)
		return (0);

	if (slow == fast)
	{
		return (1);
	}

	return check_cycle(slow->next) || check_cycle(fast->next->next);
}
