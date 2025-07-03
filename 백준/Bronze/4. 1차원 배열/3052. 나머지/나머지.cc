#include <stdio.h>
#include <math.h>

int main()
{
	int data;
	int b[10], a[10];

	for (int i = 0; i < 10; i++)
	{
		scanf("%d", &data);
		a[i] = data % 42;
		b[i] = 1;
	}

	for (int i = 0; i < 10; i++)
		for (int j = 0; j < 10; j++)
		{
			if (i == j)
				continue;
			if (a[i] == a[j])
				b[i] += 1;
		}

	double cnt = 0;

	for (int i = 0; i < 10; i++)
		for (int j = 1; j <= 10; j++)
			if (b[i] == j)
				cnt += b[i] / pow(j, 2);

	printf("%.f", cnt);

	return 0;
}