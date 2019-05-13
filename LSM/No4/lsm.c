#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

struct dataset {
  double x;
  double y;
};

void inputData(struct dataset data[], int dataNumber, char filename[256])
{
  FILE *fp;
  int i;

  fp = fopen(filename, "r");
  if(fp==NULL) {
    printf("Error.\n");
    printf("Can't open file.\n");
    exit(1);
  }
  
  for(i=0; i<dataNumber; i++) {
    fscanf(fp, "%lf", &data[i].x);
    fscanf(fp, "%lf", &data[i].y);
  }
  
  fclose(fp);
}

void dispData(struct dataset data[], int dataNumber)
{
  int i;
  
  for(i=0; i<dataNumber; i++) {
    printf("%lf %lf\n", data[i].x, data[i].y);
  }

}

void create_inverse_matrix(int degree,double matrix[degree+1][degree+1],double inverse_matrix[degree+1][degree+1]){
	double inverse_m[degree+1][degree+1];
	double tmp;
	int i,j,k;

  printf("[InverseMatrix]\n");
	//単位行列を作成
	for(i = 0;i < degree+1;i++){
		for(j = 0;j < degree+1;j++){
			inverse_m[i][j] = (i==j)?1.0:0.0;
		}
	}
	//掃き出し方によって逆行列を作成
	for(i = 0;i < degree+1;i++){
		tmp = 1.0/matrix[i][i];
		for(j = 0;j < degree+1;j++){
			matrix[i][j] *= tmp;
      inverse_m[i][j] *= tmp;
		}
    for(j = 0;j < degree+1;j++){
      if(i != j){
        tmp = matrix[j][i];
        for(k = 0;k < degree+1;k++){
          matrix[j][k] -= matrix[i][k]*tmp;
          inverse_m[j][k] -= inverse_m[i][k]*tmp;
        }
      }
    }
	}
  //逆行列を指定された配列に格納し、表示する
  for(i = 0;i < degree+1;i++){
    for(j = 0;j < degree+1;j++){
      inverse_matrix[i][j] = inverse_m[i][j];
      printf("%f ",inverse_matrix[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

void create_secondmatrix(struct dataset data[],int dataNumber,int degree,double secondmatrix[degree+1]){
   int i,j,k;
   double tmp = 1.0;

  printf("[SecoundMatrix]\n");
  //掛けられる側の行列を作る
  for(i = 0;i < degree+1;i++){
    for(j = 0;j < dataNumber;j++){
        tmp = 1.0;
        for(k = 0;k < degree-i;k++){
          tmp *= data[j].x;
        }
          secondmatrix[i] += tmp*data[j].y;
    }
    printf("%f ",secondmatrix[i]);
    printf("\n");
  }
  printf("\n");
}

void calc_answer(int degree,double inverse_m[degree+1][degree+1],double secound_m[degree+1],double ans[degree+1]){
  int i,j;

  printf("[Answer]\n");
  //答えを求める(作った行列同士を掛け合わせる)
  for(i = 0;i < degree+1;i++){
    for(j = 0;j < degree+1;j++){
      ans[i] += inverse_m[i][j] * secound_m[j];
    }
    printf("%c = %.30f\n",'a'+i,ans[i]);
  }  
}

void calc_matrix(struct dataset data[],int dataNumber,int degree){
	double matrix[degree+1][degree+1];
  double inverse_matrix[degree+1][degree+1];
  double secound_matrix[degree+1];
  double answer_matrix[degree+1];
	int i,j,k,l;
  double tmp = 1.0;

  //行列の初期化
  for(i = 0;i < degree+1;i++){
    for(j = 0;j < degree+1;j++){
      matrix[i][j] = 0;
    }
  }
  printf("[OriginalMatrix]\n");
	//元になる行列を作成する
	for(i = 0;i < degree+1;i++){
		for(j = 0;j < degree+1;j++){
      for(k = 0;k < dataNumber;k++){
        tmp = 1.0;
			  for(l = 0;l < (2*degree-i-j);l++){
				  tmp *= data[k].x;
			  }
        matrix[i][j] += tmp;
      }
      printf("%4.1f ",matrix[i][j]);
		}
		printf("\n");
	}
  printf("\n");
  //逆行列を求める
  create_inverse_matrix(degree,matrix,inverse_matrix);
  //かけられる側の行列を求める
  create_secondmatrix(data,dataNumber,degree,secound_matrix);
  //最終的な結果を計算する
  calc_answer(degree,inverse_matrix,secound_matrix,answer_matrix);
}

void lsm(struct dataset data[], int dataNumber, int degree)
{
  int i;
  dispData(data, dataNumber);

  printf("\n");
  printf("$B$o$+$j$d$9$/=PNO(B\n");
  printf("(%l.20f, %l.20f)\n", data[0].x, data[0].y);
  printf("(%l.20f, %l.20f)\n", data[1].x, data[1].y);
  printf("(%l.20f, %l.20f)\n", data[2].x, data[2].y);

  /* $B$3$3$+$i:G>.Fs>hK!$N%W%m%0%i%`$r=q$/(B */
  calc_matrix(data,dataNumber,degree);
}


int main(int argc, char *argv[])
{
  struct dataset *data;
  int dataNumber;
  int degree;
  char filename[256];

  if(argc-1 != 3) {
    printf("Error.\n");
    printf("Usage: ./a.out [Data Number] [Filename] [Degree]\n");
    exit(1);
  }
  
  dataNumber = atoi(argv[1]);
  strcpy(filename, argv[2]);
  degree = atoi(argv[3]);

  data = (struct dataset *)malloc(sizeof(struct dataset)*dataNumber);

  inputData(data, dataNumber, filename);

  lsm(data, dataNumber, degree);

  return 0;
}
