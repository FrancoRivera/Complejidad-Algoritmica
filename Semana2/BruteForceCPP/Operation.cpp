//
// Created by Franco Rivera Rivas on 8/22/17.
//

#include "Operation.h"
int Operation::sumRec(int *v, int minVal, int maxVal){
    if (minVal<=maxVal){
        return (v[minVal]);
    }
    int sumTotal = minVal+sumRec(v, minVal+1, maxVal);
    return sumTotal;
}

int Operation::sum(int n) {
    if (n<=0) return 0;
    else{
        int suma = n + sum(n-1);
        return suma;
    }

}

int Operation::mul(int n) {
    if (n<=1) return 1;
    else{
        int total = n * mul(n-1);
        return total;
    }
};


