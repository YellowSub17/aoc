

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int twonp1s(int n){
    return (2*n+1)*(2*n+1);
}

int square_size(int pos){
    int n=0;
    while (((2*n+1)*(2*n+1)) <= pos){
        n++;
    };
    return (2*n+1);

}

int unwrap(int ss, int pos){

    int max_pos = (ss)*(ss);

    int bot_l = max_pos - ss + 1;
    int top_l = bot_l - ss + 1;
    int top_r = top_l - ss + 1;
    int min_pos = (ss-2)*(ss-2) +1;


    int bot = max_pos - (ss - 1 )/2;
    int left = bot_l - (ss - 1 )/2;
    int top = top_l - (ss - 1 )/2;
    int right = top_r - (ss - 1 )/2;

    int x =0;
    int y =0;

    if (pos >max_pos) {
        return -1;
    } else if (pos >= bot_l){
        y= (ss -1)/2;
        x = abs(pos - bot);
    } else if ( pos >= top_l){
        x= (ss -1)/2;
        y = abs(pos - left);
    } else if (pos >= top_r) {
        y= (ss -1)/2;
        x = abs(pos - top);
    } else if (pos >= min_pos){
        x= (ss -1)/2;
        y = abs(pos - right);
    } else {
        return -1;
    }

    return x + y;


}


int main(void){

    int input = 289326;

    int ss = square_size(input);

    int d = unwrap(ss, input);

    printf("PART 1: %d\n", d);


    int array[ss][ss];
    int i = (ss-1)/2;
    int j = (ss-1)/2;

    array[i][j]= 1;






    



    return 0;
}


