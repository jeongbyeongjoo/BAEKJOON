#include <stdio.h>

int main(void)
{
	int data, data1;
	int a, b, c;

	scanf("%d", &data);
	scanf("%d", &data1);
	a = data1 / 100;
	b = (data1 / 10) % 10;
	c = data1 % 10;

	printf("%d\n", data * c);
	printf("%d\n", data * b);
	printf("%d\n", data * a);
	printf("%d", data * data1);

	return 0;
} 