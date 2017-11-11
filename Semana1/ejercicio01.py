from ctypes import c_longlong as ll

 void test(){
 long operando1 = 76836;
 long operando2 = 100000000000;
 int longitudsegundooperando=14;
 long producto = 0;
 for (int posicionDigito=1; posicionDigito=longitudsegundooperando;posicionDigito++)
 {
 	int digito = (int)(operando2-(operando2/10)*10);
 	for (long contador = digito; contador>0;contador--){
 		producto=producto+operador1;
 		operando2=operando2/10;
 		operando1=operando1*10;
 	}
 	cout <<producto;
 }
 }