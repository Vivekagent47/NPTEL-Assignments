#include <stdio.h>
#include <stdlib.h>

struct DoublyLinkedList{
	int data;
	struct DoublyLinkedList *prev;
	struct DoublyLinkedList *next;
};

struct DoublyLinkedList *createNode(int n)
{
	struct DoublyLinkedList *newNodeptr;
	newNodeptr = (struct DoublyLinkedList*)
		malloc (sizeof(struct DoublyLinkedList));
	newNodeptr->data = n;
	newNodeptr->prev = NULL;
	newNodeptr->next = NULL;
	return newNodeptr;
}
void appendNode ( struct DoublyLinkedList **tailptr, int n )
{
	struct DoublyLinkedList *newNode;
	newNode = createNode ( n );
	newNode->prev=*tailptr;

	(*tailptr)->next = newNode;

	*tailptr=newNode;
}

void initializeList (
	struct DoublyLinkedList **headptr,
	struct DoublyLinkedList **tailptr,
	int n)
{
	struct DoublyLinkedList *newNode;
	newNode=createNode(n);
	*headptr=newNode;
	*tailptr=newNode;
	return;
}

void printList(
	struct DoublyLinkedList *head,
	struct DoublyLinkedList *tail)
{
	struct DoublyLinkedList *curr=head;

	while ( curr != NULL ){
                if(curr->next!=NULL)
		printf("%d,",curr->data);
                else printf("%d",curr->data); 
		curr = curr->next;
	}

	return;
}
void removeNode (
	struct DoublyLinkedList **headptr,
	struct DoublyLinkedList **tailptr,
	struct DoublyLinkedList *ptr)
{
	if ( ptr == *headptr ){
		*headptr = ptr->next;
		(*headptr)->prev = NULL;
	}else{
		if ( ptr == *tailptr ) {
			*tailptr = ptr->prev;
			(*tailptr)->next=NULL;
		}else{
			ptr->prev->next = ptr->next;
			ptr->next->prev = ptr->prev;
		}
	}
	free ( ptr );
	ptr = NULL;
	return;			
}

void removeData (
	struct DoublyLinkedList **headptr,
	struct DoublyLinkedList **tailptr,
	int n)
{
	struct DoublyLinkedList *curr;
	curr = *headptr;

	while ( curr != NULL && curr->data != n ){
		curr = curr->next;
	}
	if ( curr != NULL ){
		removeNode(headptr, tailptr, curr);
	}
	return;
}


int main()
{
	int n;
	int i=0;
	int m;
	struct DoublyLinkedList *head, *tail;

	scanf("%d",&n);

	if ( n <= 0 ){
		return 0;
	}

	scanf("%d",&m);
	initializeList(&head,&tail,m);


	for(i=1;i<n;i++){ /* read the remaining elements */
		scanf("%d",&m);
		appendNode(&tail,m);
	}
  

	scanf("%d",&n);
	removeData ( &head, &tail, n );
	printList(head,tail);

	return 0;
}
