import random
import string

from Semana10.BinaryHeapDict.MaxHeap import BinaryHeap2
class PriorityQueue():
    def __init__(self):
        self.heap = BinaryHeap2(20, min=False)
        self.hora = 0;
        self.hora_cierre = 540;

    def adelantarHora(self):
        self.hora += 5;

    def get_quality(self, quality):
        if quality == "L":
            return 0
        if quality == "S":
            return 7
        if quality == "G":
            return 15
        if quality == "B":
            return 30
        else:
            return 0
    def agregar(self, nombre, quality):
        oa = self.hora_cierre-self.hora + self.get_quality(quality)
        self.heap.insert(nombre, oa)

    def agregarPriority(self):
        pass

pq = PriorityQueue()

calidades = ["L", "S", "G", "B"]
for i in range(0, 10):
    pq.agregar(''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]), calidades[random.randint(0, 3)])

pq.heap.show()