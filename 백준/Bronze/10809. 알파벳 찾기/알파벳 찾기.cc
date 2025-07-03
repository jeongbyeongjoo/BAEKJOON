#include <stdio.h>
#include <string.h>

int main(void) {

	char str[100];

	scanf("%s", str);

	int arr[26];

	for (int i = 0; i < 26; i++)
		arr[i] = -1;

	for (int i = strlen(str) - 1; i >= 0; i--)
		arr[str[i] - 97] = i;

	for (int i = 0; i < 26; i++)
		printf("%d ", arr[i]);

	return 0;
}

