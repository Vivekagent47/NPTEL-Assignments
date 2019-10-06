/*Find the number of distinct numbers in a given sequence. The sequence need not be sorted.


Input
The input consists of two lines.
The first line consists of a positive number N. N is at most 1000.
The second line consists of N numbers separated by spaces.

Output
The output should be the number of distinct elements in the sequence.

Sample Input
4 
1 2 3 1 


Sample Output
3
*/

#include<stdio.h>
int main()
{
  int n,i,j,count=1;
  scanf("%d",&n);
  int a[n];
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  for(i=1;i<n;i++){
    for(j=0;j<i;j++){
      if(a[i] == a[j])
        break;
    }
    if(i==j)
        count++;
  }
  printf("%d",count);
  return 0;
}