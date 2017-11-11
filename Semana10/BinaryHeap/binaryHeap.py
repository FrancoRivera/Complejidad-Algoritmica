class BinaryHeap():

    def __init__(self, capacity):
        self.heap = [0]*(capacity+1)
        self.capacity = capacity
        self.position = 1
        pass

    def ispower(self, n, base):
        if n == base:
            return True
        if base == 1:
            return False
        temp = base
        while (temp <= n):
            if temp == n:
                return True
            temp *= base

        return False

    def getlevel(self,i):
        level =0
        power = 0
        while i < 2**power:
            level+=1
            power+=1
        return level

    def show(self):
        for i in range(self.capacity):
            if i is 0:
                print("\n\n====================================\n\n")
                continue
            if self.heap[i]==0:
                continue
            if i is 1:
                print(" " * (self.capacity//2) + str(self.heap[1]) + " " * self.capacity)
            else:
                nivel = (i // 2)+1
                print(" "*(int(self.capacity/nivel))+str(self.heap[i])+" "*int(self.capacity/nivel),end="")
                if self.ispower((i+1), 2):
                    print("\n")


    def getLC(self,i):
        return i*2

    def getParent(self, i):
        return (i-1)//2

    def getRC(self,i):
        return i*2+1

    def extract(self):
        self.heap[1] = self.heap[self.getLast()]
        self.heap[self.getLast()]= 0
        self.position -=1
        i = 1
        while(i < self.capacity):
            rc = self.getRC(i)
            lc = self.getLC(i)
            if (rc > lc):
                self.heap[i], self.heap[rc] = self.heap[rc], self.heap[i]

    def getLast(self):
        return self.position-1

    def insert(self, dato):
        if self.position is self.capacity:
            print("Capacidad excedida: " + str(dato))
            return

        self.heap[self.position] = dato
        self.position += 1

        child = self.getLast()
        parent = self.getParent(self.position)

        while self.heap[parent] < self.heap[child] and parent > 0:
            self.heap[parent], self.heap[child]= self.heap[child], self.heap[parent]
            child = int(parent)
            parent = self.getParent(parent)




def main():
    bh = BinaryHeap(22)

    bh.insert(12)
    bh.insert(7)
    bh.insert(6)
    bh.insert(10)
    bh.insert(8)
    bh.insert(20)

    bh.show()



main()

