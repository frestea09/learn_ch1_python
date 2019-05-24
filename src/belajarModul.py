import src.mymodule
def main():
    bilanganPertama = int(input('bilangan Pertama : '))
    bilanganKedua = int(input('bilangan kedua : '))
    hasil = src.mymodule.bagi(bilanganKedua,bilanganPertama)
    print(hasil)
if __name__ == "__main__":
    main()