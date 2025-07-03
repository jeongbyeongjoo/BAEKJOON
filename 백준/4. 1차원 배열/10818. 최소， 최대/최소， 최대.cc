#include <stdio.h>

int main()
{
	int n, data, max, min;

	scanf("%d", &n);
	scanf("%d", &max);
	min = max;

	for (int i = 1; i < n; i++)
	{
		scanf("%d", &data);
		if (max < data)
			max = data;
		if (min > data)
			min = data;
	}

	printf("%d %d", min, max);

	return 0;

}