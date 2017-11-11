#include <iostream>
#include <list>
#include <queue>

using namespace std;

class Graph{
    private:
        int n;
        list<int>* listAd;
        int* incoming;
    public;
        Graph(int n=10);
        void addEdge(int v, int w);
        bool existsIncommingVertex();
        void topologicalSort();
};


Graph::Graph(int n) {
    this->n = n;
    listAd = new list<int>[n];
    incoming = new int[n];
    for (int i = 0; i< n; i++)
        incoming[i]=-1;
}

void Graph::addEdge(int v, int w) {
    listAd[v].push_back(w);
    
    if(incoming[v]<0)
        incoming[v] = 0;
    if(incoming[w]<0)
        incoming[w] =1;
    else
        incoming[w]++;
}

bool Graph::existsIncommingVertex() {
    for (int i = 0; i < n; ++i) {
        if( incoming[i] ==0){
            return true;
        }
    }
    return false;
}

void Graph::topologicalSort() {

    list q
}


int main() {

    Graph g(6);
    g.addEdge(2,4);
    g.addEdge(2,5);
    g.addEdge(1,3);
    g.addEdge(1,4);
    g.addEdge(0,3);
    g.topologicalSort();
    return 0;

}