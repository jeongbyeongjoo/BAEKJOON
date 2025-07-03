#include <stdio.h>


int main()
{
	int n, data;
	int a[10000];

	scanf("%d %d", &n, &data);

	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);

	for (int i = 0; i < n; i++)
		if (data > a[i])
			printf("%d ", a[i]);

	return 0;
}