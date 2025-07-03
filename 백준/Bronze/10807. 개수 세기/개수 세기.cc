#include <stdio.h>


int main()
{
	int n, data, sum = 0;
	int str[100];

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		scanf("%d", &str[i]);
	
	scanf("%d", &data);

	for (int i = 0; i < n; i++)
		if (data == str[i])
			sum += 1;

	printf("%d", sum);

	return 0;
}