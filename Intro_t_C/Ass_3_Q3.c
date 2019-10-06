/*A line of English text will be given, where words are separated by one
of the following symbols:

 ' ', '\t', '.', ',' and ';'

Each word may be separated from the next and the previous by one or
more of the following symbols. You have to count the number of words
in the sentence.

Note that to read the input, you have to read until the EOF symbol is
read, as in the following example.

int main()
{
    int c;
   
    c = getchar();
    while ( c != EOF ) {
       c = getchar();
    }
    return 0;
}

Note: it is possible to solve this question without arrays, so the
maximum length of the line is not important.

Input
-----
A line of English text with words separated from one another by one or
more occurrences of the symbols

 ' ', '\t', '.', ',' and ';'

Output
------
The number of words in the line.

Sample Input
------------
This is a sentence, it has words separated by spaces and fullstops.

Sample Output
-------------
12
*/

#include <stdio.h>
void consume_space()
{
    int c;
    c = getchar();
    while(1){
        switch(c){
            case ' ':
            case '\t':
            case '.':
            case ',':
            case ';':
                c = getchar();
                continue;
            default:
                ungetc(c,stdin);
            return;
        }
    }
 }
int is_space(int c)
{
    switch(c){
        case ' ':
        case '\t':
        case '.':
        case ',':
        case ';':
            return 1;
        default:
            return 0;
    }
}
 
int main()
{
    int c;
    int count=0;
    c = getchar();
    while ( c != EOF ){
        if ( is_space(c) ){
            count++;
            consume_space();
        }
        c = getchar();
    }
    printf("%d", count);
    return 0;
}