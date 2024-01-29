#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int infinite_while(void);
/**
* main - starting point of program that creates 5 zombie processes
*
* Return: status code of execution always zero
*/
int main(void)
{
	int i = 0;
	int pid = 0;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid != 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}



/**
* infinite_while - infinite while
*
* Return: status code of execution
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
