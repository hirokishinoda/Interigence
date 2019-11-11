#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dragonPole.h"

struct item {
  int number;
  int weight;
  int money;
  double cost;
};

struct item item[ITEM];
int limit;

void dragonpoleMain(void);
void getData(void);
void dispData(void);
int calcBattlePoint(int *selection);

void dragonpoleMain()
{
  getData();
  dispData();
}

void getData(void)
{
  FILE *fp;
  char tmp[256];
  char filename[256];
  int i;

  sprintf(filename, "dragonPole%d.dat", ITEM);
  if( (fp = fopen(filename, "r"))==NULL) {
    printf("can't open error.\n");
    exit(1);
  }

  fscanf(fp, "limit=%d\n", &limit);
  fgets(tmp, 256, fp);
  for (i=0; i<ITEM; i++) {
    fscanf(fp, "%d,%d,%d\n", &item[i].number, &item[i].weight, &item[i].money);
  }

}

void dispData(void)
{
  int i;

  printf("limit=%d\n", limit);
  printf("number, weight, money, cost\n");
  for (i=0; i<ITEM; i++) {
    printf("%6d,%6d,%6d,%.6lf\n", item[i].number, item[i].weight, item[i].money , item[i].cost);
  }

}

int calcBattlePoint(int *selection)
{
  int money, weight;
  int i;

  money = weight = 0;
  for(i=0; i<ITEM; i++) {
    if(selection[i]==1) {
      weight = weight + item[i].weight;
      money = money + item[i].money;
    }
  }
  if(limit<weight) {
    money = 5;
  }

  return money;
}

void calc_cost(){
  int i;

  for(i = 0;i < ITEM;i++){
    item[i].cost = (double)(item[i].money) / item[i].weight;
  }
}

void sort_cost()
{
  int i,j;
  struct item tmp;

  for(i = 0;i < ITEM;i++){
    for(j = i;j > 0;j--){
      if(item[j].cost < item[j-1].cost){
        break;
      }else{
        tmp = item[j];
        item[j] = item[j-1];
        item[j-1] = tmp;
      }
    }
  }
}
