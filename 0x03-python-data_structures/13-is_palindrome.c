#include "lists.h"

/**
 * reverse_linked_list - function that reverse a linked list
 * @head: head of the linked list
 * Return: reversed linked list
 */
listint_t *reverse_linked_list(listint_t *head)
{
	listint_t *current_node;
	listint_t *next_node;

	if (head == NULL)
	{
		return (NULL);
	}
	current_node = head;
	next_node = current_node->next;
	current_node->next = NULL;
	while (next_node != NULL)
	{
		current_node = next_node;
		next_node = next_node->next;
		current_node->next = head;
		head = current_node;
	}
	return (head);
}

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: head of the linked list
 * Return: 1 if the linked list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy_1 = *head;
	listint_t *copy_2 = *head;
	listint_t *copy_3 = *head;
	listint_t *reversed;
	int num_of_nodes = 0;
	int half = 0;

	if (*head == NULL)
	{
		return (1);
	}
	while (copy_1)
	{
		num_of_nodes += 1;
		copy_1 = copy_1->next;
	}
	while (half != (num_of_nodes / 2))
	{
		half += 1;
		copy_2 = copy_2->next;
	}
	reversed = reverse_linked_list(*head);
	while (copy_3 && reversed)
	{
		if (copy_3->n != reversed->n)
		{
			return (0);
		}
		copy_3 = copy_3->next;
		reversed = reversed->next;
	}
	return (1);
}
