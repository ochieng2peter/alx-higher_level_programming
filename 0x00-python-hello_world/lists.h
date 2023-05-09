#ifndef _LISTS_H
#define _LISTS_H


#include <stdlib.h>

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);i
int check_cycle(listint_t *list);
void free_listint(listint_t *head);

/**
 * struct listint_s - the singly linked list
 * @n: an integer
 * @next: points to the next node
 * Description: singly linked list node structure
 */
typedef struct listint_s

{
        int n;
        struct listint_s *next;
}
listint_t;

#endif /* _LISTS_H */
