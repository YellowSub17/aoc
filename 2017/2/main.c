

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdbool.h>


char *readFile(char *filename) {
    FILE *f = fopen(filename, "rt");
    assert(f);
    fseek(f, 0, SEEK_END);
    long length = ftell(f);
    fseek(f, 0, SEEK_SET);
    char *buffer = (char *) malloc(length + 1);
    buffer[length] = '\0';
    fread(buffer, 1, length, f);
    fclose(f);
    return buffer;
}



void main(void){


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
    printf("%d\n", nrows);
    printf("%d\n", nele);
    ncols = nele / nrows;

    int table[nrows][ncols];
    int i=0;
    int j=0;
    FILE *fp2 = fopen("./input.prod","r");
    while (feof(fp2) != true){

        fgets(row, MAXCHAR, fp2);
 

        token = strtok(row, "\t");
        /*printf("%d, %d, %s\n", i, j, token);*/
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

    int r=3;
    int c=6;

    printf("%s", "xxx\n");
    printf("%d, %d, %d\n", r, c,  table[r][c]);
    printf("%s", "xxx\n");




 





}
    








    /*char *found1;*/
    /*char *content1 = readFile("./input.prod");*/
    /*while (( found1 = strsep(&content1, "\t")) != NULL){*/
        /*nele++;*/
    /*}*/

    /*char *found2;*/
    /*char *content2 = readFile("./input.prod");*/
    /*while (( found2 = strsep(&content2, "\n")) != NULL){*/
        /*nrows++;*/
    /*}*/

    /*ncols = nele / nrows;*/

    /*printf("nele=%d\n", nele);*/
    /*printf("nrows=%d\n", nrows);*/
    /*printf("ncols=%d\n", ncols);*/

    /*char *table[nrows][ncols];*/

    /*char *found3;*/
    /*char *content3 = readFile("./input.prod");*/
    /*int i=0;*/
    /*int j=0;*/
    /*int counter = 0;*/
    /*while (( found3 = strsep(&content3, "\t")) != NULL){*/

        /*table[j][i] = found3;*/
        /*counter++;*/

        /*i++;*/
        /*if (i==16){*/
            /*i=0;*/
            /*j++;*/
        /*}*/


    /*}*/

    /*int r = 2;*/
    /*int c = 0;*/
    /*printf("%s\n", "xxxx");*/
    /*printf("%s\n", table[r][c]);*/
    /*printf("%s\n", "xxxx");*/


    
    /*for (int i; i<241; i++){*/
        /*found = strsep(&content1, "\t");*/
        /*printf("%s..", found);*/
        /*if (i % 16 ==0){*/
            /*printf("%s", "..");*/
        /*}*/
    /*}*/




    /*while  ((found = strsep(&content1, "\t")) != NULL ){*/
        /*nele++;*/
    /*} */

    /*printf("%d\n", nele);*/


    /*while  ((found = strsep(&content1, "\n")) != NULL ){*/
        /*nrows++;*/
    /*} */

    /*char *content2 = readFile("./input.prod");*/
    /*while  ((found = strsep(&content2, "\t")) !=NULL ){*/
        /*nele++;*/
    /*}*/

    /*printf("%d\n", nrows);*/
    /*printf("%d\n", nele);*/

    /*ncols = */


/*    while  ((found = strsep(&content, "\t")) !=NULL ){*/
        /*printf("%sxx", found);*/
    /*} */


    /*printf("%s", content);*/




