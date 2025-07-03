#include <stdio.h>

int main()
{
	int n, m, i, j, tmp;
	int a[100];

	scanf("%d %d", &n, &m);

	for (int k = 0; k < n; k++)
		a[k] = k + 1;

	for (int k = 0; k < m; k++)
	{
		scanf("%d %d", &i, &j);
		tmp = a[i-1];
		a[i-1] = a[j-1];
		a[j-1] = tmp;
	}

	for (int k = 0; k < n; k++)
		printf("%d ", a[k]);

	return 0;
}