#include <stdio.h>

int main()
{
	int data;
	int a[30]={0};

	for (int i = 0; i < 28; i++)
	{
		scanf("%d", &data);
		a[data - 1] = 1;
	}

	for (int i = 0; i < 30; i++)
		if (a[i] == 0)
			printf("%d\n", i+1);

	return 0;
}