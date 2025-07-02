#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int data;

	scanf("%d", &data);

	if (data % 4 == 0 && (data % 400 == 0 || data % 100 != 0))
		printf("1");
	else
		printf("0");

	return 0;
}