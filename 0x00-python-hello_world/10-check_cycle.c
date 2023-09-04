#include "lists.h"
/**
 * check_cycle - A function that check if a linked list
 * contains a cycle in it
 * @list: linked list
 * Return: 1 if the list has a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *sl = list;
	listint_t *fs = list->next;

	if (!list)
		return (0);
	while  (sl && fs && fs->next)
	{
		sl = sl->next;
		fs = fs->next->next;
		if (sl == fs)
			return (1);
	}
	return (0);
}
