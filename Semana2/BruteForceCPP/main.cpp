#include <iostream>
#include "Operation.h"
#include "StringMatching.h"


using namespace std;

int main(){
	cout <<"FB-Example01, String Match " << endl;

	//Fuerza bruta
	char * a = (char*)"UPC, exigete, innova";
	char *b = (char*)"exigete";

	StringMatching* sm = new StringMatching();

	int n = 20;
	int m = 7;

	double beginTime=clock();
	sm->findMatch(a,b,n,m);

	double endTime=clock();
	int t= endTime-beginTime;


	cout << "Execution Time =>" << (double)t/((double)CLOCKS_PER_SEC) << endl;
	cout << "\nString val=> " <<a <<endl;
	cout << "String key=> " <<b <<endl;


	// PATRONES MAQUINA DE ESTADOS

	beginTime=clock();

	string pat[] = {"ab", "aaab", "abbb", "aaabb", "caabb", "abc"};

	for (int i = 0; i<6; i++){
		string cad = (pat[i].c_str());
		char* subcad = &*cad.begin();
		int longitud = cad.size();

		cout << pat[i] << " es => ";
		cout << sm->StringScanner(cad, longitud) << endl;
	}

	endTime=clock();
	t= endTime-beginTime;

	cout << "\nExecution Time =>" << (double)t/((double)CLOCKS_PER_SEC) << endl;
	cout << "\nString val=> " <<a <<endl;
	cout << "\nString key=> " <<b <<endl;


    Operation* op = new Operation();
    cout << "sum(5)=> " << op->sum(5) << endl;
    cout << "mul(5)=> " << op->mul(5) << endl;
    int val[]={-1,2,0,1,2,3};

    n= sizeof(val) / sizeof(int);

    cout << op->sumRec(val, 0, n-1);


    return 0;


	}

