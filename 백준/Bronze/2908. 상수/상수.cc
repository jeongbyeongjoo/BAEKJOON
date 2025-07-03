#include <stdio.h>
#include <stdlib.h>

int main() {
	char s1[4], s2[4], tmp;
	int int_s1, int_s2;

	scanf("%s %s", s1, s2);

	tmp = s1[0];
	s1[0] = s1[2];
	s1[2] = tmp;

	tmp = s2[0];
	s2[0] = s2[2];
	s2[2] = tmp;

	int_s1 = atoi(s1);
	int_s2 = atoi(s2);

	if (int_s1 > int_s2)
		printf("%d", int_s1);
	else
		printf("%d", int_s2);

	return 0;
}