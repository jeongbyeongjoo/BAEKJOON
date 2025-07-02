#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int hour, minute, data;

	scanf("%d %d", &hour, &minute);
	scanf("%d", &data);

	if (minute + data < 60)
		minute += data;
	else
	{
		hour += (minute + data) / 60;
		if (hour >= 24)
			hour -= 24;
		minute = (minute + data) % 60;
	}

	printf("%d %d", hour, minute);

	return 0;
}