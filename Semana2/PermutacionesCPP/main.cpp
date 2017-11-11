#include <iostream>

using namespace std;

void permutations(string str, int i, int n){
    cout << "i=>" <<i << "     n=> " << n << endl;
    cout <<" -------------------------" << endl;
    if (i == n-1){
        cout << str << endl;
        return;
    }

    for (int j = i; j< n;j++){
        cout << "\tfor(j="<<j<<"): " <<endl;
        cout << "\t" << "CAMBIO: " <<endl;
        cout << "\t\tswap(str["<<i<<"]=>"<<str[i];
        cout << ";, str["<<j<<"]=>" <<str[j]<<")";
        swap(str[i], str[j]);
        permutations(str, i+1, n);
        swap(str[i], str[j]);
        cout << endl << "\t" << "Restauracion: " <<endl;
        cout << "\t\tswap(str["<<i<<"]=>"<<str[i];
        cout << ";, str["<<j<<"]=>" <<str[j]<<")";

    }
}

int main() {
    string str = "ABC";
    permutations(str, 0, 3);
    return 0;
}