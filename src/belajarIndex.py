from __future__ import print_function

def main():
    variableInput = input('input Variabel : ')
    variableCari = input('input Cari : ')
    hasilCari = variableInput.index(variableCari)
    print('variabel : %s'%variableInput)
    print('variable cari : %s'%variableCari)
    print('Hasil : %s'%hasilCari)
if __name__ == "__main__":
    main()