/*You are given a sequence of non-negative integers terminated by -1. You have to output 1 if there are atleast 2 distinct elements in the sequence and 0 if the sequence consists of only 1 integer. Note that -1 is not part of the sequence. The sequence is not necessarily sorted. 

Note: Don't use arrays to this question. 
*/

#include<stdio.h>
int main()
{
  int a,count=0,prv=0;
  while(1){
    scanf("%d",&a);
    if( a == -1)
      break;
    if(prv != a)
      count++;
    prv= a;
  }
  if(count >= 2)
    printf("1");
  else
    printf("0");
  return 0;
}