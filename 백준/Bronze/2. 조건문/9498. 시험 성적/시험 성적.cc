#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int data;

	scanf("%d", &data);

	if (data >= 90)
		printf("A");
	else if (data >= 80)
		printf("B");
	else if (data >= 70)
		printf("C");
	else if (data >= 60)
		printf("D");
	else
		printf("F");

	return 0;
}