/*
In a string, a "run" is a substring with consisting of consecutive
occurrences of the same character. For example, the string
"mississippi" contains the following runs - "ss", "ss" and "pp".

In this question, given a string, you have to output the length of the
longest run in the string.

Input
-----
A string, having length at most 100. The string is guaranteed to have
at least one run.

Output
------
The length of the longest run in the string.

Sample Input
------------
abbaaacccc

Sample Output
-------------
4
*/

#include<stdio.h>
int main()
{
	char str[100];
	int i,j,k,len=0;
        // printf("Enter the string:\n");
	scanf("%s",str);
	for(i=0,k=0;str[i]!='\0';i++,k++)
	{
		if(str[i]!=str[i+1])
		{
			if(k>len)
			 len=k;
			k=0;
		}
	}
	printf("%d",len);
	return 0;
}

