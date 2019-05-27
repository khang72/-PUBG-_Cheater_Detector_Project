#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<vector>

using namespace std;

#define MEAN 1
#define MATCHNUM 100

vector <double> FSig, FSigX;

main(){
    freopen("DataIn.in","r",stdin);
    double Exp = 0, E, A;

    for( int i = 0 ; i < MATCHNUM; i++){
        scanf("%lf", &A);
        //printf("%lf\n",A);
        FSig.push_back(A);
    }


    for( int i = 0 ; i < MATCHNUM; i++){
        scanf("%lf", &E);
        //printf("%lf\n",1/(pow(FSig[i] , MATCHNUM) ));
        FSigX.push_back( (pow(FSig[i] , MATCHNUM) ) * exp(E) / 1.5);
    }


    for( int i = 0 ; i < MATCHNUM; i++){
        printf("%lf \n",FSigX[i]);
    }
    sort (FSigX.begin(),FSigX.end());
}
