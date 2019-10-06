/*
In this question, you are given two positive integers M and N, where M
< N. You may assume that N is less than or equal to 100.

The orbit of M with respect to N is defined to be the sequence

M, (2*M) mod N, (2^2*M) mod N, ...

There are at most N elements in the sequence, but for some M, the
number of elements in this sequence may be fewer.

You have to output the maximum number of distinct integers in the
orbit of M.


For example, if M=5 and N=8, then the orbit of 5 with respect to 8 is

5, 2*5 mod 8, 4*5 mod 8, 8*5 mod 8

which is equal to

5, 2, 4, 0.

Hence the number of distinct integers in the orbit of 5 is 4.
*/

#include<stdio.h>
int modulo(int ,int ,int);
int main()
{
	int M,N,size=0;
	scanf("%d",&M);
	scanf("%d",&N);
	int multi,ans=1,index=1,count=0;
	int array[index];
	if(M < N){
		while(multi < N){
			multi=1;
			for (int i = 0; i < count; i++){
				multi = multi*2;
			}
			// ans = modulo(M,N,count);
			ans = (multi*M)%N;
			array[index-1]=ans;
			index++;
			count++;
		}
		// for(int i=0;i<index-1;i++){
		// 	printf("%d, ",array[i]);
		// }
		size = index-1;
		for(int i = 0; i < size; i++){
        	for(int j = i+1; j < size; ){
            	if(array[j] == array[i]){
                	for(int k = j; k < size; k++){
                    	array[k] = array[k+1];
                	}
                	size--;
            	}
            	else{
                	j++;
            	}
        	}
    	}
		printf("%d",size);
	}
	else{
		printf("%d",size);
	}
	return 0;
}

// int modulo(int M,int N, int count)
// {
// 	int multi=1;
// 	for (int i = 0; i < count; i++){
// 		multi = multi*2;
// 	}
// 	return (multi*M)%N;
// }