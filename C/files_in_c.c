#include <stdio.h>
#include <stdlib.h>

FILE *try_open(char *file_name, char *open_mode);
void read_file(FILE *arq);
void write_file(char *str, FILE *fout);

//------------------------------------------------------------------------------------


//________________________try_open________________________
FILE *try_open(char *file_name, char *c){
  FILE *arq;
  arq = fopen(file_name, c);

  if(arq==NULL){
    printf("failure to open file: %s'\n",file_name);
    exit(EXIT_FAILURE);
  }
  else{
    return arq;
  }
}


//________________________read_file________________________
void read_file(FILE *arq){
  int c;
  while((c=fgetc(arq))!=EOF){
    printf("%u", c);
  }
}


//________________________write_file________________________
void write_file(char *str, FILE *fout){
  
}

//________________________main________________________
void main(int argc, char **argv){
  FILE *arq;

  if(argc!=3){
    printf("Sintaxe: \n\n%s [file] [open mode]\n\n", argv[0]);
    exit(EXIT_FAILURE);
  }
  
  arq = try_open(argv[1], argv[2]);
  read_file(arq);
  fclose(arq);
}

