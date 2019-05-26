from __future__ import print_function

def printHello():
    print('Hello World')
def tambah(inputPertama, inputKedua):
    hasil = inputPertama + inputKedua
    return hasil
def parameterDinami(*inputDinamis):
    for element in inputDinamis:
        print(element)
def bagi(inputPertama, inputKedua):
    hasil = inputPertama * inputKedua
    return hasil
def main():
    bilanganPertama = int(input('Bilangan Pertama : '))
    bilanganKedua = int(input('Bilangan Kedua : '))
    hasil = tambah(bilanganPertama,bilanganKedua)
    print('Hasil : %d '% hasil)
    parameterDinami(1,2,'ilman')
#     belajar Lamda
    hasilLamda = lambda inputPertama, inputKedua: inputPertama * inputKedua
    print(hasilLamda(bilanganPertama,bilanganKedua))
if __name__ == "__main__":
    main()