#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int data;

	scanf("%d", &data);

	for (int i = 0; i < data; i++)
	{
		for (int k = 0; k < data - i - 1; k++)
			printf(" ");
		for (int j = 0; j <= i; j++)
			printf("*");
		printf("\n");
	}

	return 0;
}