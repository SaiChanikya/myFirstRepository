#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LENGTH 100

void create(FILE *fpFields, FILE *fpData) 
{
    fpFields = fopen("Fields.cfg", "r");
    char fields[LENGTH];
    fpData = fopen("data.dat", "a");
    while(fgets(fields, sizeof(fields), fpFields) != NULL)
    {
        fields[strlen(fields) - 1] = '\0';
        printf("Enter the %s: ", fields);
        fflush(stdin);       
        gets(fields);
        fprintf(fpData, "%s ", fields);
    }
    fprintf(fpData, "\n");
    fclose(fpData);
    fclose(fpFields);
}

void read(FILE *fpData) 
{
    fpData = fopen("data.dat", "r");
    char data[LENGTH];
    while(fgets(data, sizeof(data), fpData) != NULL) 
    {
        puts(data);
    }
    fclose(fpData);
}

int showMainMenu(FILE *fpPointer, FILE *fpField, FILE *fpData) 
{
    fpPointer = fopen("Menu.cfg", "r");
    char menu[LENGTH];
    int option;
    while(fgets(menu, sizeof(menu), fpPointer) > 0 ) 
    {     
        printf("%s", menu);
    }
    while(1)
    {
        printf("\nEnter the option: ");
        scanf("%d", &option);
        switch(option) 
        {
            case 1 : 
                create(fpField, fpData);
                break;
            case 2 : 
                read(fpData);
                break;
            case 3 : 
                printf("Thank you.");
                exit(1);
                break;
            default:
                printf("\nInvalid option!");
                break;
        }
    }
    fclose(fpPointer);
    return 0;
}


FILE *fpFields;
FILE *fpPointer;
FILE *fpData;
int main ()
{
    showMainMenu(fpPointer, fpFields, fpData);
    return 0;
}
