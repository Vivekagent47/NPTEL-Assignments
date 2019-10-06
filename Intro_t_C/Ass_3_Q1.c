/*Write a C function to find the kth occurrence of an even integer in a sequence of non-negative integers, and then call your function from main. 

Your function should be according to the following declaration:

int find_even(int k);

Input
You are given the input in two lines:

The first line contains a positive integer k. 
In the second line, you will be given a sequence of numbers. 

You have to find the kth occurrence of n in the sequence below. 

The second line consists of a sequence of non-negative integers,
terminated with a -1.  The -1 is not part of the sequence.

Output
If there are  k even numbers in the sequence, then output the  kth
occurrence of even in the sequence. Otherwise, output a -1.


Sample Input
2
1 1 3 2 3 4 1 -1

Sample Output
4
*/

#include<stdio.h>
int find_even(int);
int main()
{
    int a,k;
    scanf("%d",&k);
    a=find_even(k);
    printf("%d",a);
    return 0;
}

int find_even(int j){
    int n,count=0,even=0;
    while(1){
        scanf("%d",&n);
        if(n == -1)
            break;
        else{
            if(n%2 == 0){
                count++;
                even++;
                if(even == j)
                    return n;
            }
            else
                count++;
        }
    }
    if(even == 0)
        return n;


