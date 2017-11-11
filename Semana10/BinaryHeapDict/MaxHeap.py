class BinaryHeap2():
    def __init__(self,capacity, min=False ):
        self.heap = {}
        self.min = min
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

    def getlevel(self, i):
        level = 0
        power = 1
        while i > 2 ** power:
            level += 1
            power += 1
        return level

    def show(self):
        j = 0
        for i in range(self.position):
            if i is 0:
                print("\n\n====================================\n\n")
                continue
            nivel = self.getlevel(i+1)
            separation = (int(self.capacity*2/ pow(2,nivel)))
            separation_pre = separation
            if j == 2:
                separation_pre+=5
                j = 0
            else:
                j+=1

            print(" " *separation_pre + str(self.heap[i][0]) +" (" + str(self.heap[i][1])+ ")" + " " *separation, end="")
            if self.ispower((i + 1), 2):
                j = 0
                print("\n")
                '''
                espacio = True
                for i in range(pow(2,nivel+1)):
                    if espacio:
                        print(" " *int((self.capacity / pow(2, nivel + 1))), end="")
                        espacio= False;
                    else:
                        print("-"*(int(self.capacity*3/ pow(2,nivel+1))),end="")
                        espacio = True
                print("\n")
                '''

    def getLC(self, i):
        return i * 2

    def increase(self, key, amount):
        self.heap[key] = amount
        child = key
        parent = child / 2
        while (self.heap[parent] < self.heap[child] and parent > 0):
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            child=parent
            parent=child / 2

    def getParent(self, i):
        return (i) // 2

    def getRC(self, i):
        return i * 2 + 1

    def extract(self):
        self.heap[1] = self.heap[self.getLast()]
        self.heap[self.getLast()] = 0
        self.position -= 1
        i = 1
        while (i < self.position):
            rc = self.getRC(i)
            lc = self.getLC(i)
            if rc >= self.position or lc >= self.position:
                break
            if self.min:
                if (self.heap[rc][1] <= self.heap[lc][1] and self.heap[rc][1] < self.heap[i][1]):
                    self.heap[i], self.heap[rc] = self.heap[rc], self.heap[i]
                if self.heap[lc][1] < self.heap[rc][1] and self.heap[lc][1] < self.heap[i][1]:
                    self.heap[i], self.heap[lc] = self.heap[lc], self.heap[i]
            else:
                if (self.heap[rc][1] >= self.heap[lc][1] and self.heap[rc][1] > self.heap[i][1]):
                    self.heap[i], self.heap[rc] = self.heap[rc], self.heap[i]
                if self.heap[lc][1] > self.heap[rc][1] and self.heap[lc][1] > self.heap[i][1]:
                    self.heap[i], self.heap[lc] = self.heap[lc], self.heap[i]
            i +=1

    def getLast(self):
        return self.position - 1

    def insert(self,nombre, dato):
        if self.position is self.capacity:
            print("Capacidad excedida: " + str(dato))
            return

        self.heap[self.position] = (nombre,dato)


        child = self.getLast()
        parent = self.getParent(self.position)
        self.position += 1
        if self.min:
            while parent > 0:
                if self.heap[parent][1] >= self.heap[child][1]:
                    self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                child = int(parent)
                parent = self.getParent(parent)
        else:
            while parent > 0:
                if self.heap[parent][1] <= self.heap[child][1]:
                    self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                child = int(parent)
                parent = self.getParent(parent)


def main():
    bh = BinaryHeap2(22, min=False)

    bh.insert("franco", 570)
    bh.insert("luis", 555)
    bh.insert("jose",547)
    bh.insert("yolo",570)
    bh.insert("swag",555)
    bh.insert("haha",547)
    bh.insert("lmao", 570)
    bh.insert("nigg", 501)

    bh.show()
    bh.extract()
    bh.show()
