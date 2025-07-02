#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int data;

	scanf("%d", &data);

	for (int i = 0; i < data / 4; i++)
		printf("long ");

	printf("int");

	return 0;
}