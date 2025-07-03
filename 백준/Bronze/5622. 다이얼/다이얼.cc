#include <stdio.h>
#include <string.h>

int main() {
	char s[16] = " ";

	scanf("%s", s);

	int sum = 0;

	for (int i = 0; i < strlen(s); i++) {
		if ((s[i] >= 80 && s[i] <= 90)) {
			if (s[i] >= 80 && s[i] <= 83)
				sum += 8;
			else if (s[i] >= 84 && s[i] <= 86)
				sum += 9;
			else
				sum += 10;
			continue;
		}
		sum += (s[i] - 65) / 3 + 3;
	}

	printf("%d", sum);

	return 0;
}