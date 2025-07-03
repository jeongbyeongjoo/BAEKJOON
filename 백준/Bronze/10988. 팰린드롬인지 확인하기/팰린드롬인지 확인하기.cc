#include <stdio.h>
#include <string.h>

int main() {
	char str[100];
	int answer = 1;

	scanf("%s", str);

	for (int i = 0; i < strlen(str) / 2; i++)
		if (str[i] != str[strlen(str) - i - 1]) {
			answer = 0;
			break;
		}

	printf("%d", answer);

	return 0;
}