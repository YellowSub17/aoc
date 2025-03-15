

#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int twonp1s(int n){
    return (2*n+1)*(2*n+1);
}

int square_size(int pos){
    int n=1;
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

    /*int input = 289326;*/
    /*int ss = square_size(input);*/
    /*int d = unwrap(ss, input);*/
    /*printf("PART 1: %d\n", d);*/


    /*int input = 747;*/
    /*int ss = square_size(input);*/
    int ss = 7;

    int data[ss][ss];
    memset( data, 0, ss*ss*sizeof(int) );

    /*int x_sign = 1;*/
    /*int y_sign = 0;*/
    int L = 1;

    int signs[4] = {0, 1, 0, -1};
    /*int signs[4] = {5, 9, 5, 1};*/

    int x_moves[ss*ss];
    int y_moves[ss*ss];
    memset( x_moves, 0, ss*ss*sizeof(int) );
    memset( y_moves, 0, ss*ss*sizeof(int) );

    int counter = 0;
    int mod4_counter = 0;

    while (counter + 2*L < ss*ss){

        for (int l=0; l<L; l++){

            y_moves[counter+l] = signs[mod4_counter%4];
            x_moves[counter+l] = signs[(mod4_counter+1)%4];
        }
        counter= counter +L;
        mod4_counter++;

        for (int l=0; l<L; l++){
            y_moves[counter+l] = signs[mod4_counter%4];
            x_moves[counter+l] = signs[(mod4_counter+1)%4];
        }
        counter= counter +L;
        mod4_counter++;
        L++;

    }


    printf("x: %s", "\n");
    for (int s=0; s<ss*ss; s++){
        printf("%d", x_moves[s]);
    }
    printf("%s", "\n");


    printf("y: %s", "\n");
    for (int s=0; s<ss*ss; s++){
        printf("%d", y_moves[s]);
    }
    printf("%s", "\n");



    
    /*printf("%d %d\n", i, j);*/


    for (int posx=1;posx<15; posx++){

        int i = (ss-1)/2;
        int j = (ss-1)/2;
        data[i][j] = 1;


        for (int pos=0; pos<posx; pos++){

            i = i + x_moves[pos];
            j = j + y_moves[pos];
            /*printf("i=%d j=%d ymoves[pos]=%d xmoves[pos]=%d\n", i, j, y_moves[pos], x_moves[pos]);*/
            data[i][j] = (pos+2) % 10;
        }

        for (int ii = 0; ii<ss; ii++){
            for (int jj = 0; jj<ss; jj++){
                printf("%d ", data[ii][jj]);
            }
            printf("%s", "\n");
        }

        printf("%s", "\n");

    }






    



    return 0;
}


