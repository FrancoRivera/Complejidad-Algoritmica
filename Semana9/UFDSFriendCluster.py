# include<iostream>

class UfdsRankPathCom():
    def __init__(self, length):
        self.parent = []
        self.rank = [0]*length
        self.length = length
        self.dicc = dict()
        for i in range(length):
            self.parent.append(i)


    def sameSet(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def findSet(self, x):
        if x is not self.parent[x]:
            self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]

    def unionSet(self, x, y):
        if self.dicc.get(x) is None:
            self.dicc[x] = self.length+1
            self.length +=1
        if self.dicc.get(y) is None:
            self.dicc.insert(y)

        x = self.findSet(x)
        y = self.findSet(y)
        if self.sameSet(x,y) is False:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y
                if self.rank[x] is self.rank[y]:
                    self.rank[y] += 1


    def showSet(self):
        for i in range(self.length):
            print("Parent of: " + str(i) + " is " + str(self.parent[i]) +" \n")


def main():

    ubrpc = UfdsRankPathCom(6)
    ubrpc.showSet();
    print("\n")

    ubrpc.unionSet(1, 2)
    ubrpc.unionSet(2, 4)
    ubrpc.unionSet(0, 2)
    ubrpc.unionSet(3, 5)
    print("\n")
    ubrpc.showSet();
    return

main()