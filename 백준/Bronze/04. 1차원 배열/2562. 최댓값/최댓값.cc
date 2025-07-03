#include <stdio.h>

int main()
{
	int data, max=1, index;

	for (int i = 0; i < 9; i++)
	{
		scanf("%d", &data);
		if (max < data)
		{
			max = data;
			index = i;
		}
	}

	printf("%d\n", max);
	printf("%d", index+1);
	

	return 0;

}