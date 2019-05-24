from __future__ import print_function

def main():
    variabelPertama = int(input("Bilangan Pertama : "))
    variabelKedua = int(input("Bilangan Kedua : "))
    daftarNilai  = [1,2,3,4,5,6,7,8,9]
    if(variabelPertama>variabelKedua):
        print("%d > %d : %s"%(variabelPertama,variabelKedua,variabelPertama>variabelKedua))
    if(variabelPertama<variabelKedua):
        print("%d > %d : %s"%(variabelPertama,variabelKedua,variabelPertama<variabelKedua))
    if(variabelPertama<=variabelKedua):
        print("%d <= %d : %s"%(variabelPertama,variabelKedua,variabelPertama<=variabelKedua))
    if(variabelPertama>=variabelKedua):
        print("%d >= %d : %s"%(variabelPertama,variabelKedua,variabelPertama>=variabelKedua))
    if(variabelPertama==variabelKedua):
        print("%d = %d : %s"%(variabelPertama,variabelKedua,variabelPertama==variabelKedua))
    if(variabelPertama!=variabelKedua):
        print("%d != %d : %s"%(variabelPertama,variabelKedua,variabelPertama!=variabelKedua))
    if(variabelPertama in daftarNilai):
        print("%d in %s "%(variabelPertama,variabelPertama in daftarNilai))
    if(variabelKedua in daftarNilai):
        print("%d in %s "%(variabelKedua,variabelKedua in daftarNilai))
if __name__ =="__main__":
    main()