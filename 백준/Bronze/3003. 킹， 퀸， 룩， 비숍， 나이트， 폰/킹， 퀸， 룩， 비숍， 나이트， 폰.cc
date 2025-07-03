#include <stdio.h>

int main() {
	int arr[6] = { 1,1,2,2,2,8 };
	int data;

	for (int i = 0; i < 6; i++) {
		scanf("%d", &data);
		printf("%d ", arr[i] - data);
	}

	return 0;
}