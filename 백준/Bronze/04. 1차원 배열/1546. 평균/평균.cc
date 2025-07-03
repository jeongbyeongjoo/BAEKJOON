#include <stdio.h>

int main(void)
{
	int n;
	double data[1000];

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		scanf("%lf", &data[i]);

	double max = 0;

	for (int i = 0; i < n; i++)
		if (max < data[i])
			max = data[i];

	double sum = 0;

	for (int i = 0; i < n; i++)
		sum += data[i] / max * 100;

	printf("%lf", sum / n);

	return 0;
}
