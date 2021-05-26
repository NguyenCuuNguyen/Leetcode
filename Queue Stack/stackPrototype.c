#include <stdio.h>
#include <stdlib.h>

typedef struct Element{
  struct Element *next;
  void *data;
}Element;

void push(Element **stack, void* data);
void *pop(Element **stack);
