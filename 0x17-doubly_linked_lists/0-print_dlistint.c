#include "lists.h"

/**
 * Print list - doubly linked list
 * @h: head of the linked list
 *
 * Description: doubly linked list node structure
 *
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t compteur;
	dlistint_t *tmp;

	compteur = 0;
	tmp = h;
	while (tmp)
	{
		compteur++;
		printf("%d\n", tmp->n);
		tmp = tmp->next;
	}
	return (compteur);
}
