#include <stdio.h>
#include <math.h>
#include "dragonPole.h"

void dragonpoleMain();
int calcBattlePoint(int *selection);
void calc_cost();
void sort_cost();
void dispData();

int main(void)
{
  int i,j;
  int point;
  int selection[ITEM];

  /* システム初期化 */
  dragonpoleMain();

  /* 初期化 (技をすべて0にする) */
  for (i=0; i<ITEM; i++) {
    selection[i] = 0;
  }

  /* 技を選択 (ここでは，0, 4, 8の技を選択した)*/
  calc_cost();
  sort_cost();
  dispData();
  for(i = 0;i < ITEM;i++){
    selection[i] = 1;
    if(calcBattlePoint(selection) == 5)selection[i] =0;
  }
  /* 戦闘力を計測 (スカウターのこと) */
  point = calcBattlePoint(selection);
  printf("point = %d\n",point);
  return 0;
}
