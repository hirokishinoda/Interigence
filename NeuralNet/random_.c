#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define INIT_WEIGHT 0.3

double randNum(void)
{
  return ((double)rand()/RAND_MAX-0.5)*2.0*INIT_WEIGHT;
}

int main(void){
  double wbd, wbe, wcd, wce, wab, wac;
  double offb, offc, offa;

  srand(0);

  wbd = randNum();
  wbe = randNum();
  wcd = randNum();
  wce = randNum();
  wab = randNum();
  wac = randNum();
  offb =randNum();
  offc = randNum();
  offa = randNum();

  printf("%f\n",wbd);
  printf("%f\n",wbe);

  printf("%f\n",wcd);
  printf("%f\n",wce);

  printf("%f\n",wab);
  printf("%f\n",wac);

  printf("%f\n",offa);
  printf("%f\n",offb);
  printf("%f\n",offc);

  return 0;
}
