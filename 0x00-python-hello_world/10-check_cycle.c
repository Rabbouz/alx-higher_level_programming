#include "lists.h"
/**
 * check_cycle - A fucntion that checks if 
 * a linked list contains a cycle
 * @list: linked list
 * Return: 1 if the list has a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *low = list;
	listint_t *high = list;

	if (!list)
		return (0);

	while (low && high && high->next)
	{
		low = low->next;
		high = high->next->next;
		if (low == high)
			return (1);
	}

	return (0);
}
