#include <stdio.h>
#include <math.h>
#include<stdlib.h>

int isprime(int n);


int isprime(int n){
  unsigned int cont;
  if(n==2) return 1;
  if(n%2==0) return 0;
  for(cont=3;cont<=pow(n,0.5);cont=cont+2){
    if(n%cont==0){
      return 0;
    }
  }
  return 1;
}



int main(int argc, char *argv[]) {
  int n,a, cont;
  if(argc == 1){
      printf("Sintaxe correta: Soma param1 param2 ...");
      exit(1);
  }
  for(cont=1;cont<argc;cont++){
    int n = atoi(argv[cont]);
    if(!isprime(n))
      printf("%d Is Not Prime\n", n);
  
    else
      printf("%d Is Prime\n", n);
  
  }
}
