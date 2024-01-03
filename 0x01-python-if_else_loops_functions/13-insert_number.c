/*
 * File: 13-insert_number.c
 * Auth: Godsway Asamoah
 */

#include "lists.h"

/**
 * insert_node - Starts to insert a number
 * @head: Specifies a  pointer to the head
 * @number: Specifies the number to insert
 * Return: A pointer to the new new node and  NULL if otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
