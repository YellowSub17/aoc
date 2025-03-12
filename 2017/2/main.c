

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdbool.h>





void part2(void){

    int ncols = 0;
    int nrows = -1;
    int nele = -1;
    
    int MAXCHAR = 1000;
    char row[MAXCHAR];
    char* token;
    

    FILE *fp1 = fopen("./input.prod","r");
    while (feof(fp1) != true){
        fgets(row, MAXCHAR, fp1);
        /*printf("Row: %s", row);*/

        nrows++;

        token = strtok(row, "\t");

        while(token != NULL){
            /*printf("Token: %s\n", token);*/
            token = strtok(NULL, "\t");
            nele++;
        }

    }
    /*printf("%d\n", nrows);*/
    /*printf("%d\n", nele);*/
    ncols = nele / nrows;

    int table[nrows][ncols];
    int i=0;
    int j=0;
    FILE *fp2 = fopen("./input.prod","r");
    while (feof(fp2) != true){

        fgets(row, MAXCHAR, fp2);

        token = strtok(row, "\t");
        /*printf("%d, %d, %s\n", i, j, token);*/
        table[i][j] = atoi(token);
        j++;

        while(token != NULL){
            token = strtok(NULL, "\t");
            /*printf("%d, %d, %s\n", i, j, token);*/
            table[i][j] = atoi(token);
            j++;

            if (j==16){
                break;
            }
        }

        j=0;
        i++;

        if (i==16){
            break;
        }
    }



    

    int checksum = 0;
    for (int r=0; r<nrows; r++){


        for (int div1_ind=0; div1_ind <ncols;div1_ind++){

            for (int div2_ind = 0; div2_ind <ncols; div2_ind++){


                int div1 = table[r][div1_ind];
                int div2 = table[r][div2_ind];

                if (div1 <= div2){continue;}


                if (div1 % div2 == 0){
                    /*printf("(%d, %d): %d / %d = %d rem %d\n", div1_ind, div2_ind, div1, div2, div1/div2, div1 % div2);*/
                    checksum = checksum + (div1/div2);
                }



            }


        }

    }
    printf("Checksum: %d\n", checksum);



}



void part1(void){


    int ncols = 0;
    int nrows = -1;
    int nele = -1;
    
    int MAXCHAR = 1000;
    char row[MAXCHAR];
    char* token;
    

    FILE *fp1 = fopen("./input.prod","r");
    while (feof(fp1) != true){
        fgets(row, MAXCHAR, fp1);
        /*printf("Row: %s", row);*/

        nrows++;

        token = strtok(row, "\t");

        while(token != NULL){
            /*printf("Token: %s\n", token);*/
            token = strtok(NULL, "\t");
            nele++;
        }

    }
    /*printf("%d\n", nrows);*/
    /*printf("%d\n", nele);*/
    ncols = nele / nrows;

    int table[nrows][ncols];
    int i=0;
    int j=0;
    FILE *fp2 = fopen("./input.prod","r");
    while (feof(fp2) != true){

        fgets(row, MAXCHAR, fp2);

        token = strtok(row, "\t");
        /*printf("%d, %d, %s\n", i, j, token);*/
        table[i][j] = atoi(token);
        j++;

        while(token != NULL){
            token = strtok(NULL, "\t");
            /*printf("%d, %d, %s\n", i, j, token);*/
            table[i][j] = atoi(token);
            j++;

            if (j==16){
                break;
            }
        }

        j=0;
        i++;

        if (i==16){
            break;
        }
    }


    int checksum = 0;

    for (int r=0; r<nrows; r++){
        int rowmin = 99999;
        int rowmax = -1;

        for (int c=0; c<ncols; c++){
            if (table[r][c] > rowmax){
                rowmax = table[r][c];
            }
            if (table[r][c] < rowmin){
                rowmin = table[r][c];
            }
        }

        int rowdiff = rowmax - rowmin;
        checksum = checksum + rowdiff;

    }

    printf("Checksum: %d\n", checksum);

}
    



void main(void){
    part1();
    part2();
}
