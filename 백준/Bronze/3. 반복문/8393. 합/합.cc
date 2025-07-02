#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int data, sum = 0;

	scanf("%d", &data);

	for (int i = 1; i < data + 1; i++)
		sum += i;

	printf("%d", sum);

	return 0;
}