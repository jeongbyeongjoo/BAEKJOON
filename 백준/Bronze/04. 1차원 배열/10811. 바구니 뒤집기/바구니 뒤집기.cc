#include <stdio.h>

int main(void) {

	int  n, m;
	int a[100];

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++)
		a[i] = i + 1;

	int i, j, tmp;

	for (int k = 0; k < m; k++)
	{
		scanf("%d %d", &i, &j);
		for (; i < j; i++)
		{
			tmp = a[i - 1];
			a[i - 1] = a[j - 1];
			a[j - 1] = tmp;
			j--;
		}
	}

	for (int i = 0; i < n; i++)
		printf("%d ", a[i]);



	return 0;
}
