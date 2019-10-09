from sys import stdout

def CalcPI(precision = 10):
    accum = 0
    for k in range(precision):
        k8 = k * 8
        x = (1 / pow(16, k)) * ((4 / (k8 + 1)) - (2 / (k8 + 4)) - (1 / (k8 + 5)) - (1 / (k8 + 6)))
        accum += x
    return accum


if __name__ == "__main__":
    pi = CalcPI(100)
    print(f'PI = {pi}')
