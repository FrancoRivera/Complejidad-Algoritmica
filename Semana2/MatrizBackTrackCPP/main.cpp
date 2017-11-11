#include <iostream>
#include <cstring>

using namespace std;

#define M 10
#define N 10

bool isSafe(int mat[M][N], int visited[M][N], int x, int y){
    if (visited[x][y] || !(mat[x][y])) return false;
    return true;
}

bool isValid(int mat[M][N], int visited[M][N], int x, int y){
    if (x < M && y < N && x >= 0 && y>=0) return true;
    return false;

}

void findLongestPath(int mat[M][N], int visited[M][N], int i, int j, int x, int y, int &max_dist, int dist){
    if (i == x && j == y) max_dist = max(max_dist, dist);

    visited[i][j] = 1;

    if(isValid(mat, visited, i+1, j) && isSafe(mat, visited, i+1, j)){
        findLongestPath(mat, visited, i+1, j, x,y, max_dist, dist+1);
    }
    if(isValid(mat, visited, i-1, j) && isSafe(mat, visited, i-1, j)){
        findLongestPath(mat, visited, i-1, j, x,y, max_dist, dist+1);
    }
    if(isValid(mat, visited, i, j+1) && isSafe(mat, visited, i, j+1)){
        findLongestPath(mat, visited, i, j+1, x,y, max_dist, dist+1);
    }
    if(isValid(mat, visited, i, j-1) && isSafe(mat, visited, i, j-1)){
        findLongestPath(mat, visited, i, j-1, x,y, max_dist, dist+1);
    }

    visited[i][j] = 0;


}

void printMatrix(int matriz[M][N]){
    for (int j = 0; j < M; ++j) {
        for (int i = 0; i < N ; ++i) {
            cout<< matriz[M][N] << " ";
        }
        cout <<endl;
    }
}

int main() {

    int matriz[M][N] = {0};

    for (int i = 0; i < 10; ++i) {
        printf("\e[1;1H\e[2J");
        cout<<(rand() % 2);
        printMatrix(matriz);
    }


    int mat[M][N] = {
            {1,0,1,1,1,1,0,1,1,1},
            {1,0,1,0,1,1,1,0,1,1},
            {1,1,1,0,1,1,0,1,0,1},
            {0,0,0,0,1,0,0,1,0,0},
            {1,0,0,0,1,1,1,1,1,1},
            {1,1,1,1,1,1,1,1,1,0},
            {1,0,0,0,1,0,0,1,0,1},
            {1,0,1,1,1,1,0,0,1,1},
            {1,1,0,0,1,0,0,0,0,1},
            {1,0,1,1,1,1,0,1,0,0}
        };

    int visited[M][N];  //declara la matriz M x N;
    memset(visited, 0, sizeof(visited)); //crea la matriz y la llena con 0
    int max_dist=0; //distancia maxima inicial = 0

    findLongestPath(mat, visited, 0,0,5,7, max_dist, 0); //inicia la recursividad

    cout << "Camino Maximo: " << max_dist <<endl; //imprime la distancia maxima.

    return 0;
}

























