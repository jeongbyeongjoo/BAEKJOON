#include <stdio.h>

int main(void) 
{
	char str[1000];
	int data;

	scanf("%s", str);
	scanf("%d", &data);

	printf("%c", str[data-1]);
	

	return 0;
}
