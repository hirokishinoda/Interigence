#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "dragonPole.h"

#define LOOP 10000

void dragonpoleMain();
int calcBattlePoint(int *selection);

int main(void)
{
  int i,j;
  int point;
  int max_point;
  int selection[ITEM];

  srand((unsigned)time(NULL));

  /* システム初期化 */
  dragonpoleMain();

  /* 初期化 (技をすべて0にする) */
  for (i=0; i<ITEM; i++) {
    selection[i] = 0;
  }

  max_point = 0;
  /* 技を選択 (ここでは，0, 4, 8の技を選択した)*/
  for(i = 0;;i++){
    // 各ビットを入れる
    for(j = 0;j < ITEM;j++){
      selection[j] = rand()%2;
    }
    // 最大値を記憶
    point = calcBattlePoint(selection);
    if(max_point < point){
      max_point = point;
      printf("max_val : %d\n",max_point);

    }
  }

  return 0;
}
