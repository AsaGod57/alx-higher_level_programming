/*
 * File: 10-check_cycle.c
 * Auth: Godsway Asamoah
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Starts to check if a singly-linked list contains a cycle
 * @list: Specifies a  singly-linked list
 * Return: 1 if there is a cycle or 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return (0);
}
