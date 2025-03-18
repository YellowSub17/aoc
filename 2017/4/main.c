


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdbool.h>





void part1(void){

    int nrows = -1;
    int nele = -1;
    
    int MAXCHAR = 1000;
    char row[MAXCHAR];
    char* token;
    

    FILE *fp1 = fopen("./input.prod","r");
    while (feof(fp1) != true){
        fgets(row, MAXCHAR, fp1);

        nrows++;
        printf("$$%s$$\n", row);

        /*token = strtok(row, " ");*/

        /*while(token != NULL){*/
            /*printf("%s$$", token);*/
            /*token = strtok(NULL, " ");*/
            /*nele++;*/
        /*}*/


    }
    /*printf("%d\n", nrows);*/
    /*printf("%d\n", nele);*/
}
    



void main(void){
    part1();
}
