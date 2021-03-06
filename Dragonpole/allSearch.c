#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "dragonPole.h"

void dragonpoleMain();
int calcBattlePoint(int *selection);

int main(void)
{
  int i,j;
  int point;
  int max_point, max_index;
  int selection[ITEM];
  int selection_tmp[ITEM];

  /* システム初期化 */
  dragonpoleMain();

  /* 初期化 (技をすべて0にする) */
  for (i=0; i<ITEM; i++) {
    selection[i] = 0;
  }

  max_index = 0;
  max_point = 0;
  /* 技を選択 (ここでは，0, 4, 8の技を選択した)*/
  for(i = 0;i < pow(2,ITEM)-1;i++){
    // 各ビットを入れる
    for(j = 0;j < ITEM;j++){
      selection[j] = (i >> j) & 0x01;
    }
    // 最大値を記憶
    point = calcBattlePoint(selection);
    if(max_point < point){
      max_point = point;
      max_index = i;
      printf("max_val : %d\n",max_point);
    }
  }

  /* 戦闘力を計測 (スカウターのこと) */
  // 値の再現
  for(j = 0;j < ITEM;j++){
    selection[j] = (max_index >> j) & 0x01;
  }
  point = calcBattlePoint(selection);
  // 表示
  printf("戦闘力は%d\n", point);
  for(j = 0;j < ITEM;j++){
    printf("%d",selection[j]);
  }
  printf("\n");

  return 0;
}
