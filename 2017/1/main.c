

#include <stdio.h>
#include <stdlib.h>



void read_input(void){
    FILE  *fp;
    char ch;
    int counter=0;

    fp = fopen("./input.prod", "r");
    while ((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
        counter++;
    }
    fclose(fp);


    fp = fopen("./input.prod", "r");
    int digits[counter];
    for (int i=0; i<counter; i++){
        digits[i] = fgetc(fp) - '0';
    }
    fclose(fp);

    int running_total = 0;

    for (int i=0; i<counter-1; i++){
        int j = (i+ counter/2) % (counter-1);
        /*printf("%d, %d\n", i, j);*/
        /*printf("%d, %d\n", digits[i], digits[j]);*/
        if (digits[i]== digits[j]){
            /*printf("HIT");*/
            running_total= running_total + digits[i];
        }
    }
    printf("%d\n", running_total);



}

void main(void){
    read_input();
}
