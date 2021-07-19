#include <stdio.h>
#include <stdlib.h>

#define TREE_NODE_MAX 32

typedef struct tagTREE_NODE
{
	int iValue;
	struct tagTREE_NODE *pstLChild;
	struct tagTREE_NODE *pstRChild;
}TREE_NODE_S;

typedef struct tagTREE_NODE_STACK
{
	TREE_NODE_S *astStack[TREE_NODE_MAX];
	unsigned int uiBase, uiTop;
}TREE_NODE_STACK_S;

void Push(TREE_NODE_STACK_S *pstStack, TREE_NODE_S *pstNode)
{
	if(NULL == pstStack || NULL == pstRoot)
	{
		printf("para is null");
	}

	if(TREE_NODE_MAX == pstStack->uiTop)
	{
		printf("stack is full");
	}

	pstStack->astStack[pstStack->uiTop] = pstNodes;
	pstStack->uiTop++;

	return;
}

void Pop(TREE_NODE_STACK_S *pstStack, TREE_NODE_S *pstRoot)
{
	
}

void PreOrder(TREE_NODE_S *pstRoot)
{
	TREE_NODE_STACK_S stStack;

	if(NULL == root)
	{
		printf("root is null");
	}

	memset(&stStack, 0, sizeof(TREE_NODE_STACK_S));



	while(pstRoot)
	{


	}


	return;
}

int main()
{
    printf("Hello world!\n");
    return 0;
}
