/*When you keep track of stock prices, or your weight during a diet
programme, the daily prices or weights fluctuate a lot. One way to
identify the general trend is to keep track of the average over the
last 3 days, for example. This technique often smooths out the
fluctuations, and makes the trend clearer. This technique is called
"moving average".

In this question, you have to output the "moving average" of a
sequence of non-negative numbers. The moving average is the sequence
of averages of the last 3 entries. For the first 2 numbers, no average
is output.

For example, if the sequence of numbers is

a1, a2, a3, a4, a5

and k=3, then the 3-moving average is

(a3+a2+a1)/3, (a4+a3+a2)/3, (a5+a4+a3)/3.


Input
-----

The input is a sequence of non-negative floating point numbers,
terminated by a -1. The -1 is not part of the sequence. There will be
at least 3 numbers in the sequence.

Output
------
You have to output the moving average of the sequence. The output
should be printed correct to one digit after the decimal. 

Sample Input 1
--------------
70.8 70.9 71.2 70.7 70.2 -1

Sample Output 1
---------------
71.0 70.9 70.7 
*/

#include<stdio.h>
int main()
{
  float a,b,c,avg=0;
  scanf("%f",&a);
  scanf("%f",&b);
  while(1)
  {
    scanf("%f",&c);
    if(c == -1.0)
      break;
    avg= (a+b+c)/3.0;
    a=b;
    b=c;
    printf("%.1f ",avg);
  }
  return 0;
}
