#include <stdio.h>

int main(void)
{
	double a;
	double b;

	scanf("%lf %lf", &a, &b);

	printf("%.9f", a / b);

	return 0;
} 