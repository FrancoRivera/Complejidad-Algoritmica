#include <iostream>
using namespace std;

class Finder{
public:
    int MaxValue(int *a, int l, int r){
        if(r-l == 1) return a[l];
        int m = (l+r)/2;
        int u = MaxValue(a, l, m);
        int v = MaxValue(a, m, r);
        return u>v?u:v;

    }
};


class QuickSort{
public:
    void swap(int*a, int*b){
        int t = *a;
        *a = *b;
        *b = t;
    }
    int partition(int arr[], int l, int h){
        int x = arr[h];
        int i = (l-1);

        for (int j = l;j<=h-1;j++)
    }
};
int main() {

    std::cout << "Hello, World!" << std::endl;
    return 0;
}


class 
