
class Quicksort():

    def partition(self,arr, l, h):
        pivot = arr[h]
        i = l-1
        for j in range(l, h):
            if arr[j] <= pivot:
                i=i+1
                arr[j], arr[i] = arr[i], arr[j]

        arr[i+1], arr[h] = arr[h], arr[i+1]
        return i+1

    def sort(self, a, l, h):
        if l < h:
            p = self.partition(a, l, h)
            self.sort(a, l, p-1)
            self.sort(a, p+1, h)



    def mergeConquer(a, l, mid, r):
        n = r-l +1



    def mergeDevide(self,a, l, r):
        if l > r:
            return
        mid = int((l+r)/2)
        self.mergeDivide(a, l, mid)
        self.mergeDevide(a,mid+1, r)


a = [10, 5, 4, 11, 3, 12]

qs = Quicksort()
print(a)
qs.sort(a, 0, 5)
print(a)