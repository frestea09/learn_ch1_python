from __future__ import print_function

def main():
    bilanganPertama = int(input('Bilangan Pertama : '))
    bilanganKedua = int(input('Bilangan Kedua :'))
    hasilJumlah = bilanganPertama + bilanganKedua
    hasilKurang = bilanganPertama - bilanganKedua
    hasilKali = bilanganPertama * bilanganKedua
    hasilBagi = bilanganPertama / bilanganKedua
    hasilTampaKoma = bilanganPertama // bilanganKedua
    hasilModulus = bilanganPertama % bilanganKedua
    hasilPangkat = bilanganPertama ** bilanganKedua
    print("Bilangan Pertama : %d"%bilanganPertama)
    print("Bilangan Kedua : %d"%bilanganKedua)
    print("%d + %d = %d "%(bilanganPertama,bilanganKedua,hasilJumlah))
    print("%d - %d = %d "%(bilanganPertama,bilanganKedua,hasilKurang))
    print("%d * %d = %d "%(bilanganPertama,bilanganKedua,hasilKali))
    print("%d / %d = %d "%(bilanganPertama,bilanganKedua,hasilBagi))
    print("%d // %d = %d "%(bilanganPertama,bilanganKedua,hasilTampaKoma))
    print("%d mod %d = %d "%(bilanganPertama,bilanganKedua,hasilModulus))
    print("%d ^ %d = %d "%(bilanganPertama,bilanganKedua,hasilPangkat))

if __name__ == "__main__":
    main()