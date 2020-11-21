/*
  Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą.
  Proszę napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę stałą. Warunkiem jej
  usunięcia jest istnienie w liście dokładnie jednej najdłuższej podlisty stałej. Do funkcji należy
  przekazać wskaźnik na pierwszy element listy. Funkcja powinna zwrócić liczbę usuniętych elementów.

  Na przykład:
  Z listy [1 3 3 35 7 11 13 131 2 2 2 23] należy usunąć podlistę [2 2 2 2]
  A z listy [1 3 3 3 35 7 11 13 131 2 2 2 23] nie należy nic usuwać.
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct list {
  int val;
  struct list *next;
} list_t;

list_t *list_init(int val) {
  list_t *l = (list_t *)malloc(sizeof(list_t));
  if (l == NULL) {
    return NULL;
  }
  l->val = val;
  l->next = NULL;
  return l;
}

void list_delete(list_t *l) {
  if (l == NULL) {
    return;
  }
  free(l);
}

int list_delete_continuous_chunk(list_t *l) {
  int max = 0, cmax = 0, loc;
  list_t *prev = NULL, *next = NULL, *prev_max = NULL, *curr = l;

  while (curr != NULL) {
    loc = 1;

    while (curr->next != NULL && curr->val == curr->next->val) {
      loc++;
      curr = curr->next;
    }

    if (loc > max) {
      max = loc;
      prev_max = prev;
      cmax = 1;
    }
    else if (loc == max) {
      cmax += 1;
    }

    prev = curr;
    curr = curr->next;
  }

  if (cmax > 1) {
    return 0;
  }

  curr = prev_max->next;
  next = curr->next;

  for (int i = 0; i < max - 1; i++) {
    list_delete(curr);
    curr = next;
    next = next->next;
  }
  prev_max->next = next;

  return max;
}

void list_print(list_t *l) {
  for (; l != NULL; l = l->next) {
    printf("%i ", l->val);
  }
  printf("\n");
}

int main(void) {
  list_t *l, *prev, *curr = NULL;
  int vals[] = {2, 1, 1, 1, 1, 3, 4, 5, 5, 7, 11, 13, 131, 2, 2, 2};

  l = list_init(vals[0]);
  prev = l;

  for (unsigned i = 1; i < sizeof(vals) / sizeof(vals[0]); i++) {
    curr = list_init(vals[i]);
    prev->next = curr;
    prev = curr;
  }

  list_print(l);

  printf("%i\n", list_delete_continuous_chunk(l));
  list_print(l);

  printf("%i\n", list_delete_continuous_chunk(l));
  list_print(l);

  printf("%i\n", list_delete_continuous_chunk(l));
  list_print(l);

  return 0;
}

