#include <stdio.h>
#include <stdlib.h>

int main(void){
	
	int n;
	char arr[100];

	scanf("%d", &n);
	scanf("%s", arr);

	int sum = 0;

	for (int i = 0; i < n; i++)
	{
		sum += arr[i]-48;
	}
	printf("%d", sum);

	return 0;
}
