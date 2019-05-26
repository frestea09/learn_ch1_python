from __future__ import print_function

def main():
    inputVariableNumber = '4lay'
    inputVariabelAlpha = 'Alay'
    inputVariableSpace = ' AlayAnjay'
    hasilNumber = inputVariableNumber.isalnum()
    hasilAlpha = inputVariabelAlpha.isalpha()
    hasilSpace = inputVariableSpace.isspace()
    print('Variabel Number : %s'%inputVariableNumber)
    print('Variabel Alpha : %s'%inputVariabelAlpha)
    print('Variabel Space : %s'%inputVariableSpace)
    print('Hasil Number : %s '%hasilNumber)
    print('Hasil Alpha : %s '%hasilAlpha)
    print('Hasil Space : %s '%hasilSpace)
if __name__ == "__main__":
    main()