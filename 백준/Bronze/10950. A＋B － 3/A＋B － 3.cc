#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int data, a, b;

	scanf("%d", &data);

	for (int i = 1; i < data + 1; i++)
	{
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}

	return 0;
}