#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<vector>

using namespace std;

#define MEAN 1
#define MATCHNUM 100 //number of matches tested

vector <double> FSig, FSigX, Alpha;
vector <int> NUM; // number of players

main(){
    freopen("DataIn.in","r",stdin);
    double Exp = 0, E, A;
    int num;

    for( int i = 0 ; i < MATCHNUM; i++){
        scanf("%d",&num);
        scanf("%lf", &A);
        NUM.push_back(num);
        FSig.push_back(A);
    }


    for( int i = 0 ; i < MATCHNUM; i++){
        scanf("%lf", &E);
        Alpha.push_back(E);
        FSigX.push_back( (pow(FSig[i] , MATCHNUM) ) * exp(E) / 1.5);
    }

    sort (FSigX.begin(),FSigX.end());
    
    for( int i = 0 ; i < MATCHNUM; i++)
         printf(“%lf\n”,FSigX[i]);


    for( int i = 0 ; i < MATCHNUM; i++){
        double MaxSig = sqrt(2 * (-Alpha[i]*2*FSig[i]*FSig[i]) / NUM[i]);
        double T = 0.1285 * MaxSig + 1; //Threshold performance value
        printf("%lf\n",T);
    }
}
