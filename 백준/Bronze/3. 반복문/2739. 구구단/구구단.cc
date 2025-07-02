#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int data;

	scanf("%d", &data);

	for (int i = 1; i < 10; i++)
		printf("%d * %d = %d\n", data, i, data * i);

	return 0;
}