#include <stdio.h>
#include <string.h>

int main(void)
{
	int n;
	char str[100];

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%s", str);
		printf("%c%c\n", str[0], str[strlen(str) - 1]);	
	}

	return 0;
}
