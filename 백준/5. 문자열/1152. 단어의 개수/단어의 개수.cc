#include <stdio.h>
#include <string.h>

int main() {
	int cnt = 0, flag=1;
	char c;

	c = getchar();

	if (c == 32) 
		flag = 0;

	while (1){
		c = getchar();
		if (c == 32){
			flag = 0;
			cnt += 1;
			continue;
		}
		if (c == 10) {
			if (flag)
				cnt += 1;
			break;
		}
		flag = 1;
	}

	printf("%d", cnt);

	return 0;
}