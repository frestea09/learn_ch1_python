from __future__ import print_function

def getLower(inputLower):
    hasil = inputLower.islower()
    return hasil
def getUpper(inputUpper):
    hasil = inputUpper.isupper()
    return hasil

def main():
    variabelInput = input('Variable Pertama : ')
    variabelLowerInput = input('Variable Kedua : ')
    hasilUpper = getLower(variabelInput)
    hasilLower = getUpper(variabelLowerInput)
    print('hasil : ',hasilLower)
    print('Hasil Upper : ',hasilUpper)
if __name__ == "__main__":
    main()