# ==============================
# ==== Find Match Strings ======
# ==============================

def findMatch(key, val):
    M = len(key)
    N = len(val)

    for i in range(N - M + 1):
        for j in range(M):
            if val[i + j] != key[j]:
                break
        if j == M - 1:
            print("keyterm found at index " + str(i))


val = "AABAACAADAABAAABAA"
key = "AABA"
findMatch(key, val)


# ============================
# ======== POTENCIAS =========
# ============================


def potencia(x, n):
    resultado = int(x);
    for i in range(1, n):
        resultado = resultado * x;
    return (resultado);


def potencia2(x, n):
    if n == 0: return 1
    if n == 1: return x
    if n == 2: return x * x
    y = potencia2(x, int(n / 2))

    if n % 2 != 0:  # n es impar
        return y * y * x
    else:
        return y * y  # n es par


def test():
    base = int(input("Base?: "))
    expo = int(input("Expo?: "))
    res = potencia(base, expo)
    res2 = potencia2(base, expo)
    print("Potencia 1=> " + str(res))
    print("Potencia 2=> " + str(res2))

test()
