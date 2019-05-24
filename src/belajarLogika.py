from __future__ import print_function

def main():
    inputPertama = int(input("Bilangan Pertama : "))
    inputKedua = int(input("Bilangan Kedua : "))
    if(inputPertama>0 )and (inputKedua>0):
        print("Kedua input Bilangan Positif ")
    if(inputPertama<0) or (inputKedua<0):
        print("Salah satu input adalah Negatif")
    if not (inputPertama>0 ):
        print("input Pertama Negatif")
if __name__ == "__main__":
    main()