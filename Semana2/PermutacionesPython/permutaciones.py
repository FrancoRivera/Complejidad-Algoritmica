
import datetime

def swap(str, a, b):
    n_str = list(str)
    aux = n_str[a]
    n_str[a] = n_str[b]
    n_str[b] = aux
    return ''.join(n_str)


def permutaciones(str, i, n):
    if i == n-1:
        print(str)
        return

    for j in range(i, n):
        # if str[i] == str[j] and i != j:
        #    continue
        #
        str = swap(str, i, j)
        permutaciones(str, i+1, n)
        str = swap(str, i, j)

past = datetime.datetime.now()



string = "Abc"
permutaciones(string, 0, len(string))
present = datetime.datetime.now()
print(present-past)