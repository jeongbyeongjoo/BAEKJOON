#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int data;

	scanf("%d", &data);

	for (int i = 1; i <= data; i++)
	{
		for (int j = 0; j < i; j++)
			printf("*");
		printf("\n");
	}

	return 0;
}