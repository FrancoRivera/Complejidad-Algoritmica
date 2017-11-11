//
// Created by Franco Rivera Rivas on 8/22/17.
//

#include "StringMatching.h"

int StringMatching::findMatch(char *a, char *b, int n, int m) {
        int k, i, j, band=0;
        for(i=0;i<=n-m;i++){
            k=i; j = 0;
            while(a[k]==b[j] &&j<=m){
                k++;j++;
            }
            if(j>m-1){
                cout<<"Value at position => "<< i+1 << endl; band=1;
            }
            else band = 0;

        }
        if (band==0) cout << "Value not found. ";

}

string StringMatching::StringScanner(string str, int n) {
    int estado = 0;
    for (int i = 0; i <n ; ++i) {
        if (str[i] == 'a' && (estado==1 || estado==0))
            estado = 1;
        else if (str[i] == 'b' && (estado==1 || estado ==2))
            estado = 2;

        else estado = -1;

    }

    return (estado == 2 ? "Valido" : "no valido");

}
