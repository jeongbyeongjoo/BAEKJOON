#include <stdio.h>

int main()
{
	int n, m, i, j, k;
	int a[100]={0};

	scanf("%d %d", &n, &m);
	 
	for (int l = 0; l < m; l++)
	{
		scanf("%d %d %d", &i, &j, &k);
		for (; i <= j; i++)
			a[i-1] = k;
	}

	for (int l = 0; l < n; l++)
		printf("%d ", a[l]);


	return 0;

}